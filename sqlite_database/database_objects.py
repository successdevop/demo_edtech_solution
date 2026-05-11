"""Classes to represent the structure of an SQLite table, columns, etc."""
from __future__ import annotations

from typing import Iterable
from abc import abstractmethod, ABC
import datetime as dt
import os.path
import sqlite3


CONVERT_DATES = True  # set False to *NOT* use the adapters and converters.


class Expandable(ABC):
    """An abstract class for things that contain other things.

    For example, a Column can contain Constraints, and a Table can contain Columns.
    """
    name: str

    @abstractmethod
    def expand(self) -> Iterable:
        """Return iterable (or Generator) of the contained objects."""

    def __str__(self):
        return f'{type(self).__name__.upper()} {self.name}'


class Constraint:
    """Representation of a Column's constraints."""
    def __init__(self, name, value=None):
        self.name = name.upper()
        self.value = value

    def __str__(self):
        return self.name + (f' {self.value}' if self.value is not None else '')


class Column(Expandable):
    """Represents an SQLite Column."""
    def __init__(self, _id: int, name: str, col_type, not_null, default, pk):
        self.id = _id
        self.name = name
        self.type = col_type
        self.constraints = []
        if not_null == 1:
            self.constraints.append(Constraint('NOT_NULL'))
        if default is not None:
            self.constraints.append(Constraint('DEFAULT', default))
        if pk != 0:  # pk is the 1-based index of the column within the primary key.
            self.constraints.append(Constraint('PRIMARY_KEY'))

    def expand(self) -> Iterable:
        yield from self.constraints
        # equivalent to:
        # for constraint in self.constraints:
        #     yield constraint

    def __str__(self):
        return f'{self.name}: {self.type}'


class Table(Expandable):
    """An SQLite Table, with its columns."""
    def __init__(self, name: str):
        self.name = name
        self.columns: list[Column] = []

    def expand(self):
        yield from self.columns


class View(Expandable):
    """An SQLite View."""
    def __init__(self, name: str):
        self.name = name
        self.columns: list[Column] = []

    def expand(self):
        yield from self.columns


class Database(Expandable):
    """Class for working with an SQLite database."""
    @classmethod
    def get_name(cls, path: str):
        return os.path.basename(os.path.normpath(path))

    def __init__(self, path: str):
        self.full_path = path
        self.name = type(self).get_name(path)
        self.tables: list[Table] = []
        self.views: list[View] = []
        self.connection: sqlite3.Connection | None = None
        self.connected = False

        self.connect()
        self.load_structure()
        self.close()

    def expand(self):
        yield from self.tables
        yield from self.views

    def connect(self):
        self.connection = sqlite3.connect(self.full_path, isolation_level=None, detect_types=sqlite3.PARSE_DECLTYPES)
        self.connected = True

    def close(self):
        if self.connected:
            self.connection.commit()
            self.connection.close()
        self.connected = False

    def load_structure(self):
        """Use SQLite pragmas to load the tables and views (with their columns and the column constraints)."""
        tables_cursor = self.connection.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.tables = [Table(table[0]) for table in tables_cursor]
        tables_cursor.close()
        # Now get the columns
        for table in self.tables:
            fk_cursor = self.connection.execute(f"PRAGMA foreign_key_list('{table.name}');")
            fk_list = fk_cursor.fetchall()
            fk_cursor.close()
            columns_cursor = self.connection.execute(f"PRAGMA table_info('{table.name}');")
            for column in columns_cursor:
                new_column = Column(*column)
                table.columns.append(new_column)
                for fk in fk_list:
                    if fk[3] == new_column.name:
                        new_column.constraints.append(Constraint('FOREIGN_KEY', f'{table.name}.{fk[3]}={fk[2]}.{fk[4]}'))

            columns_cursor.close()

        views_cursor = self.connection.execute("SELECT name FROM sqlite_master WHERE type='view';")
        self.views = [View(view[0]) for view in views_cursor]
        views_cursor.close()
        # Now get the columns
        for view in self.views:
            columns_cursor = self.connection.execute(f"PRAGMA table_info('{view.name}');")
            for column in columns_cursor:
                view.columns.append(Column(*column))
            columns_cursor.close()

    def run_query(self, query: str) -> sqlite3.Cursor:
        """Run a SQL query and return the cursor object."""
        try:
            cursor = self.connection.execute(query)
        except sqlite3.Error as e:
            raise RuntimeError(str(e))
        return cursor

    def run_script(self, script: str) -> None:
        """Execute the SQL statements in a script."""
        cursor = None
        try:
            cursor = self.connection.executescript(script)
        except sqlite3.Error as e:
            raise RuntimeError(str(e))
        finally:
            if cursor is not None:
                cursor.close()

    def get_rows_affected(self) -> int:
        """Return the number of rows affected by the last query."""
        return self.connection.execute('SELECT changes();').fetchone()[0]

    def __str__(self):
        return f'{self.name}'


databases: dict[str, Database] = {}


def add_database(path_to_db: str) -> Database:
    """Add the selected database to the list"""

    db = Database(path_to_db)
    databases[db.name] = db
    return db


def convert_datetime(val: bytes) -> dt.datetime:
    """Convert ISO 8601 datetime to datetime.datetime object after reading from the database."""
    return dt.datetime.fromisoformat(val.decode())  # .astimezone()


def adapt_datetime(val: dt.datetime) -> str:
    """Adapt datetime.datetime to ISO 8601 date string for storing in the database.

    Converts the datetime to UTC before storing.
    """
    return dt.datetime.isoformat(val.astimezone(dt.timezone.utc))


def convert_date(val: bytes) -> dt.date:
    """Convert ISO 8601 date to datetime.date object after reading from the database."""
    return dt.date.fromisoformat(val.decode())


def adapt_date(val: dt.date) -> str:
    """Adapt datetime.date to ISO 8601 date string for storing in the database."""
    return dt.date.isoformat(val)


def convert_timestamp(val: bytes) -> float | str:
    """Return timestamp columns as floats after reading.

    Python does not have a ``timestamp`` type, so we can't create a corresponding
    adapter. Storing datetime objects in a timestamp field could cause problems,
    and we don't have an adapter to convert them to timestamps (floats).
    Attempt to convert to a timestamp float value.
    """
    try:
        return float(val)
    except ValueError:
        # Attempt to interpret as a datetime
        try:
            return dt.datetime.fromisoformat(val.decode()).timestamp()
        except ValueError:
            # Not much more we can do!
            return val.decode()


def register_datetime_adapters():
    """Register an adapter and a converter for storing datetime and timestamp objects."""
    # Adapters are called before writing to the database.
    sqlite3.register_adapter(dt.datetime, adapt_datetime)
    sqlite3.register_adapter(dt.date, adapt_date)
    # Converters are called after reading from the database.
    sqlite3.register_converter("datetime", convert_datetime)
    sqlite3.register_converter("date", convert_date)
    sqlite3.register_converter('timestamp', convert_timestamp)


# Register the datetime adapters and converters.
if CONVERT_DATES:
    register_datetime_adapters()

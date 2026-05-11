"""A very basic GUI front-end to SQLite databases"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

import configparser
import os.path

from database_objects import Database, databases, add_database
from ui_widgets import FrameTree, TableView, MessageEntry, RefocusButton, FocusNotebook

VERSION = '1.10'
ALLOW_SCRIPTS = False

# ******************************************************************************
# **                    Configuration options and functions                   **
# ******************************************************************************
_config_filename = os.path.join(os.path.expanduser('~'), 'lpa_sqlbrowser.config')
config = configparser.ConfigParser(empty_lines_in_values=False)
config.optionxform = str  # option names are case-sensitive


def _update_config():
    with open(_config_filename, 'w') as config_file:
        config.write(config_file)


def store_entry(section, option, value):
    """Helper function to store a value."""
    str_value = str(value)
    if not config.has_section(section):
        config.add_section(section)

    if config[section][option] != str_value:
        # don't update if nothing's changed
        config[section][option] = str_value


if not config.read(_config_filename):
    config['SCREEN'] = {
        'window_width': '1024',
        'window_height': '768',
        'window_x': '0',
        'window_y': '0',
        'large_font_size': '24',
        'resize_database_view': 'False',
    }
    _update_config()

duplicate_message = ('You already have a database called %s open.\n'
                     'Having the same name twice in the databases list could be confusing.\n\n'
                     'Please use a new name, or restart the program to remove the existing database from the list.')


def on_close_callback():
    """Save the main window size and position when the program is closed."""
    width = main_window.winfo_width()
    height = main_window.winfo_height()
    x = main_window.winfo_x()
    y = main_window.winfo_y()
    if x < 0:
        x = 0
    if y < 0:
        y = 0
    store_entry('SCREEN', 'window_width', width)
    store_entry('SCREEN', 'window_height', height)

    store_entry('SCREEN', 'window_x', x)
    store_entry('SCREEN', 'window_y', y)
    _update_config()

    disconnect_databases()

    main_window.update_idletasks()
    main_window.update()
    main_window.destroy()


def check_duplicate_name(path: str) -> tuple[bool, str]:
    """Return True if the database name already exists in the dictionary."""
    name = Database.get_name(path)
    return name in databases, name


def verify_sqlite3_file(filename: str) -> bool:
    """Check that the specified filename is (probably) an SQLite 3 database."""
    with open(filename, 'rb') as file:
        header = file.read(16)
        return header == b'SQLite format 3\0'


def create_database():
    message_label.clear_text()
    file_types = (('SQLite databases', '*.db *.sqlite'), ('All files', '*'))
    db_path = filedialog.SaveAs(main_window, filetypes=file_types).show()

    if db_path:
        # Check that we don't already have a database with that name loaded.
        exists, name = check_duplicate_name(db_path)
        if exists:
            messagebox.showwarning('Create database', duplicate_message % name)
        else:
            loaded_database = add_database(db_path)
            database_tree.insert(loaded_database)


def get_database_file():
    """Open an SQLite database file."""
    message_label.clear_text()
    file_types = (('SQLite databases', '*.db *.sqlite'), ('All files', '*.*'))

    filenames = filedialog.askopenfilenames(
        parent=main_window,
        title='Select database(s) to open...',
        filetypes=file_types
    )
    if filenames:
        error_file_list = []
        for file_name in filenames:
            # Check that we don't already have a database with that name loaded.
            exists, name = check_duplicate_name(file_name)
            if exists:
                messagebox.showwarning(
                    'Open database',
                    duplicate_message % name
                )
                continue
            if verify_sqlite3_file(file_name):
                loaded_database = add_database(file_name)
                database_tree.insert(loaded_database)
            else:
                error_file_list.append([file_name])

        # Now display dialogue if there were invalid files.
        if error_file_list:
            results_table.display_rows(['Invalid files'], error_file_list)
            message_label.display_error(f'Attempted to open {len(error_file_list)} invalid files.')
            messagebox.showerror(
                'Open database',
                f'Some files were not valid SQLite databases',
                detail='Check the results pane for details.'
            )


def connect_database() -> Database | None:
    """Open the database selected in the TreeView"""
    message_label.clear_text()
    disconnect_databases()  # close any database that's already open.
    db_name = database_tree.get_parent_object()
    if db_name is not None:
        db = databases[db_name]
        db.connect()
        database_tree.tag_item(db_name)
        return db
    else:
        num_loaded = len(databases)
        if num_loaded == 0:
            message_label.display_error('Please load a database with the Open button, or create a new one with New.')
        elif num_loaded > 1:
            message_label.display_error('Please select a database to connect to.')
        # else: the calling code will open the only loaded db automatically.
        return None


def disconnect_databases():
    """Close the open database(s)"""
    for key, db in databases.items():
        if db.connected:
            db.close()


def get_database_to_connect_to() -> Database | None:
    # See if a database is already connected.
    for name, db in databases.items():
        if db.connected:
            result = db
            break
    else:
        # We didn't break out of the loop, so no connected database was found.
        # If there's only one database loaded, we'll use that.
        if len(databases) == 1:
            result = next(iter(databases.values()))
            if not result.connected:
                result.connect()
                database_tree.tag_item(result.name)
        else:
            # Attempt to connect to the selected database if there is one.
            result = connect_database()
    return result


def parse_sql_entry() -> str:
    """Not really parsing, just stripping blanks and comments."""
    sql = code_tabs.get_active_editor().get_text().strip()

    # Now read lines of text and strip out any comments. SQLite accepts comments
    # starting with -- but we'll also remove any lines starting with # or //
    sql_lines = sql.split('\n')
    # delete commented lines.
    valid_lines = [True] * len(sql_lines)
    for index, line in enumerate(sql_lines):
        for comment_marker in ('#', '--', '//'):
            if line.strip().startswith(comment_marker):
                valid_lines[index] = False
    valid_sql = []
    for index, (line, keep) in enumerate(zip(sql_lines, valid_lines)):
        if keep and len(line) > 0:
            valid_sql.append(line.strip())

    sql = ' '.join(valid_sql)
    message_label.display_message(f'Executing {sql}')
    return sql


def run_query():
    """Run the editor query. Called by the run_query button."""
    message_label.clear_text()
    results_table.clear()

    sql = parse_sql_entry()
    if sql == '':
        message_label.display_error('Please enter a valid SQL statement.')
        return
    if not sql.endswith(';'):
        message_label.display_error('SQL not terminated with a semi-colon ;')
        return

    connected_database = get_database_to_connect_to()

    if connected_database is None:
        messagebox.showinfo('Connect', message='Please connect to a database.')
        return
    try:
        cursor = connected_database.run_query(sql)
    except RuntimeError as e:
        message_label.display_error(f'{connected_database.name} — {e}')
    else:
        results = cursor.fetchall()
        if results:
            column_names = [description[0] for description in cursor.description]
            results_table.display_rows(column_names, results)
        message_label.display_message(f'Query returned {len(results_table)} rows.')
        cursor.close()

        # Now consider if the query has changed the database structure.
        for command in ('create', 'alter', 'modify', 'drop', 'rename'):
            if sql.lower().startswith(command):
                # Update the database object's structure, then cause the Treeview to refresh.
                connected_database.load_structure()
                database_tree.reload_structure(connected_database.name, connected_database)
                break

        # For insert and update, it would be nice to display the number of rows affected.
        for command in (('insert', 'inserted'), ('update', 'updated'), ('delete', 'deleted')):
            if sql.lower().startswith(command[0]):
                rows_affected = connected_database.get_rows_affected()
                message_label.display_message(f'{rows_affected} row{"s" if rows_affected != 1 else ""} {command[1]}.')
                break


def execute_script():
    """Execute the script in the editor. Called by the execute_script button."""
    message_label.clear_text()
    results_table.clear()

    connected_database = get_database_to_connect_to()

    if connected_database is None:
        messagebox.showinfo('Connect', message='Please connect to a database.')
        return
    try:
        sql = parse_sql_entry()
        if sql == '':
            message_label.display_error('Please enter a valid SQL script.')
            return

        connected_database.run_script(sql)
    except RuntimeError as e:
        message_label.display_error(f'{connected_database.name} — {e}')
    else:
        # Refresh the treeview entry.
        connected_database.load_structure()
        database_tree.reload_structure(connected_database.name, connected_database)


def set_fonts():
    if font_button['text'] == 'Large fonts':
        font_button['text'] = 'Small fonts'
        font_button.update_idletasks()
        # set large fonts for query_text and results_table.
        code_tabs.set_font_size(large_font_size)
        results_table.set_font_size(large_font_size)
        message_label.set_font_size(large_font_size)
        if 'frame' in full_pane.panes()[0] or resize_database_view:
            database_tree.set_font_size(large_font_size)
    else:
        font_button['text'] = 'Large fonts'
        font_button.update_idletasks()
        code_tabs.set_font_size(0)
        results_table.set_font_size(0)
        message_label.set_font_size(0)
        database_tree.set_font_size(0)


def save_file():
    message_label.clear_text()

    editor = code_tabs.get_active_editor()
    if editor.file_path == '':
        file_types = (('Load SQL file', '*.sql *.txt'), ('All files', '*'))
        main_window.update()
        file_path = filedialog.SaveAs(main_window, filetypes=file_types).show()

        if file_path:
            # Add .sql extension if an extension not specified.
            name, ext = os.path.splitext(file_path)
            if ext == '':
                file_path += '.sql'
        else:
            return
    else:
        file_path = editor.file_path

    try:
        with open(file_path, 'w') as file:
            file.write(code_tabs.get_active_editor().get_text())
    except Exception as e:
        message_label.display_error(f'Error saving file: {e}')
    else:
        # Update the editor's path
        code_tabs.on_saved(file_path)
        message_label.display_message(f'Saved SQL to {file_path}')


def load_file():
    message_label.clear_text()
    file_types = (('Load SQL file', '*.sql *.txt'), ('All files', '*'))
    file_path = filedialog.Open(main_window, filetypes=file_types).show()

    if file_path:
        try:
            with open(file_path, 'r') as file:
                text = file.read()
            if text[-2:] == '\n\n':
                # The Text widget will add another '\n' so strip off the final linefeed.
                text = text[:-1]
            code_tabs.load(file_path, text)

        except UnicodeError:
            message_label.display_error(f'Invalid code file {file_path}')
        else:
            message_label.display_message(f'{file_path} loaded')


def swap_panes():
    if 'frame' in full_pane.panes()[0]:
        # The left pane was the Databases pane, insert it with weight = 1
        weight = 1
    else:
        # The left pane was the main edit and results pane, weight = 100
        weight = 100

    left = full_pane.panes()[0]
    full_pane.forget(left)  # remove the left pane,
    full_pane.add(left, weight=weight)  # adding it again will put it to the right.


def on_double_click(_):
    database_tree.set_font_size(large_font_size)


# ******************************************************************************
# ******************************************************************************
# ******                    The main code starts here.                    ******
# ******************************************************************************
# ******************************************************************************
main_window = tk.Tk()

window_width = config.getint('SCREEN', 'window_width', fallback=1024)
window_height = config.getint('SCREEN', 'window_height', fallback=768)
window_x = config.getint('SCREEN', 'window_x', fallback=0)
window_y = config.getint('SCREEN', 'window_y', fallback=0)
large_font_size = config.getint('SCREEN', 'large_font_size', fallback=0)
resize_database_view = config.getboolean('SCREEN', 'resize_database_view', fallback=False)

# Ensure that the settings weren't saved with a larger display size than we're currently using
max_width, max_height = main_window.maxsize()
if window_x > max_width:
    # reset to zero
    window_x = 0
if window_width > max_width:
    window_width = max_width

if window_y > max_height:
    # reset to zero
    window_y = 0
if window_height > max_height:
    window_height = max_height

main_window.geometry(f'{window_width}x{window_height}{window_x:+}{window_y:+}')
main_window.title(f'LPA Sqlite Browser v{VERSION}')

main_window.protocol('WM_DELETE_WINDOW', on_close_callback)

ttk.Style().theme_use('clam')
# ttk.Style().theme_use('alt')
# ttk.Style().theme_use('default')
# ttk.Style().theme_use('classic')

main_window.config(padx=16, pady=16)

main_window.rowconfigure(0, weight=10)
main_window.rowconfigure(1, weight=0)
main_window.columnconfigure(0, weight=100)

# The paned window – divides the screen vertically
full_pane = ttk.PanedWindow(main_window, orient='horizontal')
full_pane.grid(row=0, column=0, sticky='nsew')

# ******************************************************************************
# **                     listbox frame (left-hand side)                       **
# ******************************************************************************
left_frame = ttk.Frame(full_pane, borderwidth=2, relief='sunken')
left_frame.rowconfigure(0, weight=1)
left_frame.rowconfigure(1, weight=100)
left_frame.columnconfigure(0, weight=1)

database_toolbar = ttk.Frame(left_frame)
database_toolbar.grid(row=0, column=0, sticky='nsew', ipadx=0)
database_toolbar.rowconfigure(0, weight=1)
database_toolbar.columnconfigure(0, weight=1, minsize=2)
database_toolbar.columnconfigure(1, weight=1, minsize=2)
database_toolbar.columnconfigure(2, weight=1, minsize=2)
database_toolbar.bind('<Double-Button-1>', on_double_click)

# ******************************************************************************
# **                 Query and results frame (right-hand side)                **
# ******************************************************************************

right_pane = ttk.PanedWindow(full_pane, orient='vertical')

# ********************************
# **  Top frame, the SQL code.  **
# ********************************
code_pane = ttk.Frame(right_pane, borderwidth=2, relief='sunken')
code_pane.rowconfigure(0, weight=0)
code_pane.rowconfigure(1, weight=10)
code_pane.columnconfigure(0, weight=1)

code_tabs = FocusNotebook(code_pane, run_function=run_query)
code_tabs.grid(row=1, column=0, sticky='nsew')

# The button toolbar on the editor pane.
editor_toolbar = ttk.Frame(code_pane, relief='sunken')
editor_toolbar.grid(row=0, column=0, sticky='nsew')
editor_toolbar.rowconfigure(0, weight=1)
editor_toolbar.columnconfigure(0, weight=1)

# **************************************
# ** Bottom frame, the query results. **
# **************************************
results_pane = ttk.Frame(right_pane)
results_pane.rowconfigure(0, weight=1)
results_pane.columnconfigure(0, weight=1)

results_table = TableView(results_pane, large_font_size=large_font_size, relief=tk.SUNKEN)
results_table.grid(row=0, column=0, sticky='nsew')

# ***************************************
# **  Add the panes to the right pane. **
# ***************************************
right_pane.add(code_pane, weight=1)
right_pane.add(results_pane, weight=1)

full_pane.add(left_frame, weight=1)
full_pane.add(right_pane, weight=100)

# Add the database pane toolbar buttons.
open_db_button = RefocusButton(database_toolbar, focus_window=code_tabs, text='Open',
                               command=get_database_file, padding=0)
open_db_button.grid(row=0, column=0)

new_db_button = RefocusButton(database_toolbar, focus_window=code_tabs, text='New', command=create_database,
                              padding=0)
new_db_button.grid(row=0, column=1)

connect_db_button = RefocusButton(database_toolbar, focus_window=code_tabs, text='Connect',
                                  command=connect_database, padding=0)
connect_db_button.grid(row=0, column=2, )

database_tree = FrameTree(left_frame, title='Databases')
database_tree.grid(row=1, column=0, sticky='nsew')

# Add the editor toolbar buttons.
run_query_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='Run query', command=run_query, underline=0)
run_query_button.pack(side='left')
if ALLOW_SCRIPTS:
    execute_script_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='Execute script', command=execute_script)
    execute_script_button.pack(side='left')

font_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='Large fonts', command=set_fonts)
font_button.pack(side='right')
save_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='Save code', command=save_file)
save_button.pack(side='right')
load_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='Load code', command=load_file)
load_button.pack(side='right')
load_button = RefocusButton(editor_toolbar, focus_window=code_tabs, text='\u21d0|\u21d2', command=swap_panes)
load_button.pack(side='right')

# ******************************************************************************
# **                          The bottom message bar                          **
# ******************************************************************************
message_frame = ttk.Frame(main_window)
message_frame.grid(row=1, column=0, sticky='nsew')
message_frame.rowconfigure(0, weight=0)
message_frame.columnconfigure(0, weight=0)
message_label = MessageEntry(message_frame)
message_label.pack(side='left', expand=1, fill='both', anchor='w')

main_window.mainloop()

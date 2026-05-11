"""ui_widgets.py

This module provides a set of classes useful in a graphical user
interface (GUI) built using tkinter.

It includes:

- FocusNotebook: A ttk Notebook that returns focus to the edit window when it
                 receives focus. It also includes a close button for each tab.

- SimpleEditor: A tkinter Text box with line numbering and an integrated scrollbar.
                Tabs expand to 4 spaces, and Ctrl-/ can be used to comment out
                lines of code.

- RefocusButton: A Button that returns focus to another window after
                 executing its command.

- FrameTree: A tkinter TreeView, wrapped in a Frame, that automatically inserts
             child objects if passed something that implements ``Expandable``.
             Useful to display the tables and columns of an SQLite database.

- TableView: A ttk Treeview (wrapped in a Frame) that behaves like a data table.
             Useful for displaying data from a database cursor, for example.


Although it's being used specifically with database objects and queries in this
project, the classes have been kept general – I've avoided passing a cursor, for
example, so that the classes can be used in other applications.
"""
from __future__ import annotations

import os
import tkinter as tk
from tkinter import ttk
from tkinter import font

from database_objects import Expandable


class FocusNotebook(ttk.Notebook):
    """A ttk Notebook that returns focus to the edit window when it receives focus."""

    # Base-64 encoded png images. These are Class attributes, so we don't duplicate for each instance.
    image_close_data = r"""
        iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA9hAAAPYQGoP6dpAAACJElEQVQ4EaWTwWsTURDGv7ebTbqt
        wYIiFgseBHsUczBdW4I9iKIUCgZEBMGDJ0XQ/0APehDUgx4Ee6kUkaYnQVCRorU0OVQEDxIh0kNtRJqamKa72d2368xLNlrBHHRg2H0z
        v/nezL59wH+a4PrSyNCAZiZygeOmEYZ6V00hpNZjFALbze5bKJZjDGtmPJfMpK1kZljAMLrWw/P0+pu8RT5D4KgSCBwv3ZtKCbf0Efqe
        /ZArRcqFfwgJ6INDkF8+gdnai/lhBjRFUdtBM4TYvhfmsQswDp6E/90ht9vuqBjnmGE2GrUlQCp+o4nN9+9gL75EIjWGxMgEvJqjnN85
        xjlmmI1MjcALudGEv95AdXoSNBL6xk6oJ4SAaR1FY+4ZfsxO8c7QiY2sIxA0XPhVW8XXJx9QmxLJ4+NqXX/+FNVHD1UxBwxiI+sIeLaH
        Zr2tTLtKT0YMpOu3crQ7W4zYyH4TcAlywC3vvngJ/eMTqMzmFLfjVJZEJL7ev6e6iNt/64BmG7x6BVzw7fETrNy+owS4eNeZ00qEYz3U
        gfoDKfurg00X5oGUAstT01i+caszc+naTRrJx8C5s6i8eg2P2Hh7hkhAkqi+9nYJ9vnLWJtfpOIo1SI/XL+L8lwBlYUl7Bw9xALqIynK
        D0QhWC1ZvdZhYYsY+jJH2vpbH3xGxCBYLYZUk+esEohpYXZbbXmmf+MzXQZ0vUx0DtIPtDzXbJX/x9VPTW4F5tojtkcAAAAASUVORK5CYII="""
    image_close_active_data = r"""
        iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAA9hAAAPYQGoP6dpAAABXklEQVQ4EaWS3UoDQQyFs239qVUo
        VMQF73wIfZC+pT6Ggl73uuiFUJG2iH9F7ez6nenMsF1WVDyQTprknGSyY/ZPZOKPzfKW2XlhdsLf9g+ajtpraofHZhNfe2N2OTUr3s3K
        35hq4VyIHCdY5nR2BNReZxNiTietHRN0mMajzUherVuWtoG/rJliyqmjaoF0rKMfQYQPrJVlvrDgfFEC7GJbkBfE3vA3FQxIAhpbIo+Y
        yD0IOgV1fsV/8v/Wt5wENJYEhDkm8h5E4RlfwhG6TkQS+CTCF0ioLlJ+NZdIxJNfFTgk0af7LFxhgO/w74N84w6iwBFFIjxAuAsEkQ+C
        iGLb2Go7tQm6JFQ4gXCLHzHGkUhOTlOpWZwiXsEtWC4vzH8qnXWMCEh4xrmPIeDX5B8S29fbLndIIGS9b0w51agWzhXuaomMMeSxnPXN
        Trmbf2FKNoEP60QWpyn/59gXvaqLJ0A6+TQAAAAASUVORK5CYII="""
    image_close_pressed_data = r"""
        iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsSAAALEgHS3X78AAACUklEQVQ4EW1TyW4aURAshmEPm8IiBcsBCXHgYJ84wJ/w
        jXbO5BxfA7GcU2BASFgWQuDBGLPOMOlqAvYhD43mAa+qq6r7+fb7vbfZbLDdbrHdbeHsHbiuC8/z8HH5fD7w8fv9CAaDiESjiEYiMNfrNUajEWzbxmKxwGq1
        gpB+ICDREWwYBkKhEBLJBDKZLL5eXr4TDIdDzGYzBAIBrSQYws4iDocD+FBtLpfDxcVSSDIwd7sdptMper0elsslyuWyWqAlAiiblcPhkKrqdrtaiDZ2csak
        XwIdx0GpVEK9XocrQEsIX19flSCfz6NQKIDFnp6esBOLtM5zBqvwD1akf+5dIaNM7hkapZ6CJpCVTzmZTJvVeXg8HsPqWyh8KWjS1WpV32+rN5hC9PDwW8Nm
        kFQunmAwpZOK+XyO9s+2yozH42g0GigWi0jEEwrudv/g5eVF1SqBYE0SUMVeFDAL7mnl2X7W75ROYiq07bnmEg6HtSixSqAKJBhaqVQqKu9x9Ii7H3dIp1PS
        BT+y2axk8RmWZSGZTB4J2CG2SRUIAcNKp9P6/f7+F25ubnB7+02JJ5OJ2ClpS88tFgVKQAX8kQlTvmX10Gp9134PBgPZt+C4jga4Wq+0I+5BQpQ5MzkkfI5A
        C51O5zzS9MjVbrfR7/d1zzzC0gXIhBs+AyZHNyoXg2F58mEOEbkkfP63UqmU+PfALnEaTR68ur5Cs9nE7HkmQyKD9O82Mhsu5nR6E8SsarUaYrEYfNIej/Lp
        nzkQzExO4CPy/WJxMjlIsU8xUR7DX7RKq7qNZLBjAAAAAElFTkSuQmCC"""

    images: tuple[tk.PhotoImage, tk.PhotoImage, tk.PhotoImage]
    _active: int | None = None
    tab_close_image: tk.PhotoImage | None = None
    tab_close_active_image: tk.PhotoImage | None = None
    tab_close_pressed_image: tk.PhotoImage | None = None

    def __init__(self, window, run_function=None, *args, **kwargs):
        self._active = None  # Used when closing a tab.
        self.initialize_notebook_style()
        kwargs["style"] = "FocusNotebook"

        self.callable = run_function

        super().__init__(window, *args, **kwargs)

        style = ttk.Style()
        self.default_font = style.lookup('TNotebook.Tab', 'font')
        self.default_font_size = 0

        self.NEW_TAB_HEADING = 'New tab'
        self.PADDING_SPACES = '    '

        self._create_empty_tab()

        self.bind('<FocusIn>', self.on_focus_in)
        self.bind('<ButtonPress-1>', self.on_close_press, True)
        self.bind('<ButtonRelease-1>', self.on_close_release)

    def _create_empty_tab(self) -> None:
        """Create a new empty editor tab."""
        new_tab = SimpleEditor(self, comment_symbol='--', relief='sunken', run_function=self.callable)
        new_tab.grid(row=1, column=0, sticky='nsew')
        self.add(new_tab, text=self.NEW_TAB_HEADING)

    def initialize_notebook_style(self):
        """Initialize the notebook style with close buttons while preserving the native look"""
        style = ttk.Style()

        # Initialize tab close images
        class_type = type(self)
        if class_type.tab_close_image is None:
            class_type.tab_close_image = tk.PhotoImage('image_close', data=type(self).image_close_data)
            class_type.tab_close_active_image = tk.PhotoImage('image_close_active',
                                                              data=type(self).image_close_active_data)
            class_type.tab_close_pressed_image = tk.PhotoImage('image_close_pressed',
                                                               data=type(self).image_close_pressed_data)
            class_type.images = (
                class_type.tab_close_image,
                class_type.tab_close_active_image,
                class_type.tab_close_pressed_image
            )

        # Create the close button element
        style.element_create(
            'close', 'image', 'image_close',
            ('active', 'pressed', '!disabled', 'image_close_pressed'),
            ('active', '!disabled', 'image_close_active'),
            border=8, sticky=''
        )

        # Configure notebook style
        style.layout('FocusNotebook', [('FocusNotebook.client', {'sticky': 'nswe'})])

        # Configure tab style
        style.layout('FocusNotebook.Tab', [
            ('FocusNotebook.tab', {
                'sticky': 'nswe',
                'children': [
                    ('FocusNotebook.padding', {
                        'side': 'top',
                        'sticky': 'nswe',
                        'children': [
                            ('FocusNotebook.focus', {
                                'side': 'top',
                                'sticky': 'nswe',
                                'children': [
                                    ('FocusNotebook.label', {'side': 'left', 'sticky': 'w'}),
                                    ('FocusNotebook.close', {'side': 'right', 'sticky': 'e'})
                                ]
                            })
                        ]
                    })
                ]
            })
        ])

        # Copy existing tab settings from the current theme
        settings = {}
        for key in ('background', 'lightcolor', 'bordercolor', 'darkcolor'):
            for state in ('selected', '!selected'):
                value = style.lookup('TNotebook.Tab', key, [state])
                if value:
                    settings.setdefault(key, []).append((state, value))

        # Apply valid settings to our custom style. Background colours for
        # selected and !selected colours are reversed because I didn't like it
        # the way the default worked. Selected used the background of the
        # underlying frame, and it looks better different to the frame.
        if settings:
            for key, setting in settings.items():
                # We have a list of tuples.
                new_settings = []
                for index, tup in enumerate(setting):
                    state, value = tup
                    if state == '!selected':
                        state = 'selected'
                    elif state == 'selected':
                        state = '!selected'
                    new_settings.append((state, value))
                settings[key] = new_settings
            style.map('FocusNotebook.Tab', **settings)

        # Configure basic tab appearance ................. (L, T, R, B)
        style.configure('FocusNotebook.Tab', padding=(6, 2, 0, 0))

    def on_close_press(self, event):
        """Called when the mouse button is pressed over the close button"""

        element = self.identify(event.x, event.y)
        if 'close' in element:
            index = self.index('@%d,%d' % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return 'break'
        return event

    def on_close_release(self, event):
        """Called when the mouse button is released"""
        if not self.instate(['pressed']):
            return event

        element = self.identify(event.x, event.y)
        if 'close' not in element:
            # The user moved the mouse off the close button
            self.state(['!pressed'])
            self._active = None
            return event

        index = self.index('@%d,%d' % (event.x, event.y))

        if self._active == index:
            self.forget(index)
            self.event_generate('<<NotebookTabClosed>>')
        if self.index('end') == 0:
            self._create_empty_tab()

        self.state(['!pressed'])
        self._active = None
        return 'break'

    def get_active_editor(self) -> SimpleEditor:
        """Return the currently selected editor in the Notebook"""
        return self.nametowidget(self.select())

    def on_focus_in(self, _):
        """Restore the focus to the edit window when it receives focus."""
        self.get_active_editor().textbox.focus_set()

    def add(self, child: SimpleEditor, **kwargs):
        text = kwargs.pop('text', None)
        if text is None:
            text = self.NEW_TAB_HEADING
        child.set_font_size(self.default_font_size)
        super().add(child, text=text + self.PADDING_SPACES)
        num_tabs = self.index('end')  # get the new tab count, to select the new tab.
        self.select(num_tabs - 1)

    def insert(self, pos, child: SimpleEditor, **kwargs):
        text = kwargs.pop('text', None)
        if text is None:
            text = self.NEW_TAB_HEADING + self.PADDING_SPACES
        child.set_font_size(self.default_font_size)
        super().insert(pos, child, text=text, **kwargs)

    def set_font_size(self, size: int = 0):
        """Set the size of the text in the notebook tabs, and in each editor"""

        style = ttk.Style()
        if size != 0:
            large_font = tk.font.Font(font=self.default_font)
            large_font.configure(size=size)
            style.configure('FocusNotebook.Tab', font=large_font)
            self.default_font_size = size
        else:
            # Resetting the font size to 0 will revert to the default font.
            style.configure('FocusNotebook.Tab', font=self.default_font)
            self.default_font_size = 0

        for tab in self.tabs():
            editor = self.nametowidget(tab)
            editor.set_font_size(size)

    def load(self, path: str, contents: str):
        # we'll create a new tab for the file.
        new_editor = SimpleEditor(self, file_path=path, comment_symbol='--',
                                  relief='sunken',
                                  run_function=self.callable)
        new_editor.grid(row=1, column=0, sticky='nsew')
        self.add(new_editor, text=new_editor.name)
        new_editor.set_text(contents)
        self.tab(new_editor, text=new_editor.name + self.PADDING_SPACES)

    def on_saved(self, path: str):
        """Notification that an editor's filename has changed."""
        editor = self.get_active_editor()
        editor.file_path = path
        self.tab(editor, text=editor.name + self.PADDING_SPACES)

        # Now make sure there's always a new tab
        new_tab_exists = any(self.nametowidget(tab).name == self.NEW_TAB_HEADING
                             for tab in self.tabs())
        if not new_tab_exists:
            new_editor = SimpleEditor(self, comment_symbol='--', relief='sunken', run_function=self.callable)
            new_editor.grid(row=1, column=0, sticky='nsew')
            self.insert(0, new_editor)

    def get_editor_file_details(self) -> tuple[str, str] | tuple[None, None]:
        """Return the name and file path of the currently selected editor."""
        selected_editor = self.get_active_editor()
        if selected_editor.name != self.NEW_TAB_HEADING:
            return selected_editor.name, selected_editor.file_path
        else:
            return None, None


class SimpleEditor(tk.Frame):
    """A tkinter Text widget with a scrollbar and line numbers."""

    def __init__(self, window, file_path='', comment_symbol='--', run_function=None, **kwargs):
        super().__init__(window, **kwargs)

        self._file_path: str
        self.name: str
        self.file_path = file_path

        self.comment_symbol = comment_symbol

        self.callable = run_function

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=100)
        self.columnconfigure(2, weight=0)

        self.textbox = BryonOakleyText(self, wrap='word')
        self.line_numbers = LineNumbers(self, width=30)
        self.line_numbers.attach(self.textbox)

        self.vertical_scrollbar = ttk.Scrollbar(self,
                                                orient='vertical',
                                                command=self.textbox.yview)

        self.default_font = font.Font(font=self.textbox['font'])
        self.large_font = font.Font(font=self.default_font)
        self.default_font.configure(family='Arial')
        self.large_font.configure(family='Arial')
        self.set_font_size(0)

        self.textbox.bind('<Control-slash>', self.apply_commenting)
        self.textbox.bind('<Control-Key-a>', self.select_all)
        self.textbox.bind('<Control-Key-v>', self.paste)  # Delete selection before pasting.
        self.textbox.bind('<Tab>', self.on_tab)
        self.textbox.bind('<Control-Return>', self.insert_new_lines)
        if run_function is not None:
            self.textbox.bind('<Control-Key-r>', self.run_callable)

    def run_callable(self, _):
        self.callable()
        return 'break'

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path
        if path:
            self.name = os.path.basename(os.path.normpath(path))
        else:
            self.name = 'New tab'

    def on_tab(self, _):
        self.textbox.insert('insert', '    ')
        return 'break'  # Stop the default Tab action.

    def insert_new_lines(self, _):
        # Move to the start of the current line.
        self.textbox.mark_set('insert', 'insert linestart')
        self.textbox.insert('insert', '\n\n')
        # Now put the cursor back.
        self.textbox.mark_set('insert', 'insert-2c')
        return 'break'

    def select_all(self, _):
        self.textbox.tag_add('sel', '1.0', 'end')
        return 'break'  # Stop the default Ctrl-a action.

    def paste(self, _):
        """Clear the current selection (if any),
        then fall through to the default paste operation.
        """
        selection = self.textbox.tag_ranges('sel')
        if selection:
            self.textbox.delete(*selection)

    def apply_commenting(self, _) -> str:
        """Comment out a selection with self.comment_symbol (which can be several
           characters such as '--' or '/*') or remove commenting from an already
           commented out section.

        Uses Ctrl-/ (the same keystroke as IntelliJ IDEA and PyCharm).
        """
        cursor_pos = self.textbox.index('insert')
        selection = self.textbox.tag_ranges('sel')

        if selection == ():
            start = f'{cursor_pos} linestart'
            end = f'{cursor_pos} lineend'

            self.textbox.tag_add('sel', start, end)
            selection = self.textbox.tag_ranges('sel')
        else:
            # make sure the selection is at the start of the line.
            start = f'{selection[0]} linestart'
            self.textbox.tag_add('sel', start, selection[1])
            self.textbox.tag_ranges('sel')
            selection = self.textbox.tag_ranges('sel')

        if selection:
            contents = self.textbox.selection_get()
            if contents.startswith(self.comment_symbol):
                self.textbox.replace(*selection, contents.replace(self.comment_symbol, ''))
            else:
                self.textbox.replace(*selection, contents.replace('\n', '\n--'))
                # insert comment at start of current line.
                self.textbox.insert(selection[0], self.comment_symbol)
        else:
            # we must be on a blank line
            self.textbox.insert(cursor_pos, self.comment_symbol)
        return 'break'

    def grid(self, row, column, sticky='nsew', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row,
                     column=column,
                     sticky=sticky,
                     rowspan=rowspan,
                     columnspan=columnspan,
                     **kwargs)
        self.line_numbers.grid(row=0, column=0, sticky='ns')
        self.textbox.grid(row=0, column=1, sticky='nsew')

        self.vertical_scrollbar.grid(row=0,
                                     column=2,
                                     sticky='nse')

        self.textbox['yscrollcommand'] = self.vertical_scrollbar.set

    def set_font_size(self, size: int = 0):
        if size != 0:
            self.large_font.configure(size=size)
            self.textbox.configure(font=self.large_font)
            self.line_numbers.set_font()
        else:
            self.textbox.configure(font=self.default_font)
            self.line_numbers.set_font()

    def set_text(self, text):
        self.textbox.delete('1.0', 'end')
        self.textbox.insert('1.0', text)
        # Now move to the top of the file.
        self.textbox.mark_set('insert', '1.0')
        self.textbox.see('1.0')

    def get_text(self):
        return self.textbox.get('1.0', 'end-1c')


class RefocusButton(ttk.Button):
    """Button that restores the focus to another window after being clicked."""

    def __init__(self, window, focus_window: tk.Widget, **kwargs):
        self.callable = kwargs.pop('command', None)
        self.focus_window: tk.Widget = focus_window
        super().__init__(window, **kwargs)
        self.bind('<ButtonRelease-1>', self.on_click)

    def on_click(self, _):
        self.callable()
        self.after_idle(self.focus_window.focus_set)  # False warning from IntelliJ IDEA.


class FrameTree(ttk.Frame):
    """A TreeView embedded in its own Frame, with methods to add objects."""

    def __init__(self, window, title='', **kwargs):
        self.title = title
        super().__init__(window, **kwargs)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        show = ['tree']
        if self.title:
            show.append('headings')
        self.tree = ttk.Treeview(self, show=show, selectmode='browse')

        # Give this Treeview its own style
        style = ttk.Style()
        self.treeview_font = tk.font.Font(font=tk.font.nametofont('TkTextFont'))
        self.original_size = self.treeview_font['size']
        self.headings_font = tk.font.Font(font=tk.font.nametofont('TkHeadingFont'))
        font_height = self.treeview_font.metrics()['linespace']
        style.configure('FrameTree.Treeview', font=self.treeview_font, rowheight=font_height + 2)
        style.configure('FrameTree.Treeview.Heading', font=self.headings_font)
        self.tree.configure(style='FrameTree.Treeview')

        self.open_database_font = tk.font.Font(font=tk.font.nametofont('TkTextFont'))
        self.open_database_font.configure(weight='bold')

        # Attributes for highlighting a "special" top-level item – the tagged item.
        self.tagged_font = tk.font.Font(font=self.treeview_font)
        self.tagged_font.configure(weight='bold')
        self.tagged_item = None

    def grid(self, row, column, rowspan=1, columnspan=1, sticky='nsew', **kwargs):
        super().grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                     sticky=sticky, **kwargs)
        self.tree.grid(row=0, column=0, sticky='nsew', **kwargs)

        self.tree.column('#0', stretch=tk.YES)
        if self.title:
            self.tree.heading('#0', text=self.title, anchor='w')

    def set_font_size(self, size: int = 0):
        style = ttk.Style()
        if self.treeview_font['size'] != self.original_size or size == 0:
            # Reset the size.
            self.treeview_font.configure(size=self.original_size, weight='normal')
            self.headings_font.configure(size=self.original_size)  # , weight='normal')
        else:
            self.treeview_font.configure(size=size)
            self.headings_font.configure(size=size)

        font_height = self.treeview_font.metrics()['linespace']
        style.configure('FrameTree.Treeview', rowheight=font_height + 2)
        # Remember to also configure any items that have been tagged.
        self.tagged_font.configure(size=self.treeview_font['size'])

    def tag_item(self, name: str):
        if self.tagged_item:
            self.tree.tag_configure(self.tagged_item, background='white', font=self.treeview_font)

        self.tree.tag_configure(name, background='yellow', font=self.tagged_font)
        self.tagged_item = name

    def insert(self, obj: Expandable | str, object_id=''):
        """Insert an object, and all its children, into the TreeView.

        Objects must either be strings (in which case they have no children)
        or they should implement the `Expandable` interface.
        """

        if object_id == '':
            # We have a top-level item (i.e., a database name rather than a column).
            # Tag it so that we can change its styling.
            tags = (str(obj))
        else:
            tags = ''

        obj_id = self.tree.insert(
            object_id,
            'end',
            text=str(obj),
            open=False,
            tags=tags
        )

        # Now recursively add the child objects.
        if isinstance(obj, Expandable):
            expansion = obj.expand()
            if expansion:
                for child in expansion:
                    self.insert(child, object_id=obj_id)

    def _find_node(self, node_name):
        for node in self.tree.get_children(''):
            tags = self.tree.item(node).get('tags', None)
            if tags is not None and node_name in tags:
                return node
        return None

    def reload_structure(self, name, obj: Expandable):
        node = self._find_node(name)
        if node is not None:
            self.tree.delete(*self.tree.get_children(node))
            for child in obj.expand():
                self.insert(child, node)

    def get_parent_object(self):
        """Return the name of the selected top-level item, or None if nothing selected."""
        selected = self.tree.selection()
        if selected:
            current = selected[0]
            # Now find the top-level object associated with this item.
            while self.tree.parent(current) != '':
                current = self.tree.parent(current)

            db_name = self.tree.item(current, 'text')
            return db_name
        else:
            return None


class TableView(ttk.Frame):
    """A ttk Frame containing a Treeview that behaves like a table to display rows and columns."""

    def __init__(self, window, title='', large_font_size=24, **kwargs):

        self.title = title
        self.large_font_size = large_font_size
        super().__init__(window, **kwargs)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=0)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)

        show = ['headings']
        self.table = ttk.Treeview(self, show=show)

        self.vertical_scrollbar = ttk.Scrollbar(self,
                                                orient='vertical',
                                                command=self.table.yview)
        self.horizontal_scrollbar = ttk.Scrollbar(self,
                                                  orient='horizontal',
                                                  command=self.table.xview)

        self.table['yscrollcommand'] = self.vertical_scrollbar.set
        self.table['xscrollcommand'] = self.horizontal_scrollbar.set

        self.default_headings_font = font.Font(font=font.nametofont('TkHeadingFont'))
        self.default_text_font = font.nametofont('TkTextFont')
        self.large_headings_font = font.Font(font=font.nametofont('TkHeadingFont'))
        self.large_headings_font.configure(size=self.large_font_size)
        self.large_text_font = font.Font(font=font.nametofont('TkTextFont'))
        self.large_text_font.configure(size=self.large_font_size)

        # Font will be toggled back to default in the grid method.
        self.current_text_font = self.large_text_font
        self.current_headings_font = self.large_headings_font

        self.table.bind('<Control-c>', self.copy_contents)
        self.table.bind('<Control-Insert>', self.copy_contents)
        self.table.bind('<Button-3>', self.on_right_click)

    def grid(self, row, column, rowspan=1, columnspan=1, sticky='nsew', **kwargs):
        super().grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan,
                     sticky=sticky, **kwargs)

        self.table.grid(row=row, column=column, sticky='nsew', **kwargs)

        self.table.column('#0', stretch=tk.YES)
        if self.title:
            self.table.heading('#0', text=self.title, anchor='w')

        self.vertical_scrollbar.grid(row=0, column=1, sticky='nse')
        self.horizontal_scrollbar.grid(row=1, column=0, sticky='new')

        self.toggle_font_size()  # Make sure the Treeview font size is reset.

    def on_right_click(self, _):
        """A right-click toggles the font size between large and default."""
        self.toggle_font_size()

    def copy_contents(self, _):
        """Copy the selected rows (including headings) in the Treeview to the clipboard."""
        self.clipboard_clear()

        # copy headers (but slice out the first item).
        headings = [self.table.heading("#{}".format(i), "text") for i in range(len(self.table.cget("columns")) + 1)]
        self.clipboard_append("\t".join(headings[1:]) + "\n")

        selection = self.table.selection()
        for row in selection:
            # retrieve the values of the row
            values = (self.table.item(row, 'values'))
            # append the values separated by \t to the clipboard
            self.clipboard_append("\t".join(values) + "\n")

    def clear(self):
        """ Delete all existing items."""
        self.table.delete(*self.table.get_children())

    def display_rows(self, headings, rows):
        """Display rows of data in columns of a TreeView.

        Assumes each row contains the same number of items.

        :param headings: A sequence containing the column names to be displayed.
        :param rows: A sequence of sequences, such as an SQLite cursor or a list of lists.
        :return: Nothing useful (i.e., None).
        """

        self.clear()
        self.table.see('')

        self.table.config(columns=headings, displaycolumns='#all')

        for column_number, column_heading in enumerate(headings):
            self.table.heading(column=column_number, text=column_heading, anchor='w')

        if rows:
            for row_number, values in enumerate(rows):
                # strip newlines (and multiple leading spaces at line start) from values.
                values = [' '.join(value.split()) if isinstance(value, str) else value for value in values]
                self.table.insert('', 'end', text=f'{row_number}', values=values)

        self.set_column_widths()

    def _calculate_text_width(self, text: str) -> int:
        result = self.current_headings_font.measure(text=text)
        return result + 16  # 16 is an arbitrary value to give extra padding on the right.

    def set_column_widths(self):
        if len(self) == 0:
            return  # Nothing to do.
        widths = {}  # Store the text length to avoid calling measure() multiple times.

        for column_number, column_text in enumerate(self.table['columns']):
            widths[column_number] = len(column_text)
            self.table.column(column_number, width=self._calculate_text_width(column_text), stretch=False)
        for row in self.table.get_children():
            for column_number, column_text in enumerate(self.table.item(row, 'values')):
                current_width = len(column_text)
                if widths.get(column_number, 0) < current_width:
                    widths[column_number] = current_width
                    self.table.column(column_number, width=self._calculate_text_width(column_text),
                                      stretch=False)

    def set_font_size(self, size: int = 0):
        """Set the font size. 0 resets to the default size."""
        if size == 0:
            # set to the font we *don't* want, it will be toggled.
            self.current_text_font = self.large_text_font
            self.current_headings_font = self.large_headings_font
        else:
            # We'll toggle to the large font.
            if size != self.large_font_size:
                self.large_font_size = size
                self.large_text_font.configure(size=self.large_font_size)
                self.large_headings_font.configure(size=self.large_font_size)
            self.current_text_font = self.default_text_font
            self.current_headings_font = self.default_headings_font

        self.toggle_font_size()

    def toggle_font_size(self):
        """Set the font size of the Treeview and headings."""
        style = ttk.Style()
        if self.current_text_font is self.default_text_font:
            self.current_text_font = self.large_text_font
            self.current_headings_font = self.large_headings_font
        else:
            self.current_text_font = self.default_text_font
            self.current_headings_font = self.default_headings_font
        font_height = self.current_text_font.metrics()['linespace']
        style.configure('Treeview', rowheight=font_height + 2,
                        font=self.current_text_font)
        style.configure('Treeview.Heading', font=self.current_headings_font)

        self.set_column_widths()

    def __len__(self):
        return len(self.table.get_children())


class MessageEntry(ttk.Entry):
    """A tk Entry widget with methods to display messages and errors."""

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.default_font = self['font']
        self.large_font = font.Font(font=self.default_font)

    def set_font_size(self, size: int = 0):
        if size != 0:
            self.large_font.configure(size=size)
            self.configure(font=self.large_font)
        else:
            self.configure(font=self.default_font)

    def display_message(self, message: str):
        self.delete(0, 'end')
        self.configure(foreground='black')
        self.insert(0, message)

    def display_error(self, message: str):
        self.delete(0, 'end')
        self.configure(foreground='#a01813')
        self.insert(0, message)

    def clear_text(self):
        self.delete(0, 'end')


class LineNumbers(tk.Canvas):
    """A tk Canvas that displays line numbers when the attached Text changes.

    Based on a class created by Bryan Oakley responding to a stackOverflow post at
    https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
    """

    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs)
        self.text_widget = None
        self.font = None

    def attach(self, text_widget):
        self.text_widget = text_widget
        self.set_font()

        self.text_widget.bind("<<Change>>", self._on_change)
        self.text_widget.bind("<Configure>", self._on_change)

    def _on_change(self, _):
        self.redraw()

    def set_font(self):
        """Call after the text widget's font changes."""
        self.font = self.text_widget['font']
        font_object = font.nametofont(self.font)
        width = font_object.measure('999') + 8
        self.configure(width=width)

    def redraw(self, *_):
        """redraw line numbers"""
        self.delete("all")

        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None: break
            y = dline[1]
            line_num = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=line_num, font=self.font)
            i = self.text_widget.index("%s+1line" % i)


class BryonOakleyText(tk.Text):
    """A tk Text widget that can attached to a LineNumbers canvas.

    Created by Bryan Oakley responding to a stackOverflow post at
    https://stackoverflow.com/questions/16369470/tkinter-adding-line-number-to-text-widget
    """

    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)

    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        try:
            result = self.tk.call(cmd)
        except tk.TclError:
            # Maybe that command shouldn't be called here.
            return 'break'
        else:
            # generate an event if something was added or deleted,
            # or the cursor position changed
            if (args[0] in ("insert", "replace", "delete") or
                    args[0:3] == ("mark", "set", "insert") or
                    args[0:2] == ("xview", "moveto") or
                    args[0:2] == ("xview", "scroll") or
                    args[0:2] == ("yview", "moveto") or
                    args[0:2] == ("yview", "scroll")
            ):
                self.event_generate("<<Change>>", when="tail")

            # return what the actual widget returned
            return result

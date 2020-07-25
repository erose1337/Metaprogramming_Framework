import pride.components.database
import pride.gui.widgets.formext
import pride.functions.contextmanagers
from pride.gui.widgets.form import field_info
from pride.functions.utilities import slide

# Db_Viewer takes a Database as a target
#   Db_Viewer introspects table names and creates tabs based on them
# Each table_name tab opens a Table, which takes a Database and table name
#   Table introspects the tables values and creates Db_Entry objects for each entry
# Db_Entry takes a database, table_name, and value, and translates attribute access to SQL queries

def determine_primary_key(db, table_name):
    table_info = list(db.table_info(table_name))
    for _, name, _type, _, _, _ in table_info:
        try:
            _type, _type_info = _type.split(' ', 1)
        except ValueError:
            if ' ' in _type:
                raise
            _type_info = ''

        if "PRIMARY_KEY" in _type_info:
            return name
    else:
        raise ValueError("No PRIMARY_KEY in table {}".format(table_name))


class Db_Entry(pride.gui.widgets.formext.Data):

    defaults = {"table_name" : '', "entry_id" : '', "primary_key" : '',
                "column_names" : tuple(), "field_index" : 0}
    autoreferences = ("db", )

    def __getitem__(self, name):
        value = self.db.query(self.table_name,
                              where={self.primary_key : self.entry_id},
                              retrieve_fields=(name, ))
        return value

    def __setattr__(self, name, value):
        try:
            is_db_value = name in self.column_names
        except AttributeError:
            super(Db_Entry, self).__setattr__(name, value)
        else:
            if is_db_value:
                self[name] = value
            else:
                super(Db_Entry, self).__setattr__(name, value)

    def __setitem__(self, name, value):
        entry_id = self.entry_id
        try:
            self.db.update_table(self.table_name,
                                 where={self.primary_key : entry_id},
                                 arguments={name : value})
        except OverflowError as error:
            form = pride.objects[self.parent.form_reference]
            form.show_status(error.message)
        else:
            if name == self.primary_key: # need to update field.name
                self.entry_id = value


class Table(pride.gui.widgets.formext.Data):

    defaults = {"table_name" : '', "read_only" : False, "items_per_row" : 6}
    autoreferences = ("db", )

    def __init__(self, **kwargs):
        super(Table, self).__init__(**kwargs)
        db = self.db
        table_name = self.table_name
        primary_key = determine_primary_key(db, table_name)
        names = [item[1] for item in db.table_info(table_name)]
        with pride.functions.contextmanagers.backup(db, "return_cursor"):
            # if len(query) == 1 and db.return_cursor == False,
            # then database.py extracts the single item in the list automatically
            db.return_cursor = True
            values = list(db.query(table_name))

        fields = self.fields = []
        row_kwargs = dict()
        try:
            row_kwargs.update(self.row_kwargs)
        except AttributeError:
            pass
        row_count = len(fields)
        editable = not self.read_only
        items_per_row = self.items_per_row
        for index, value in enumerate(values):
            entry_id = value[0]
            try:
                row_kwargs[row_count].setdefault("h_range", (0, .05))
            except KeyError:
                row_kwargs[row_count] = {"h_range" : (0, .05)}
            db_entry = self.create(Db_Entry, db=db, table_name=table_name,
                                   entry_id=value[0], primary_key=primary_key,
                                   column_names=set(names), field_index=index)
            fields.append([field_info("select_entry", args=(entry_id, ),
                                      button_text=entry_id,
                                      entry_kwargs={"scale_to_text" : False})])
            row_count += 1
            for _names in slide(names, items_per_row):
                row = [field_info(name, target_object=db_entry,
                                editable=editable) for name in _names
                       if name != primary_key]
                fields.append(row)
                row_count += 1
        self.row_kwargs = row_kwargs

    def delete(self):
        del self.fields
        super(Table, self).delete()

    def select_entry(self, name):
        message = "Selected: {}".format(name)
        self.alert(message)
        pride.objects[self.form_reference].show_status(message)


class Database_Data(pride.gui.widgets.formext.Data):

    defaults = {"read_only" : False}
    autoreferences = ("db", )

    def setup_tabs(self):
        db = self.db
        tabs = self.tabs = dict()
        read_only = self.read_only
        for table_name in sorted(db.db_info().keys()):
            def callable(db=db, table_name=table_name, read_only=read_only):
                return Table(db=db, table_name=table_name, read_only=read_only)
            tabs[table_name] = callable
        super(Database_Data, self).setup_tabs()


#class Db_Viewer(pride.gui.gui.Window):
#
#    autoreferences = ("db", )
#
#    def __init__(self, **kwargs):
#        super(Db_Viewer, self).__init__(**kwargs)
#        self.create_data_and_form()
#
#    def create_data_and_form(self):
#        data = Database_Data(db=self.db)
#        form = pride.gui.widgets.formext.Tabbed_Form
#        self.create(form, target_object=data)

class Db_Viewer(pride.gui.widgets.formext.Tabbed_Form):

    defaults = {"read_only" : False}
    autoreferences = ("db", )

    def create_subcomponents(self):
        self.target_object = Database_Data(db=self.db, read_only=self.read_only)
        super(Db_Viewer, self).create_subcomponents()

    def synchronize_fields(self):
        super(Db_Viewer, self).synchronize_fields()
        # check for new Tables and Entries



class Test_Db_Viewer_Db(pride.components.database.Database):

    defaults = {"return_cursor" : False}
    schema = {"table1" : ("entry_name INTEGER PRIMARY_KEY UNIQUE",
                          "entry_data BLOB", "entry_num INTEGER"),
              "table2" : ("entry_name TEXT PRIMARY_KEY UNIQUE",
                          "entry_data BLOB", "entry_num INTEGER")}

def test_Database_Data():
    import sqlite3
    import pride.gui.main as gui
    db = Test_Db_Viewer_Db()

    output = db.query("table1")
    if not output:
        db.insert_into("table1", (0, "data goes here", 0))
    output = db.query("table2")
    if not output:
        db.insert_into("table2", ("test_entry", "data", 0))

    programs = (lambda **kwargs: Db_Viewer(db=db, **kwargs), )
    gui.run_programs(programs, position=(100, 100))

if __name__ == "__main__":
    test_Database_Data()

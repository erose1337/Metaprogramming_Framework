#- database viewer program
#    - select db file (File_Selector)
#    - use Database.db_info and table_info to display contents
import pride.components.database
import pride.gui.widgets.tabs
import pride.functions.persistence

class Table_Viewer(pride.gui.gui.Window):

    defaults = {"pack_mode" : "top"}

    def __init__(self, **kwargs):
        super(Table_Viewer, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        dbfields = [item[1] for item in self.schema]
        for dbfield in dbfields:
            setattr(self, "_field_name_{}".format(dbfield), dbfield)

        for item in self.database.query(self.table_name, retrieve_fields=dbfields):
            fields = [[("_field_name_{}".format(dbfield), {"editable" : False,
                                                           "auto_create_id" : False})] for
                        dbfield in dbfields]
            self.create("pride.gui.widgets.form.Form",
                        fields=fields, target_object=self, pack_mode="top")


class Database_Viewer(pride.gui.widgets.tabs.Tabbed_Window):

    defaults = {"new_window_type" : Table_Viewer}
    autoreferences = ("file_selector", "database")

    def create_subcomponents(self):
        assert self.file_selector is None
        assert not self.tab_targets
        self.file_selector = self.create("pride.gui.programs.fileexplorer.File_Selector",
                                         callback=self.load_database)

    def load_database(self, filename):
        db = self.database = pride.components.database.Database(database_name=filename)
        self.file_selector.delete()
        targets = self.tab_targets = []
        for table_name, schema in db.db_info().items():
            def callable(db=db, table_name=table_name, schema=schema, **kwargs):
                return self.create(Table_Viewer, database=db, table_name=table_name,
                                   schema=schema, **kwargs)
            callable.tab_text = table_name
            targets.append(callable)
        super(Database_Viewer, self).create_subcomponents()

def test_Database_Viewer():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable()]
    def callable(**kwargs):
        return Database_Viewer(**kwargs)

    window.create(pride.gui.main.Gui, startup_programs=(callable, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Database_Viewer()

import time
import os

import pride.gui.gui
import pride.gui.widgets.form
import pride.gui.widgets.tree

class Prompt(pride.gui.widgets.form.Form):

    defaults = {"prompt_text" : '',
                "fields" : [ [("prompt_text", {"editable" : False, "auto_create_id" : False,
                                               "scale_to_text" : True,
                                               "entry_kwargs" : {"theme_profile" : "default"}}),
                              ("handle_yes", {"orientation" : "stacked",
                                              "button_text" : "Yes"}),
                              ("handle_no", {"orientation" : "stacked",
                                             "button_text" : "No"})
                             ]
                           ],
                "pack_mode" : "top", "h_range" : (.25, .25),
                "include_delete_button" : True
                }

    def handle_yes(self):
        raise NotImplementedError()

    def handle_no(self):
        raise NotImplementedError()


class Overwrite_Prompt(Prompt):

    defaults = {"prompt_text" : "File already exists. Overwrite?",
                "theme_profile" : "alert"}

    def handle_yes(self):
        self.parent.save_data(overwrite=True)
        assert not self.deleted
        self.delete()

    def handle_no(self):
        assert not self.deleted
        self.delete()


class File_Saver(pride.gui.widgets.form.Form):

    defaults = {"filename" : '', "data" : '', "autodelete" : False,
                "fields" : (("filename", ("save_data", {"button_text" : "save"})), ),
                "h_range" : (0, .25), "include_delete_button" : True,
                "form_name" : "File saver"}
    autoreferences = ("prompt", )

    def save_data(self, overwrite=False):
        if (not overwrite) and os.path.exists(self.filename) and self.prompt is None:
            self.prompt = self.create(Overwrite_Prompt)

        if self.prompt is None or overwrite:
            size = len(self.data)
            units = ["bytes", "KB", "MB", "GB", "TB"]
            index = 0
            while size > 1024:
                index += 1
                size /= 1024.0
            self.show_status("Saving {0:.2f}{1} to {2}...".format(size, units[index], self.filename))
            try:
                with open(self.filename, "wb") as _file:
                    _file.write(self.data)
            except IOError:
                if os.path.exists(self.filename):
                    raise
                self.show_status("Unable to write to file {}; Ensure all directories exist and are spelled correctly and try again.".format(self.filename))
            else:
                if self.autodelete:
                    self.delete()


class Directory_Viewer(pride.gui.widgets.tree.Tree_Viewer):

    defaults = {"current_node" : '~/', "selected_file" : '',
                "node_label" : "Directory Explorer", "pack_mode" : "top"}

    @staticmethod
    def epoch_to_english(_time):
        return time.asctime(time.localtime(_time))

    @staticmethod
    def new_entry(child):
        alt = os.path.split(str(child))[-1]
        if os.path.isfile(child):
            name = "select_file"
        else:
            name = "view_node"
        return (name, {"button_text" : getattr(child, "text", alt),
                       "args" : (child, )})

    def convert_size_unit(self, size):
        units = ["bytes", "KB", "MB", "GB", "TB"]
        index = 0
        while size > 1024:
            index += 1
            size /= 1024.0
        # size < 1024 won't trigger loop and size would be an int
        # int has no `is_integer` method that select_file expects size to have
        return float(size), units[index]

    def select_file(self, identifier):
        self.selected_file = identifier
        extension = os.path.splitext(identifier)[-1]
        size, unit = self.convert_size_unit(os.path.getsize(identifier))
        if not size.is_integer():
            size = "{:.2f}".format(size)
        else:
            size = int(size)
        file_information = os.stat(identifier)
        created  = self.epoch_to_english(file_information.st_ctime)
        modified = self.epoch_to_english(file_information.st_mtime)
        str1 = "Selected file: {}  |  Type: {}  |  Size: {} {}\n".format(identifier, extension, size, unit)
        str2 = str1 + "Created: {}  |  Modified: {}".format(created, modified)
        self.show_status(str2)

    def lookup(self, identifier):
        if identifier == '~': # normalize because os.path.split('~') = ('', '~'); os.path.split("~/") = ('~', '/')
            identifier = "~/"
        identifier = identifier.strip()
        identifier = os.path.expanduser(identifier) # will change ~/ into home directory, or not do anything at all
        if not os.path.exists(identifier) and identifier[0]:
            raise ValueError("{} does not exist".format(identifier))
        if os.path.isdir(identifier):
            try:
                children = os.listdir(identifier)
            except OSError as error:
                if error.errno != 13:
                    raise
                else:
                    self.show_status("Unable to open '{}'; Access denied".format(identifier))
                    return None
            else:
                return sorted([os.path.join(identifier, child) for
                              child in children if max(set(bytearray(child))) < 128])
        else:
            assert os.path.isfile(identifier)
            self.select_file(identifier)
            return None

    def handle_up(self):
        node = self.current_node
        if node == "~/":
            node = '~'
        node = os.path.split(os.path.expanduser(node))[0]
        if self.current_node != node:
            self.current_node = node
            self.view_node()

    def view_node(self, identifier=None):
        if identifier is None and not os.path.exists(os.path.expanduser(self.current_node)):
            self.show_status("{} does not exist".format(self.current_node))
            return
        super(Directory_Viewer, self).view_node(identifier)



class File_Selector(Directory_Viewer):

    required_attributes = ("callback", )
    autoreferences = ("confirmation_box", )
    hotkeys = {('\n', None) : "handle_return"}

    def handle_return(self):
        self.view_node()

    def select_file(self, filename):
        self.filename = filename
        if self.confirmation_box is None:
            fields = [["filename", ("confirm_selection", {"button_text" : "Confirm"}),
                       ("delete_confirmation", {"button_text" : 'x'})
                     ]]
            box = self.application_window.create(pride.gui.widgets.form.Form,
                                                fields=fields, target_object=self)
            self.confirmation_box = box
        else:
            self.confirmation_box.synchronize_fields()

    def delete_confirmation(self):
        self.confirmation_box.delete()

    def confirm_selection(self):
        self.callback(self.filename)
        if not self.deleted:
            self.delete()


def directory_explorer_test():
    import pride.gui
    window = pride.objects[pride.gui.enable()]
    window.create("pride.gui.main.Gui", startup_programs=(Directory_Viewer, ),
                  user=pride.objects["/User"])

def file_saver_test():
    import pride.gui
    window = pride.objects[pride.gui.enable()]
    gui = window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                        startup_programs=(File_Saver, ))

if __name__ == "__main__":
    directory_explorer_test()
    file_saver_test()

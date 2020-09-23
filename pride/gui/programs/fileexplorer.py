import time
import os

import pride.gui.gui
import pride.gui.form
import pride.gui.widgets.tree
from pride.gui.form import field_info, row_info, layout
from pride.components import Component


class Prompt(pride.gui.form.Form):

    defaults = {"prompt_text" : '',
                "layout" :
                    layout(
                        row_info(0,
                            field_info("prompt_text", editable=False,
                                       auto_create_id=False,
                                    entry_kwargs={"theme_profile" : "default",
                                                  "scale_to_text" : True}),
                            field_info("handle_yes", orientation="stacked",
                                       button_text="Yes"),
                            field_info("handle_no", orientation="stacked",
                                       button_text="No"))),
                "location" : "top", "h_range" : (.25, .25),
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
        assert not self.deleted
        self.delete()
        self.parent.parent.save_data(overwrite=True)

    def handle_no(self):
        assert not self.deleted
        self.delete()


class _File_Saver(pride.gui.form.Form):

    defaults = {"layout" :
                    layout(
                        row_info(0,
                            field_info("filename"),
                            field_info("save_data", button_text="save"))),
                "h_range" : (0, .25), "include_delete_button" : True,
                "form_name" : "File saver"}


class Directory_Viewer(pride.gui.widgets.tree.Tree_Viewer):

    defaults = {"current_node" : '~/', "selected_file" : '',
                "node_label" : "Directory Explorer", "location" : "top"}

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

    defaults = {"callback" : None}
    autoreferences = ("confirmation_box", )
    hotkeys = {('\n', None) : "handle_return"}

    def handle_return(self):
        self.view_node()

    def select_file(self, filename):
        super(File_Selector, self).select_file(filename)
        self.filename = filename
        if self.confirmation_box is None:
            _layout = layout(
                        row_info(0,
                            field_info("filename"),
                        field_info("confirm_selection", button_text="Confirm"),
                        field_info("delete_confirmation", button_text='x')))
            box = self.main_window.create(pride.gui.form.Form,
                                          layout=_layout, target_object=self)
            self.confirmation_box = box
        else:
            self.confirmation_box.synchronize_fields()

    def delete_confirmation(self):
        self.confirmation_box.delete()

    def confirm_selection(self):
        if self.callback is not None:
            self.callback(self.filename)
        if not self.deleted:
            self.delete()


class File_Saver(pride.gui.form.Scrollable_Window):

    defaults = {"data" : bytes(), "filename" : '', "autodelete" : False,
                "location" : "top"}
    subcomponents = {"vertical_slider" : Component(location=None),
                     "horizontal_slider" : Component(location=None),
        "_file_saver" : Component("pride.gui.programs.fileexplorer._File_Saver",
                                  h_range=(0, .1)),
        "directory_viewer" :
                  Component("pride.gui.programs.fileexplorer.Directory_Viewer")}
    autoreferences = ("prompt", "file_saver", "directory_viewer")

    def create_subcomponents(self):
        super(File_Saver, self).create_subcomponents()
        window = self.main_window
        self.file_saver = window.create(self._file_saver_type, data=self.data,
                                        target_object=self,
                                        **self._file_saver_kwargs)
        self.directory_viewer = window.create(self.directory_viewer_type,
                                              **self.directory_viewer_kwargs)

    def save_data(self, overwrite=False):
        filename = os.path.join(self.directory_viewer.current_node,
                                self.filename)
        filename = os.path.expanduser(filename)
        already_exists = os.path.exists(filename)
        if already_exists and self.prompt is None:
            if overwrite == False:
                self.prompt = self.main_window.create(Overwrite_Prompt)
            #else:
            #    if self.prompt is not None and not self.prompt.deleted:
            #        self.prompt.delete()
            #        assert self.prompt is None
        if overwrite or not already_exists:
            size = len(self.data)
            units = ["bytes", "KB", "MB", "GB", "TB"]
            index = 0
            while size > 1024:
                index += 1
                size /= 1024.0
            self.show_status("Saving {0:.2f}{1} to {2}...".format(size, units[index], filename))
            try:
                with open(filename, "wb") as _file:
                    _file.write(self.data)
            except IOError:
                if os.path.exists(filename):
                    raise
                self.show_status("Unable to write to file {}; Ensure all directories exist and are spelled correctly and try again.".format(filename))
            else:
                if self.autodelete:
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
    #directory_explorer_test()
    file_saver_test()

import time
import os

import pride.gui.gui
import pride.gui.widgets.form


class File_Info(pride.gui.widgets.form.Form):

    name = ("name", {"auto_create_id" : False})
    _type = ("type", {"editable" : False, "auto_create_id" : False})
    filesize = ("filesize", {"editable" : False, "auto_create_id" : False})
    created = ("created", {"editable" : False, "auto_create_id" : False})
    modified = ("created", {"editable" : False, "auto_create_id" : False})
    defaults = {"fields" : [[name, _type, filesize, created, modified]],
                "name" : '', "type" : '', "filesize" : 0, "created" : '',
                "modified" : '', "pack_mode" : "top"}
    del name, _type, filesize, created, modified


class File_Explorer(pride.gui.gui.Window):

    defaults = {"path" : os.curdir}
    mutable_defaults = {"contents" : list}

    def __init__(self, **kwargs):
        super(File_Explorer, self).__init__(**kwargs)
        self.view_directory(self.path)

    def view_directory(self, directory):
        contents = self.contents
        for child in contents:
            child.delete()
        del contents[:]
        directories = []
        for filename in os.listdir(directory):
            full_name = os.path.join(directory, filename)
            file_type = os.path.splitext(filename)[-1] or filename
            epoch_to_english = lambda _time: time.asctime(time.localtime(_time))
            if os.path.isfile(full_name):
                file_information = os.stat(full_name)
                _entry = self.create(File_Info, name=full_name, type=file_type,
                            filesize=os.path.getsize(full_name),
                            created=epoch_to_english(file_information.st_ctime),
                            modified=epoch_to_english(file_information.st_mtime))
                contents.append(_entry)
            else:
                directories.append(full_name)
        for full_name in directories:
            _entry = self.create(pride.gui.widgetlibrary.Method_Button, target=self.reference,
                                 method="view_directory", args=(full_name, ),
                                 text=full_name, scale_to_text=False)
            contents.append(_entry)


class Prompt(pride.gui.widgets.form.Form):

    defaults = {"prompt_text" : '',
                "fields" : [ [("prompt_text", {"editable" : False}),
                              ("handle_yes", {"orientation" : "stacked",
                                              "button_text" : "Yes"}),
                              ("handle_no", {"orientation" : "stacked",
                                             "button_text" : "No"})
                             ]
                           ],
                "pack_mode" : "fill"
                }

    def handle_yes(self):
        raise NotImplementedError()

    def handle_no(self):
        raise NotImplementedError()


class Overwrite_Prompt(Prompt):

    defaults = {"prompt_text" : "File already exists. Overwrite?"}

    def handle_yes(self):
        self.parent_application.save_as(overwrite=True)
        assert self.deleted

    def handle_no(self):
        self.delete()


class File_Saver(pride.gui.gui.Application):

    defaults = {"filename" : '', "data" : '', "create_tip_bar" : False}
    autoreferences = ("address_bar", "prompt")

    def __init__(self, **kwargs):
        super(File_Saver, self).__init__(**kwargs)
        window = self.application_window
        top = window.create("pride.gui.gui.Container", pack_mode="top",
                            h_range=(0, .25))
        self.address_bar = top.create(pride.gui.widgets.form.Form,
                                      target_object=self, fields=[["filename"]],
                                      pack_mode="left")
        top.create("pride.gui.widgetlibrary.Method_Button", target=self.reference,
                   method="save_as", pack_mode="left", text="save")

    def save_as(self, overwrite=False):
        # make warning if saving over existing file?
        #size = len(self.data)
        #units = ["bytes", "KB", "MB", "GB", "TB"]
        #index = 0
        #while size / 1024.0 > 1024:
        #    index += 1
        #    size /= 1024.0
        #sizestr = "{} {}".format(size, units[index])
        #self.show_status("Saving {} to {}...".format(sizestr, self.filename))
        if os.path.exists(self.filename) and self.prompt is None:
            self.prompt = self.application_window.create(Overwrite_Prompt)

        if self.prompt is None or overwrite:
            with open(self.filename, "wb") as _file:
                _file.write(self.data)
            self.delete()

def test():
    import pride.gui
    window = pride.objects[pride.gui.enable()]
    gui = window.create("pride.gui.main.Gui", user=pride.objects["/User"],
                        startup_programs=(File_Saver, ))

if __name__ == "__main__":
    test()

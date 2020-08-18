import os

import pride.gui.gui
import pride.gui.widgets.tabs


class Listing(pride.gui.gui.Container):

    defaults = {"location" : "right"}


class Pinned_Listing(Listing): pass


class Settings_Listing(Listing): pass


class Places_Listing(Listing): pass


class Theme_Customizer_Button(pride.gui.gui.Button):

    defaults = {"program_type" : "pride.gui.programs.themecustomizer.Theme_Customizer",
                "text" : "Theme Customizer", "h_range" : (.025, .1)}

    def left_click(self, mouse):
        self.parent.parent.parent.parent.launch_program(self.program_type,
                                                        target_theme=self.theme)


class File_Explorer_Button(pride.gui.gui.Button):

    defaults = {"program_type" : "pride.gui.programs.fileexplorer.Directory_Viewer",
                "text" : "File Explorer", "h_range" : (.025, .1)}

    def left_click(self, mouse):
        self.parent.parent.parent.parent.launch_program(self.program_type)


class Programs_Listing(Listing):

    def __init__(self, **kwargs):
        super(Programs_Listing, self).__init__(**kwargs)
        self.create(Theme_Customizer_Button)
        self.create(Pride_Shell_Button)
        self.create(File_Explorer_Button)


class Pride_Shell_Button(pride.gui.gui.Button):

    defaults = {"text" : "pride shell", "h_range" : (.025, .1)}

    def left_click(self, mouse):
        self.parent.launcher_window.launch_program("pride.gui.shell.Python_Shell")


class OS_Program_Button(pride.gui.gui.Button):

    defaults = {"program" : "pride.gui.programs.Program_Button: program unspecified",
                "location" : "left", "scale_to_text" : True}

    def left_click(self, mouse):
        os.system(self.program)


class Power_Button(OS_Program_Button):

    defaults = {"program" : "shutdown", "text" : "Shutdown",
                "tip_bar_text" : "Shuts the computer down"}


class Restart_Button(OS_Program_Button):

    defaults = {"program" : "shutdown -r", "text" : "Restart",
                "tip_bar_text" : "Shuts the computer down and automatically restarts it"}


class Sleep_Button(OS_Program_Button):

    defaults = {"program" : "echo sleep not implemented yet", "text" : "Sleep",
                "tip_bar_text" : "(Not Implemented Yet) Puts the computer to sleep"}


#class Logout_Button(Program_Button):




class Content_Launcher(pride.gui.gui.Window):

    autoreferences = ("program", )

    def __init__(self, **kwargs):
        super(Content_Launcher, self).__init__(**kwargs)
        # programs  |   places  |    settings |    pinned
        #           |           |             |
        #           |           |             |
        #--power/restart/sleep/logout---------------------
        self.launcher_screen = launcher_screen = self.create("pride.gui.gui.Container")
        top = launcher_screen.create("pride.gui.gui.Container", location="top")
        bottom = launcher_screen.create("pride.gui.gui.Container", h_range=(.025, .05),
                             location="top")
        programs_column = top.create(Programs_Listing, launcher_window=self)
        places_column = top.create(Places_Listing, launcher_window=self)
        settings_column = top.create(Settings_Listing, launcher_window=self)
        pinned_column = top.create(Pinned_Listing)

        bottom.create(Power_Button)
        bottom.create(Restart_Button)
        bottom.create(Sleep_Button)
        #bottom.create(Log_Out_Button)

    def launch_program(self, program_type, **program_kwargs):
        self.launcher_screen.hide()
        self.program = self.create(program_type, **program_kwargs)
        self.tab.text = self.program.__class__.__name__

    def end_program(self):
        assert not self.program.deleted
        self.program.delete()
        self.program = None


class _Homescreen(pride.gui.widgets.tabs.Tabbed_Window):

    defaults = {"window_type" : Content_Launcher}



class Homescreen(pride.gui.gui.Application):

    def __init__(self, **kwargs):
        super(Homescreen, self).__init__(**kwargs)
        self.application_window.create(_Homescreen)


def test_Homecreen():
    import pride.gui.main
    window = pride.objects[pride.gui.enable(position=(100, 100))]
    window.create(pride.gui.main.Gui, startup_programs=(Homescreen, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Homecreen()

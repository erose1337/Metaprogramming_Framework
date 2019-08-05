import pride.gui.gui
import pride.gui.widgets.tabs

class _Homescreen(pride.gui.widgets.tabs.Tabbed_Window): pass


class Homescreen(pride.gui.gui.Application):

    def __init__(self, **kwargs):
        super(Homescreen, self).__init__(**kwargs)
        self.application_window.create(_Homescreen)


def test_Homecreen():
    import pride.gui.main
    window = pride.objects[pride.gui.enable()]
    window.create(pride.gui.main.Gui, startup_programs=(Homescreen, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Homecreen()

import pride.gui.gui

class Cell(pride.gui.gui.Container):

    defaults = {"location" : "left"}


class Identicon_Dark(pride.gui.gui.Window):

    defaults = {"location" : "top"}

    def __init__(self, **kwargs):
        super(Identicon_Dark, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        container = "pride.gui.gui.Container"
        create = self.create
        create(container, location="top", h_range=(0, .05), theme_profile="borderless")
        create(container, location="left", w_range=(0, .05), theme_profile="borderless")
        create(container, location="right", w_range=(0, .05), theme_profile="borderless")
        create(container, location="bottom", h_range=(0, .05), theme_profile="borderless")
        main = create(container, location="main", theme_profile="borderless")

        create = main.create; kwargs = {"location" : "top", "theme_profile" : "borderless"}
        row1 = create(container, **kwargs); row2 = create(container, **kwargs)
        row3 = create(container, **kwargs); row4 = create(container, **kwargs)
        row5 = create(container, **kwargs)
        create1 = row1.create; create2 = row2.create; create3 = row3.create; create4 = row4.create; create5 = row5.create
        inter = {"theme_profile" : "hover"}; bg = {"theme_profile" : "borderless"}
        create1(Cell, **inter); create1(Cell, **bg); create1(Cell, **inter); create1(Cell, **bg); create1(Cell, **inter)
        create2(Cell, **inter); create2(Cell, **inter); create2(Cell, **inter); create2(Cell, **inter); create2(Cell, **inter);
        create3(Cell, **inter); create3(Cell, **bg); create3(Cell, **bg); create3(Cell, **bg); create3(Cell, **inter)
        create4(Cell, **bg); create4(Cell, **bg); create4(Cell, **inter); create4(Cell, **bg); create4(Cell, **bg)
        create5(Cell, **bg); create5(Cell, **bg); create5(Cell, **inter); create5(Cell, **bg); create5(Cell, **bg)



def test():
    import pride.gui
    import pride.gui.main
    window = pride.objects[pride.gui.enable()]
    window.tip_bar.hide()
    window.create(pride.gui.main.Gui, startup_programs=(Identicon_Dark, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test()

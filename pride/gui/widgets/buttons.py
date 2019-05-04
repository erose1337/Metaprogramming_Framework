import pride.gui.gui

class Toggle(pride.gui.gui.Button):

    defaults = {"state" : False,
                "indicator_type" : "pride.gui.widgetlibrary.Status_Indicator"}
    autoreferences = ("indicator", )

    def __init__(self, **kwargs):
        super(Toggle, self).__init__(**kwargs)
        indicator = self.indicator = self.create(self.indicator_type)
        if self.state:
            indicator.enable_indicator()
        else:
            indicator.disable_indicator()

    def left_click(self, mouse):
        super(Toggle, self).left_click(mouse)
        self.state = not self.state
        if self.state:
            #self.theme_profile = "interactive"
            self.indicator.enable_indicator()
        else:
            #self.theme_profile = "placeholder"
            self.indicator.disable_indicator()

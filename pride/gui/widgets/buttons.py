import pride.gui.gui

class Proxy_Button(pride.gui.gui.Button):

    def left_click(self, mouse):
        super(Proxy_Button, self).left_click(mouse)
        self.parent.left_click(mouse)


class Toggle(pride.gui.gui.Button):

    defaults = {"state" : False, "pack_mode" : "left",
                "indicator_type" : "pride.gui.widgetlibrary.Status_Indicator",
                "label" : ''}
    autoreferences = ("indicator", )

    def __init__(self, **kwargs):
        super(Toggle, self).__init__(**kwargs)
        label = self.create("pride.gui.gui.Container", text=self.label, pack_mode="top",
                            scale_to_text=False, h_range=(0, .03),
                            theme_profile="default")
        button = self.create(Proxy_Button, pack_mode="left", tip_bar_text=self.tip_bar_text)
        indicator = self.indicator = self.create(self.indicator_type, w_range=(0, .03),
                                                 pack_mode="left")

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

    @classmethod
    def from_info(cls, **kwargs):
        return lambda: cls(**kwargs)

    def turn_off(self):
        self.state = False
        self.indicator.disable_indicator()


class Toggle_Bar(pride.gui.gui.Container):

    defaults = {"button_type" : Toggle, "toggle_count" : 0}

    def __init__(self, **kwargs):
        super(Toggle_Bar, self).__init__(**kwargs)
        self.initialize_buttons()

    def initialize_buttons(self):
        self.buttons = [self.create(self.button_type) for count in range(self.toggle_count)]

    def delete(self):
        self.buttons = None
        super(Toggle_Bar, self).delete()


class Mutexed_Button(Toggle):
    # if a Mutexed_Button is turned on, then other mutex buttons will be turned off

    def left_click(self, mouse):
        super(Mutexed_Button, self).left_click(mouse)
        if self.state:
            for button in self.parent.buttons:
                if button.state:
                    button.turn_off()


class Selection_Bar(Toggle_Bar):

    defaults = {"button_type" : Mutexed_Button}

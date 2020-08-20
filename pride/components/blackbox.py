""" Provides network services that do not reveal information about how
    application logic produces its result. Black_Box_Services receive input
    in the form of keystrokes, mouse clicks, and potentially audio,
    operate on the input in a manner opaque to the client, and return output
    to the client. """
import pride.components.authentication3
import pride.functions.utilities

class Event_Structure(object):

    def __init__(self, mouse):
        self.button = mouse


class Mouse_Structure(object):

    def __init__(self, x, y, clicks, button):
        self.x = x
        self.y = y
        self.clicks = clicks
        self.button = button

    def __str__(self):
        return "Mouse(x={}, y={}, clicks={}, button={})".format(self.x, self.y, self.clicks, self.button)


class Black_Box_Service(pride.components.authentication3.Authenticated_Service):

    defaults = {"input_types" : ("keyboard", "mouse", "audio"), "window_type" : "pride.gui.sdllibrary.Window_Context",
                "command_line" : "/User/Command_Line", "command_line_program" : "python"}
    remotely_available_procedures = ("handle_input", )
    verbosity = {"handle_keyboard" : "vvv", "handle_mouse" : "v", "handle_audio" : "vvv", "refresh" : 'v'}
    mutable_defaults = {"windows" : dict}

    def login_success(self, username):
        window = self.create(self.window_type)
        self.windows[username] = window.reference
        window.create("pride.gui.widgetlibrary.Homescreen")
        return super(Black_Box_Service, self).login_success(username)

    def handle_input(self, packed_user_input):
        input_type, input_values = packed_user_input.split(' ', 1)
        if input_type in self.input_types:
            return getattr(self, "handle_{}_input".format(input_type))(input_values)
        else:
            raise ValueError("Unaccepted input_type: {}".format(packed_user_input))

    def handle_keyboard_input(self, input_bytes):
        self.alert("Received keystrokes: {}".format(input_bytes),
                   level=self.verbosity["handle_keyboard"])
        component, method = pride.objects[self.command_line].programs[self.command_line_program]
        getattr(pride.objects[component], method)(input_bytes)

    def handle_mouse_input(self, mouse_info):
        user_window = pride.objects[self.windows[self.current_user]]
        if mouse_info:
            mouse = Mouse_Structure(*pride.functions.utilities.load_data(mouse_info))
            self.alert("Received mouse info: {}".format(mouse), level=self.verbosity["handle_mouse"])
            user_window.user_input.handle_mousebuttondown(Event_Structure(mouse))
        else:
            self.alert("Received window refresh request", level=self.verbosity["refresh"])

        instructions = user_window.run()
        assert instructions
        return "draw", instructions

    def handle_audio_input(self, audio_bytes):
        self.alert("Received audio: {}...".format(audio_bytes[:50]),
                   level=self.verbosity["handle_audio"])


class Black_Box_Client(pride.components.authentication3.Authenticated_Client):

    defaults = {"target_service" : "/Program/Black_Box_Service",
                "mouse_support" : False, "refresh_interval" : .95,
                "audio_support" : False, "audio_source" : "/Program/Audio_Manager/Audio_Input",
                "microphone_on" : False, "sdl_window" : None,
                "response_methods" : ("handle_response_draw", )}
    required_attributes = ("sdl_window", )
    verbosity = {"handle_input" : 'v', "receive_response" : 'v', "receive_null_response" : 'v'}
    predefaults = {"_refresh_flag" : False}

    def __init__(self, **kwargs):
        super(Black_Box_Client, self).__init__(**kwargs)
        pride.objects["/User/Command_Line"].set_default_program(self.reference, (self.reference, "handle_keyboard_input"))
        if self.mouse_support:
            self.sdl_window.create("pride.gui.blackbox.Client_Window", client=self.reference)
            self.refresh_instruction = pride.Instruction(self.reference, "_refresh")
            self.refresh_instruction.execute(priority=self.refresh_interval)
        if self.audio_support:
            pride.objects[self.audio_source].add_listener(self.reference)

    @pride.components.authentication3.remote_procedure_call(callback_name="receive_response")
    def handle_input(self, packed_user_input):
        pass

    def handle_keyboard_input(self, input_bytes):
        self.handle_input("keyboard " + input_bytes)

    def handle_mouse_input(self, mouse_info):
        self._refresh_flag = False
        self.handle_input("mouse " + mouse_info)

    def handle_audio_input(self, audio_bytes):
        if self.microphone_on:
            self.handle_input("audio " + audio_bytes)

    def receive_response(self, packet):
        try:
            _type, data = packet
        except TypeError:
            self.alert("Received null response", level=self.verbosity["receive_null_response"])
            assert packet is None
        else:
            self.alert("Received response: {}".format(_type), level=self.verbosity["receive_response"])
            response_method = "handle_response_{}".format(_type)
            if response_method in self.response_methods:
                getattr(self, response_method)(data)
            else:
                self.alert("Unsupported response method: '{}'".format(response_method), level=0)

    def handle_response_draw(self, draw_instructions):
        if draw_instructions:
            self.sdl_window.draw(draw_instructions)

    def _refresh(self):
        if self._refresh_flag:
            self.handle_mouse_input('')
        self.refresh_instruction.execute(priority=self.refresh_interval)
        self._refresh_flag = True


def test_black_box_service():
    import pride
    import pride.gui
    import pride.audio
    try:
        pride.objects["/User/Command_Line"]
    except KeyError:
        pride.objects["/User"].create("pride.components.shell.Command_Line")
    window = pride.gui.enable()
    #pride.audio.enable()
    service = pride.objects["/Program"].create(Black_Box_Service)
    client = Black_Box_Client(username="localhost", sdl_window=window, mouse_support=True, audio_support=False)

if __name__ == "__main__":
    test_black_box_service()

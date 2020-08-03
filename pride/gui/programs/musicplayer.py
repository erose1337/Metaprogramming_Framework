# play/pause/skip buttons for a fixed filename
# filename selector

# directory viewer
import os
os.environ["VLC_VERBOSE"] = str("-1")

import vlc

import pride.gui.widgets.form
field_info = pride.gui.widgets.form.field_info


class File_Player(pride.gui.widgets.form.Form):

    defaults = {"fields" : [
                            (field_info("filename"),
                             field_info("volume", minimum=0, maximum=100)),
                            (field_info("track_position", minimum=0,
                                        maximum=1000, auto_create_id=False,
                            entry_kwargs={"include_minmax_buttons" : False,
                                          "include_incdec_buttons" : False,
                                          "hide_text" : True}), ),
                            (field_info("handle_play", button_text="|>",
                                        entry_kwargs={"scale_to_text" : False}),
                             field_info("handle_stop", button_text="[]",
                                        entry_kwargs={"scale_to_text" : False}),
                             field_info("handle_pause", button_text="||",
                                        entry_kwargs={"scale_to_text" : False}),
                             field_info("handle_previous", button_text="<<",
                                        entry_kwargs={"scale_to_text" : False}),
                             field_info("handle_next", button_text=">>",
                                        entry_kwargs={"scale_to_text" : False}))
                            ],
                "_synchronize_instruction" : None}
    mutable_defaults = {"player" : vlc.MediaPlayer,
                        "row_kwargs" : lambda: {0 : {"h_range" : (0, .1)},
                                                1 : {"h_range" : (0, .05)},
                                                2 : {"h_range" : (0, .05)}
                                               }
                       }
    verbosity = {"vlc_error" : "v"}

    def _get_track_position(self):
        output = int(round(1000 * self.player.get_position()))
        if output == -100:
            output = 0
        return output
    def _set_track_position(self, value):
        adjusted = value / 1000.0
        self.player.set_position(adjusted)
    track_position = property(_get_track_position, _set_track_position)

    def _get_volume(self):
        output = self.player.audio_get_volume()
        if output == -1:
            output = 0
        return output
    def _set_volume(self, value):
        self.player.audio_set_volume(value)
    volume = property(_get_volume, _set_volume)

    def __init__(self, **kwargs):
        super(File_Player, self).__init__(**kwargs)
        self.player.set_mrl(self.filename)

    def create_subcomponents(self):
        super(File_Player, self).create_subcomponents()
        self.disable_sliders()

    def disable_sliders(self):
        fields = self.fields_list
        fields[1].editable = False
        fields[2].editable = False

    def enable_sliders(self):
        fields = self.fields_list
        fields[1].editable = True
        fields[2].editable = True

    def handle_value_changed(self, field, old, new):
        if field.name == "filename":
            if self.player.is_playing():
                self.player.stop()
            self.player.set_mrl(new)
        elif field.name == "volume":
            field.update_position_from_value()
        super(File_Player, self).handle_value_changed(field, old, new)

    def handle_play(self):
        self.show_status("Playing {}".format(self.filename))
        player = self.player
        player.play()

        self.enable_slider_synchronization()
        self.enable_sliders()

    def enable_slider_synchronization(self):
        inst = pride.Instruction(self.reference, "synchronize_slider")
        if self._synchronize_instruction is None:
            self._synchronize_instruction = inst
        inst.execute(priority=1)
        self._slider_synchronization_enabled = True

    def disable_slider_synchronization(self):
        if self._synchronize_instruction is not None:
            self._synchronize_instruction.unschedule()
        self._slider_synchronization_enabled = False

    def synchronize_slider(self):
        state = self.player.get_state()
        disable = False
        if state == vlc.State.Error:
            self.alert("VLC Error", verbosity=self.verbosity["vlc_error"])
            self.show_status("VLC Error")
            disable = True
        elif state == vlc.State.Ended:
            self.show_status("Playback ended")
            disable = True

        if disable:
            self.disable_slider_synchronization()
            self.disable_sliders()

        fields = self.fields_list
        volume_bar = fields[1]
        volume_bar.entry.texture_invalid = True
        volume_bar.update_position_from_value()

        seek_bar = fields[2]
        seek_bar.entry.texture_invalid = True
        seek_bar.update_position_from_value()
        if self._slider_synchronization_enabled:
            self._synchronize_instruction.execute(priority=1)

    def handle_stop(self):
        self.show_status("Stopping {}".format(self.filename))
        self.player.stop()
        self.track_position = 0
        self.disable_slider_synchronization()
        self.synchronize_slider()
        self.disable_sliders()

    def handle_pause(self):
        self.show_status("Pausing {}".format(self.filename))
        self.player.pause()
        if hasattr(self, "_synchronize_instruction"):
            self.disable_slider_synchronization()

    def handle_previous(self):
        self.show_status("Back")# to {}".format(self.prior_filename))

    def handle_next(self):
        self.show_status("Next")# to {}".format(self.playlist))

    def delete(self):
        self.disable_slider_synchronization()
        self.player.release()
        del self.player
        super(File_Player, self).delete()


def test_File_Player():
    import pride.gui.main
    program = lambda **kwargs: File_Player(filename="/home/e/Music/test.mp3",
                                           **kwargs)
    pride.gui.main.run_programs([program], position=(0, 60))

if __name__ == "__main__":
    test_File_Player()

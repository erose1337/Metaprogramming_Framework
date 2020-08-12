import os
#os.environ["VLC_VERBOSE"] = str("-1")

import vlc

from pride.gui.widgets.form import field_info
import pride.gui.widgets.formext
Data = pride.gui.widgets.formext.Data

class Controls_Layout(Data):

    #class form_type(pride.gui.widgets.form.Form):


    defaults = {"filename" : '', "volume" : 100, "play_when_opened" : False,
                "_volume_requested" : None, "_synchronize_instruction" : None,
                "fields" : [
                            (field_info("filename"),
                             field_info("volume", minimum=0, maximum=100)),
                            (field_info("track_position", minimum=0,
                                        maximum=1000, auto_create_id=False,
                            entry_kwargs={"include_minmax_buttons" : False,
                                          "include_incdec_buttons" : False,
                                          "hide_text" : True}),
                             field_info("time_info", editable=False,
                                        auto_create_id=False,
                                        w_range=(0, .15)),),
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
                            ]
               }
    mutable_defaults = {"player" : vlc.MediaPlayer,
                        "row_kwargs" : lambda: {0 : {"h_range" : (0, .1)},
                                                1 : {"h_range" : (0, .05)},
                                                2 : {"h_range" : (0, .05)}
                                               }
                       }

    def _get_volume(self):
        output = self.player.audio_get_volume()
        if output == -1:
            output = 0
        return output
    def _set_volume(self, value):
        value = min(100, max(0, value))
        self.player.audio_set_volume(value)
        # vlc cannot adjust volume while not playing/paused
        after = self.volume
        if after != value: # defer setting volume until play begins/resumes
            self._volume_requested = value
    volume = property(_get_volume, _set_volume)

    def _get_track_position(self):
        output = int(round(1000 * self.player.get_position()))
        if output == -100:
            output = 0
        return output
    def _set_track_position(self, value):
        adjusted = value / 1000.0
        self.player.set_position(adjusted)
    track_position = property(_get_track_position, _set_track_position)

    def _get_time_info(self):
        player = self.player
        progress = self._format_time(player.get_time())
        total = self._format_time(player.get_length())
        return "{}/{}".format(progress, total)
    time_info = property(_get_time_info)

    def _format_time(self, ms):
        progressf = []
        seconds = int(round(ms / 1000.0))
        if seconds < 0:
            seconds = 0
        minutes = int(round(seconds / 60.0))
        hours = int(round(minutes / 60.0))
        progressf.append(hours)
        progressf.append(minutes % 60)
        progressf.append(seconds % 60)
        if not hours:
            if not minutes:
                output = str(seconds)
            else:
                output = ':'.join(str(item) for item in progressf[1:])
        else:
            output = ':'.join(str(item) for item in progressf)
        return output

    def __init__(self, **kwargs):
        super(Controls_Layout, self).__init__(**kwargs)
        if self.filename:
            self.player.set_mrl(self.filename)
            if self.play_when_opened:
                self.handle_play()

    def create_subcomponents(self):
        super(Controls_Layout, self).create_subcomponents()
        self.disable_sliders()

    def disable_sliders(self):
        fields = pride.objects[self.form_reference].fields_list
        fields[1].editable = False
        fields[2].editable = False

    def enable_sliders(self):
        fields = pride.objects[self.form_reference].fields_list
        fields[1].editable = True
        fields[2].editable = True

    def handle_play(self):
        filename = self.filename
        _dir, _file = os.path.split(filename)
        should_play = True
        if os.path.exists(_dir):
            if not os.path.exists(filename):
                self.show_status("No file named '{}'".format(filename))
                should_play = False
        if should_play:
            self.show_status("Playing {}".format(self.filename))
            player = self.player
            player.play()

            if self._volume_requested is not None:
                self.volume = self._volume_requested
                self._volume_requested = None

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

        fields = pride.objects[self.form_reference].fields_list
        volume_bar = fields[1]
        volume_bar.entry.texture_invalid = True
        volume_bar.update_position_from_value()

        seek_bar = fields[2]
        seek_bar.entry.texture_invalid = True
        seek_bar.update_position_from_value()
        if self._slider_synchronization_enabled:
            self._synchronize_instruction.execute(priority=1)

        time_info = fields[3]
        time_info.entry.texture_invalid = True

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
        super(Controls_Layout, self).delete()

    def show_status(self, message):
        pride.objects[self.form_reference].show_status(message)


class Directory_Layout: pass
class Visualizer_Layout: pass

class Player_Layout(Data):

    tabs = {"controls" : Controls_Layout,
            "directory" : Directory_Layout,
            "visualizer" : Visualizer_Layout}
    ordering = ("controls", "directory", "visualizer")


class File_Player(pride.gui.widgets.formext.Tabbed_Form):

    def handle_value_changed(self, field, old, new):
        controls = self.target_object.controls
        if field.name == "filename":
            player = controls.player
            if player.is_playing():
                player.stop()
            player.set_mrl(new)
        elif field.name == "volume":
            field.update_position_from_value()
        super(File_Player, self).handle_value_changed(field, old, new)

def test_File_Player():
    import pride.gui.main

    layout = Player_Layout()
    program = lambda **kwargs: File_Player(target_object=layout,
                                           **kwargs)
    pride.gui.main.run_programs([program])

if __name__ == "__main__":
    test_File_Player()

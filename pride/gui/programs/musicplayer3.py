import pride.gui.gui
import pride.gui.programs.musicplayer
import pride.gui.widgets.form
import pride.gui.widgets.formext2
from pride.components import Config
tab_info = pride.gui.widgets.formext2.tab_info
field_info = pride.gui.widgets.form.field_info

class Track(pride.gui.widgets.form.Form):

    defaults = {"filename" : '',
                "fields" : [[field_info("filename", display_name="File name")]]}
    mutable_defaults = {"row_kwargs" : lambda: {0 : {"h_range" : (0, .1)}}}

    def handle_value_changed(self, field, old, new):
        if field.name == "filename":
            tab = pride.objects[self.tab_reference]
            tab.button_text = new
            tab.entry.texture_invalid = True
        super(type(self), self).handle_value_changed(field, old, new)


class Playlist(pride.gui.widgets.formext2.Tabbed_Form):

    defaults = {"include_new_tab_button" : True, "new_window_type" : Track,
                "playlist_name" : '',
                "fields" : [[field_info("playlist_name",
                                        display_name="Playlist name",
                                        orientation="side by side",
                                        id_kwargs={"scale_to_text" : True})]]}


    class form_type(pride.gui.widgets.form.Form):

        defaults = {"h_range" : (0, .05)}

        def handle_value_changed(self, field, old, new):
            if field.name == "playlist_name":
                tab = pride.objects[self.parent.parent.tab_reference]
                tab.button_text = new
                tab.entry.texture_invalid = True
            super(type(self), self).handle_value_changed(field, old, new)
    defaults["form_type"] = form_type


class Library(pride.gui.widgets.formext2.Tabbed_Form):

    defaults = {"include_new_tab_button" : True, "new_window_type" : Playlist,
                "tabs_per_row" : 1}
    subcomponent_kwargs = Config(top_bar={"pack_mode" : "left",
                                          "w_range" : (0, .2),
                                          "h_range" : (0, 1.0)},
                                 new_tab_button2={"w_range" : (0, 1.0),
                                                  "h_range" : (0, .1),
                                                  "pack_mode" : "top"},
                                 tab={"entry_kwargs" :
                                        {"scale_to_text" : False}},
                                 tab_bar={"pack_mode" : "top",
                                          "max_rows" : 8},
                                 tab_bar_row={"h_range" : (0, .1)})


class Visualizer(pride.gui.gui.Window): pass

class File_Player(pride.gui.widgets.formext2.Tabbed_Form):

    tabs = [tab_info("controls", pride.gui.programs.musicplayer.File_Player),
            tab_info("library", Library),
            tab_info("visualizer", Visualizer)]

def test_File_Player():
    import pride.gui.main
    pride.gui.main.run_programs([File_Player])

if __name__ == "__main__":
    test_File_Player()

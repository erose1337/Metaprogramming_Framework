#music visualizer
#================
#
#        note_1  note_3  note_5  note_7
#        note_2  note_4  note_6  note_8
#
#   highlight current note
#   draw transition from current note to next current note
import pride.gui.gui

DEFAULT_NOTES = ['D', 'E', 'F', 'G', 'A', 'B', 'C']

class Note_Theme(pride.gui.gui.Minimal_Theme):

    theme_profiles = ("unselected", "activated")
    theme_colors = dict((profile, pride.gui.gui._default_colors()) for profile in theme_profiles)
    theme_colors["activated"]["background"] = pride.gui.color.Color(245, 245, 220)
    _theme_users = []


class Note_Visualizer(pride.gui.gui.Container):

    defaults = {"theme_type" : Note_Theme, "theme_profile" : "unselected",
                "location" : "left"}

    def left_click(self, mouse):
        super(Note_Visualizer, self).left_click(mouse)
        self.parent_application.activate_note(self.text)


class Music_Visualizer(pride.gui.gui.Application):

    defaults = {"notes" : DEFAULT_NOTES, "current_note" : ''}
    mutable_defaults = {"active_profile" :pride.gui.gui._default_colors,
                        "backup_profiles" : dict}

    def __init__(self, **kwargs):
        super(Music_Visualizer, self).__init__(**kwargs)
        music_notes = self.notes
        window = self.application_window
        top_row = window.create("pride.gui.gui.Container")
        bottom_row = window.create("pride.gui.gui.Container")
        _notes = self._notes = []

        for index, musical_note in enumerate(music_notes + [music_notes[0]]):
            if index % 2 == 0:
                note = top_row.create(Note_Visualizer, text=musical_note)
            else:
                note = bottom_row.create(Note_Visualizer, text=musical_note)
            _notes.append(note.reference)

    def activate_note(self, note):
        note = self._notes[self.notes.index(note)]
        current = self.current_note
        if current:
            profile = self.backup_profiles.pop(current)
            visualizer = pride.objects[current]
            visualizer.theme_profile = profile

        self.current_note = note
        visualizer = pride.objects[note]
        self.backup_profiles[note] = visualizer.theme_profile
        visualizer.theme_profile = "activated"

def main():
    try:
        window = pride.objects["/SDL_Window"]
    except KeyError:
        window = pride.objects[pride.gui.enable()]
    visualizer = window.create(Music_Visualizer)

if __name__ == "__main__":
    main()

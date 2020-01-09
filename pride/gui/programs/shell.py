import subprocess
import tempfile
import getpass
import shlex

import pride.gui.widgets.form

field_info = pride.gui.widgets.form.field_info

class Shell(pride.gui.widgets.form.Scrollable_Window):

    defaults = {"text_field" : '', "input_field" : '', "stdin" : None,
                "line_count" : 24, "offset" : 0, "process" : None}
    mutable_defaults = {"input_history" : list, "lines" : list,
                        "vertical_slider_entry_kwargs" :\
                            lambda: {"orientation" : "stacked",
                                     "include_minmax_buttons" : False,
                                     "hide_text" : True}}
    hotkeys = {('\n', None) : "handle_return"}
    autoreferences = ("_form", )

    def __init__(self, **kwargs):
        super(Shell, self).__init__(**kwargs)
        self.create_subcomponents()

    def create_subcomponents(self):
        window = self.main_window
        fields = [[field_info("text_field", auto_create_id=False,
                              editable=False,
                              entry_kwargs={"center_text" : False,
                                            "hoverable" : False,
                                            "font" : "Hack-Regular"})],
                  [field_info("input_field", orientation="side by side",
                              field_type=pride.gui.widgets.form.Text_Field,
                              parent_shell=self,
                              display_name=self._get_user_string(),
                              entry_kwargs={"center_text" : False,
                                            "font" : "Hack-Regular"})]
                 ]
        form = window.create(pride.gui.widgets.form.Form, fields=fields,
                             target_object=self)
        form.rows[1].h_range = (24, 24)
        self._form = form

    def _get_user_string(self):
        return "{}@{}:{}".format(getpass.getuser(), os.uname()[1], os.getcwd())

    def handle_return(self):
        input_field = self.input_field; lines = self.lines
        if not input_field:
            return
        if self.stdin is not None:
            new_line = input_field
        else:
            new_line = self._get_user_string() + ' ' + input_field
        lines.append(new_line)

        self.input_history.append(input_field)
        self.input_field = ''

        if self.stdin is not None:
            process = self.process
            _stdin = process.stdin
            _stdin.write(input_field)
            _stdin.flush()
        else:
            pipe = subprocess.PIPE
            stdout = pipe#tempfile.TemporaryFile()#None#pipe
            stderr = subprocess.STDOUT
            stdin = tempfile.TemporaryFile()
            args = shlex.split(input_field)
            try:
                process = subprocess.Popen(args, stdout=stdout, stderr=stderr,
                                           stdin=stdin)
            except OSError as error:
                if error.errno != 2:
                    raise
                return
            self.process = process

        stdout = process.stdout
        if stdout is not None:
            output = stdout.read()
            if output:
                output = output.split('\n')
                lines.extend(output)
                if not self.vertical_slider.hidden:
                    self.offset += len(output)
                    self.synchronize_scroll_bars()

        code = process.wait()
        # > A None value indicates that the process hasn’t terminated yet.
        #      -> not None indicates the process has terminated
        if code is not None and input_field != "python":
            print("Process terminated with code {}".format(code))
            self.stdin = None
            self.process = None
        else:
            print("Process did NOT terminate")

        assert self.vertical_slider is not None # relies on below to call `update_text_field`
        self.synchronize_scroll_bars()

    def update_text_field(self):
        self.text_field = '\n'.join(self.lines[self.offset:self.offset + self.line_count])
        #print("Wrote {} lines:".format(len(self.text_field.split('\n'))))
        #print(self.text_field)
        self._form.synchronize_fields()

    def handle_area_change(self, old_area):
        super(Shell, self).handle_area_change(old_area)
        font_size = self.sdl_window.renderer.font_manager.wrapped_object.size
        self.line_count = int(float(self._form.rows[0].h) / (font_size + 3))
        self.synchronize_scroll_bars()

        #if not self.lines:
        #    self.lines = ['\n'] * self.line_count

    def handle_y_scroll(self, old_value, new_value):
        super(Shell, self).handle_y_scroll(old_value, new_value)
        self.offset = new_value
        self.update_text_field()

    def synchronize_scroll_bars(self):
        slider = self.vertical_slider
        if slider is not None:
            slider.maximum = max(0, len(self.lines) - self.line_count)
            slider.update_position_from_value()
            slider.pack()
            self.update_text_field()
            #entry = slider.entry
            #entry.max_button.entry.texture_invalid = True
            #entry.min_button.entry.texture_invalid = True

    def delete(self):
        if self.process is not None:
            self.process.terminate()
            self.process = None
        super(Shell, self).delete()

def test_Shell():
    import pride.gui
    window = pride.objects[pride.gui.enable(x=50, y=65)]
    window.tip_bar.hide()
    window.create("pride.gui.main.Gui", startup_programs=(Shell, ),
                  user=pride.objects["/User"])

if __name__ == "__main__":
    test_Shell()

import subprocess
import tempfile
import getpass
import shlex
from math import ceil

import pride.gui.widgets.form
import pride.gui.widgets.formext

field_info = pride.gui.widgets.form.field_info

class Shell(pride.gui.widgets.formext.Scrollable_Text_Window):

    defaults = {"stdin" : None, "process" : None}

    def _get_user_string(self):
        return "{}@{}:{}".format(getpass.getuser(), os.uname()[1], os.getcwd())

    def create_subcomponents(self):
        super(Shell, self).create_subcomponents()
        self.write_to(self._get_user_string() + ' ')

    def handle_backspace(self):
        if self.lines[-1] != self._get_user_string() + ' ':
            super(Shell, self).handle_backspace()

    def handle_return(self):
        super(Shell, self).handle_return()
        command = self.lines[-2][len(self._get_user_string()) + 1:] # -2 because handle_return creates a new line; +1 because of space
        if not command.strip():
            #print("No command -2: {} -1: {}".format(self.lines[-2], self.lines[-1]))
            self.write_to(self._get_user_string() + ' ')
            return

        if self.process is not None:
            self.poll_process() # will clear .process and .std* if necessary

        if self.process is not None:
            print("Input: {}".format(command))
            stdin = self.process.stdin
            stdin.write(command + '\n')
            stdin.flush()
        else:
            self.run_command(command)
        self.read_stdout()

        self.lines.append(self._get_user_string() + ' ')
        self.synchronize_scroll_bars()

        if self.process is not None:
            self.poll_process()

    def run_command(self, command):
        assert self.process is None
        args = shlex.split(command)
        stdout = stderr = open("_prideshell.temp", "wb")
        self.stdout = open("_prideshell.temp", 'r')
        stdin = subprocess.PIPE
        print("Command: {} ({})".format(command, args))
        try:
            process = subprocess.Popen(args, stdout=stdout, stderr=stderr,
                                       stdin=stdin)
        except OSError as error:
            if error.errno not in (2, 13):
                raise
            if error.errno == 13 and os.path.exists(command):
                if os.path.isdir(command):
                    self.write_to("Shell: {}: Is a directory".format(command))
                else:
                    self.write_to("Shell: {}: Permission denied".format(command))
            print("Ignoring {} '{}'".format(error, command))
            self.lines.append(self._get_user_string() + ' ')
            self.y_scroll_value += 1
            self.synchronize_scroll_bars()
            return
        import time
        time.sleep(.01)
        self.process = process
        #self.sdl_window.schedule_postdraw_operation(self.check_output, self)

    def read_stdout(self):
        stdout = self.stdout
        if stdout is not None:
            stdout.flush()
            output = stdout.read()
            #print("Read {} bytes".format(len(output)))
            if output:
                output = output.split('\n')
                self.write_to(output.pop(0))
                if any(output):
                    self.lines.extend(output)
                if not self.vertical_slider.hidden:
                    self.y_scroll_value += len(output)
#                    self.synchronize_scroll_bars()
#                else:
#                    self.update_text_field()

    def poll_process(self):
        code = self.process.poll()
        # > A None value indicates that the process hasn’t terminated yet.
        #      -> not None indicates the process has terminated
        if code is not None:
            print("Process terminated with code {}".format(code))
            if self.stdin is not None:
                self.stdin.close()
            if self.stdout is not None:
                self.stdout.close()
            self.stdin = self.stdout = self.process = None
        else:
            print("Process did NOT terminate")
        return code

    def delete(self):
        if self.process is not None:
            if self.process.returncode is None:
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

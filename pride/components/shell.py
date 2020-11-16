import random
import sys
import os
import codeop
import traceback
import inspect

import pride
import pride.components.scheduler
import pride.functions.utilities
import pride.components._termsize

try:
    from msvcrt import getwch, kbhit
    input_waiting = kbhit
    PLATFORM = "Windows"
except:
    PLATFORM = "POSIX"
    import select
    def input_waiting():
        return select.select([sys.stdin], [], [], 0.0)[0]

def get_permission(prompt):
    """ Displays prompt to the user. Attempts to infer whether or not the supplied
        user input is affirmative or negative via shell.is_affirmative. """
    return get_selection(prompt, bool)

def get_selection(prompt, answers):
    """ Displays prompt to the user. Only input from the supplied answers iterable
        will be accepted. bool may be specified as answers in order to extract
        a True/False response. """
    selection = None
    while selection is None:
        selection = raw_input(prompt)
        if answers == bool:
            selection = is_affirmative(selection)
        else:
            selection = None if selection not in answers else selection
    return selection

def is_affirmative(input, affirmative_words=("affirmative", "true")):
    """ Attempt to infer whether the supplied input is affirmative. """
    if not input:
        return None
    lowered = input.lower()
    for affirmative in affirmative_words:
        if affirmative in lowered:
            is_positive = True
            break
    else:
        y_location = lowered.find('y')
        n_location = lowered.find('n')
        if y_location != -1:
            if n_location != -1:
                is_positive = True if y_location < n_location else False
            else:
                is_positive = True
        elif n_location != -1:
            is_positive = False
        else:
            is_positive = None
    return is_positive


class Command_Line(pride.components.scheduler.Process):
    """ Captures user input and provides the input to the specified or default program.

        Available programs can be modified via the add_program, remove_program,
        set_default_program, and get_program methods."""
    defaults = {"write_prompt" : True,
                "prompt" : ">>> ", "programs" : None,
                "default_programs" : ("pride.components.shell.OS_Shell",
                                      "pride.components.shell.Switch_Program"),
                "idle_threshold" : 1000,
                "screensaver_type" : "pride.components.shell.Random_Screensaver",
                "_raw_input_callback" : None,
                "priority" : .05}

    def __init__(self, **kwargs):
        self._idle = True
        self.screensaver = None
        super(Command_Line, self).__init__(**kwargs)

        self.programs = self.programs or {}
        default_program = self.create(self.default_programs[0])
        self.set_default_program(default_program.name, (default_program.reference, "handle_input"), set_backup=True)

        for program in self.default_programs[1:]:
            self.create(program)

        pride.Instruction(self.reference, "handle_idle").execute(priority=self.idle_threshold)
        self._input_generator = self._new_input_generator()

    def add_program(self, program_name, callback_info):
        self.programs[program_name] = callback_info

    def remove_program(self, program_name):
        del self.programs[program_name]

    def set_default_program(self, name, callback_info, set_backup=False):
        if name not in self.programs:
            self.programs[name] = callback_info
        self.default_program = callback_info
        if set_backup:
            self.__default_program = callback_info

    def get_program(self, program_name):
        if program_name == "default":
            result = self.default_program
        elif program_name == "__default":
            result = self.__default_program
        else:
            result = self.programs.get(program_name, self.default_program)
        return result

    def set_prompt(self, prompt):
        self.prompt = prompt

    def __getstate__(self):
        attributes = super(Command_Line, self).__getstate__()
        return attributes

    def _new_input_generator(self):
        while True:
            if input_waiting():
                try:
                    input = sys.stdin.readline()
                except ValueError: # main thread exited
                    raise SystemExit()
                self._idle = False
                self.clear_screensaver()
                self.handle_input(input)
            yield

    def run(self):
        next(self._input_generator)

    def clear_screensaver(self):
        if self.screensaver is not None:
            pride.objects[self.screensaver].delete()
            self.screensaver = None
            self.clear()
            previous_log_contents = sys.stdout_log[:self._position]
            sys.stdout.write(previous_log_contents)
            sys.stdout.flush()
            sys.stdout.logging_enabled = True

    def handle_input(self, input):
        self.alert("Got user input {}".format(input), level='vvv')
        if self._raw_input_callback:
            callback = self._raw_input_callback
            self._raw_input_callback = None
            return callback(input)
        try:
            program_name, program_input = input.split(' ', 1)
        except ValueError:
            if input.strip() not in self.programs:
                component, method = self.default_program
                program_input = input
            else:
                component, method = self.programs[input]
                program_input = ''
        else:
            if (program_input != '\n' and program_input.split()[0] in
               ("+", '-', '*', '%', '/', '//', '**', '=', '==',
                '+=', '-=', '*=', '%=', '/=', '//=', '**=',
                '>>', '<<', '||', '&&', '>>=', '<<=', '||=', '&&=',
                "and", "or", "not")):
                component, method = self.default_program
                program_input = input
            else:
                try:
                    component, method = self.programs[program_name]
                except KeyError:
                    component, method = self.default_program
                    program_input = input
        pride.Instruction(component, method, program_input).execute()
        #if self.write_prompt:
        #    sys.stdout.write(self.prompt)

    def handle_idle(self):
        if self._idle and not self.screensaver:
            self._position = sys.stdout_log.tell()
            sys.stdout.logging_enabled = False
            self.alert("Starting terminal screensaver; Press enter to resume... ")
            self.screensaver = self.create(self.screensaver_type).reference
        self._idle = True
        pride.Instruction(self.reference, "handle_idle").execute(priority=self.idle_threshold)

    def clear(self):
        if PLATFORM == "Windows":
            command = "CLS"
        else:
            command = "clear"
        os.system(command)


class Program(pride.components.base.Base):

    defaults = {"set_as_default" : False, "name" : '',
                "command_line" : "/User/Command_Line"}

    def _get_name(self):
        return self._name or self.reference
    def _set_name(self, value):
        self._name = value
    name = property(_get_name, _set_name)

    def __init__(self, **kwargs):
        super(Program, self).__init__(**kwargs)
        if self.set_as_default:
            self.set_as_default_program()
        else:
            self.add_to_programs()

    def handle_input(self, input):
        try:
            command, input = input.split(' ', 1)
        except ValueError:
            command = input
            input = ''
        return getattr(self, command, self.help)(input)

    def help(self, input):
        self.alert("Unrecognised command '{}'".format(input), level=0)
        print self.__doc__

    def set_as_default_program(self):
        pride.objects[self.command_line].set_default_program(self.name, (self.reference, "handle_input"))

    def add_to_programs(self):
        pride.objects[self.command_line].add_program(self.name, (self.reference, "handle_input"))


class Program_Shell(Program):

    defaults = {"name" : "python", "shell_connection" : "/User/Shell"}

    predefaults = {"user_is_entering_definition" : False, "prompt" : ">>> ",
                   "lines" : ''}

    def handle_input(self, user_input):
        if not user_input:
            user_input = '\n'

        self.lines += user_input
        lines = self.lines
        write_prompt = True
        output = None

        if lines != "\n":
            try:
                code = codeop.compile_command(lines, "<stdin>", "exec")
            except (SyntaxError, OverflowError, ValueError) as error:
                sys.stdout.write(traceback.format_exc())
                self.prompt = ">>> "
                sys.stdout.write(self.prompt)
                self.lines = ''
            else:
                if code:
                    if self.user_is_entering_definition:
                        if lines[-2:] == "\n\n":
                            self.prompt = ">>> "
                            self.lines = ''
                            pride.objects[self.shell_connection].execute_source(lines)
                            self.user_is_entering_definition = False
                    else:
                        self.lines = ''
                        pride.objects[self.shell_connection].execute_source(lines)
                        write_prompt = False
                else:
                    self.user_is_entering_definition = True
                    self.prompt = "... "
        else:
            self.lines = ''
        pride.objects["/User/Command_Line"].set_prompt(self.prompt)
        sys.stdout.write("\b" * 4 + self.prompt)
        sys.stdout.flush()


class OS_Shell(Program):

    defaults = {"use_shell" : True, "name" : "os_shell"}

    def handle_input(self, input):
        pride.functions.utilities.shell(input, shell=self.use_shell)


class Switch_Program(Program):

    defaults = {"name" : "switch"}

    def handle_input(self, input):
        command_line = pride.objects["/User/Command_Line"]
        if not input:
            input = "__default"
        _input = input.strip()
        command_line.set_default_program(_input, command_line.get_program(_input))


class Messenger_Program(Program):

    defaults = {"name" : "messenger"}

    def handle_input(self, user_input):
        destination, message = user_input.split(':', 1)
        pride.objects["/Messenger_Client"].send_message(destination, message,
                                                        self.reference)


class Terminal_Screensaver(pride.components.scheduler.Process):

    defaults = {"rate" : 3, "priority" : .08, "newline_scalar" : 1.5,
                "file_text" : ''}

    def __init__(self, **kwargs):
        super(Terminal_Screensaver, self).__init__(**kwargs)
        self._priority = self.priority

    def run(self):
        if not self.file_text:
            if random.choice((True, False)):
                name = random.choice(list(pride.objects))
                instance = pride.objects[name] # get a random instance
                pride.objects[name] = instance
                self.file_text = '\n' + name + ':\n' + instance.__doc__
            else:
                module = None
                while module is None:
                    name = random.choice(sys.modules.keys())
                    module = sys.modules[name]
                    try:
                        source = inspect.getsource(module)
                    except (TypeError, IOError):
                        continue
                self.file_text = "\n" + source + "\n"

        sys.stdout.write(self.file_text[:self.rate])
        if '\n' in self.file_text[:self.rate]:
            self.priority *= self.newline_scalar
        else:
            self.priority = self._priority

        self.file_text = self.file_text[self.rate:]


class Random_Screensaver(Terminal_Screensaver):

    choices = ["pride.components.shell.Terminal_Screensaver",
               "pride.components.shell.Matrix_Screensaver",
               "pride.components.shell.CA_Screensaver"]

    def __new__(cls, *args, **kwargs):
        _type = random.choice(cls.choices)
        __type = pride.functions.utilities.resolve_string(_type)
        return __type(*args, **kwargs)


class Matrix_Screensaver(Terminal_Screensaver):

    defaults = {"priority" : .08, "column" : None, "index" : 0}
    mutable_defaults = {"characters" : list}

    def __init__(self, **kwargs):
        super(Matrix_Screensaver, self).__init__(**kwargs)
        self.width, self.height = pride.components._termsize.getTerminalSize()
        for x in xrange(self.height):
            row = [' '] * self.width
            row[-1] = '\n'
            self.characters.append(row)

    def run(self):
        if self.column is None:
            self.column = random.randint(0, self.width - 2)
            self.index = 0
        self.characters[self.index][self.column] = unichr(random.randint(0, 255))
        self.index += 1
        if self.index == self.height:
            self.column = None
            self.index = 0
        pride.objects["/User/Command_Line"].clear()
        sys.stdout.write(''.join(''.join(item) for item in self.characters))
        sys.stdout.flush()


class CA_Screensaver(Terminal_Screensaver):

    defaults = {"storage_size" : pride.components._termsize.getTerminalSize()[0],
                "character1" : 'A', "character0" : ' '}

    rule_30 = {(1, 1, 1) : 0, (1, 1, 0) : 0, (1, 0, 1) : 0, (1, 0, 0) : 1,
               (0, 1, 1) : 1, (0, 1, 0) : 1, (0, 0, 1) : 1, (0, 0, 0) : 0}

    def __init__(self, **kwargs):
        super(CA_Screensaver, self).__init__(**kwargs)
        self.bytearray = bytearray(self.storage_size)
        self.bytearray[ord(os.urandom(1)) % self.storage_size] = 1
        self._state = CA_Screensaver.rule_30
        self.translator = {ord(self.character1) : 1, 1 : 1,
                           ord(self.character0) : 0, 0 : 0}
    def run(self):
        _bytearray = self.bytearray
        size = self.storage_size
        new_bytearray = bytearray(size)
        rule = self._state
        translator = self.translator
        for index, byte in enumerate(_bytearray):
            current_state = (translator[_bytearray[index - 1]],
                             translator[byte],
                             translator[_bytearray[(index + 1) % size]])
            value = rule[current_state]
            if value == 1:
                display_character = 'A'
            else:
                display_character = ' '
            new_bytearray[index] = display_character
        self.bytearray = new_bytearray
        sys.stdout.write(new_bytearray)
        sys.stdout.write("\n")
        sys.stdout.flush()


class Wave_CAtest(Terminal_Screensaver):

    def __init__(self, **kwargs):
        super(Wave_CAtest, self).__init__(**kwargs)
        self.rows = [[(0, 0) for y in xrange(16)] for x in xrange(16)]
        random_coordinate = format(ord(random._urandom(1)), 'b').zfill(8)
        x = int(random_coordinate[:4], 2)
        y = int(random_coordinate[4:], 2)
        self.rows[x][y] = (ord(random._urandom(1)), ord(random._urandom(1)))

    def run(self):
        new_rows = [[(0, 0) for y in xrange(16)] for x in xrange(16)]

        last_row = False
        for row_index, row in enumerate(self.rows):
            new_row = [(0, 0) for x in range(16)]
            if row_index == 15:
                last_row = True
            for point_index, magnitudes in enumerate(row):
                x_magnitude, y_magnitude = magnitudes
                if point_index == 15:
                    x_magnitude = -x_magnitude
                if x_magnitude > 0:
                    x_magnitude -= 1
                    new_x_coord = point_index + 1
                elif x_magnitude < 0:
                    x_magnitude += 1
                    new_x_coord = point_index - 1
                else:
                    new_x_coord = point_index

                if last_row:
                    y_magnitude = -y_magnitude
                if y_magnitude > 0:
                    y_magnitude -= 1
                    new_y_coord = row_index + 1
                elif y_magnitude < 0:
                    y_magnitude += 1
                    new_y_coord = row_index - 1
                else:
                    new_y_coord = row_index
                if new_y_coord > 15:
                    new_y_coord = 15
                elif new_y_coord < 0:
                    new_y_coord = 0
                    y_magnitude = -y_magnitude
                if new_x_coord > 15:
                    new_x_coord = 15
                elif new_x_coord < 0:
                    new_x_coord = 0
                    x_magnitude = -x_magnitude

                self.rows[new_y_coord][new_x_coord] = (x_magnitude, y_magnitude)

        pride.objects["/User/Command_Line"].clear()
        def decide_symbol(number):
            if number[0] or number[1]:
                return str(number[0]) + str(number[1])
            else:
                return '*'
        print '\n'.join((''.join(decide_symbol(number) for number in row) for row in self.rows))


class Chaos_Screensaver(Terminal_Screensaver):

    defaults = {"storage_size" : 1600}

    def __init__(self, **kwargs):
        super(Chaos_Screensaver, self).__init__(**kwargs)
        self.bytearray = bytearray(self.storage_size)
        self.bytearray[ord(os.urandom(1)) % self.storage_size] = ord(os.urandom(1))
        self.coroutine = self.advance_state()
        next(self.coroutine)

    @staticmethod
    def rotate_left(x, r, bit_width=8, _mask=dict((bit_width, ((2 ** bit_width) - 1)) for bit_width in (8, 16, 32, 64, 128))):
        r %= bit_width
        return ((x << r) | (x >> (bit_width - r))) & _mask[bit_width]

    def advance_state(self):
        data = self.bytearray

        total = 0
        for byte in data:
            total ^= byte

        size = len(data)
        rotate_left = self.rotate_left
        while True:
            for index in range(size):
                byte = data[index]
                total ^= byte
                byte ^= rotate_left(total, index) ^ (index % 256) ^ data[(index + 1) % size] ^ data[(index - 1) % size]
                total ^= byte

                data[index] = byte
                yield

    def run(self):
        next(self.coroutine)
        pride.objects["/User/Command_Line"].clear()
        sys.stdout.write(self.bytearray)
        sys.stdout.write("\n")
        sys.stdout.flush()

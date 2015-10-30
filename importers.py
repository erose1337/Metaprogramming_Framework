""" Contains import related functions and objects, including the compiler """
import os
import inspect
import sys
import importlib
import contextlib
import types
import imp
import tokenize
import shlex
import string
import operator
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO
  
OPERATORS = ('+', '-', '*', '**', '/', '//', '%', '<<', '>>', '&', '|', '^',
             '~', '<', '>', '<=', '>=', '==', '!=', '<>')
               
DELIMITERS = ('(', ')', '[', ']', '{', '}', '@', ',', ':', '.', '`', '=',
              ';', '$', '+=', '-=', '*=', '/=', '//=', '%=', '&=', '|=', 
              '^=', ">>=", "<<=", "**=", ' ', '\n')
                
unused = tuple("$?")

misc = tuple("\'\"\#\\")

special_symbols = misc + unused + DELIMITERS + OPERATORS
  
@contextlib.contextmanager
def sys_meta_path_switched(new_meta_path):
    backup = sys.meta_path
    sys.meta_path = new_meta_path
    try:
        yield
    finally:
        sys.meta_path = backup

@contextlib.contextmanager        
def imports_from_disk():
    with sys_meta_path_switched([From_Disk()]):
        yield
                    
class From_Disk(object):
        
    def __init__(self, modules=tuple()):
        self.modules = modules
        
    def find_module(self, module_name, path):
        if not self.modules or module_name in self.modules:
            return self
        return None
        
    def load_module(self, module_name):
        del sys.modules[module_name]
        sys.modules[module_name] = module = importlib.import_module(module_name)
        return module
        
       
class Parser(object):
    
    @staticmethod
    def get_string_indices(source):
        """ Return a list of indices of strings found in source. 
            Includes substrings located within other strings. """
        quote_symbols = ["'", '"', "'''", '"""']        
        triple_quote_start = triple_quote_end = ignore_count = 0
        source_length = len(source) - 1
        triple_quote_closing = closing_quote = ''
        indices, open_quotes = [], []
        start_index, end_index = {}, {}
    #    print "Getting strings from: ", len(source), source
        for index, character in enumerate(source):
         #   print index, len(source)
            if character == '\\': # backslash
                ignore_count += 2                
            elif character == '#':
                try:
                    newline = source[index:].index('\n') + index
                except ValueError: # comment with no newline at end of file
                    break
                else:
                    ignore_count = newline - index
                                
            if ignore_count:
                ignore_count -= 1
                continue
            _character = source[index:index + min(3, source_length - index)]
            is_triple_quote = _character in quote_symbols                    
            if is_triple_quote or character in quote_symbols:
                if is_triple_quote:
                    character = _character
                    ignore_count = 2
                    
                if character not in start_index:
                    open_quotes.append(character)
                    start_index[character] = index
                else:
                    end_index[character] = index + len(character)
                    
            if character in end_index:
                indices.append((start_index[character], end_index[character]))
                layer = open_quotes.index(character)
                for __character in open_quotes[layer:]:
                    end_index.pop(__character, None)
                    start_index.pop(__character, None)
                open_quotes = open_quotes[:layer]
        return sorted(indices, key=operator.itemgetter(0))
    
    @staticmethod    
    def find_symbol(symbol, source, quantity=0, back_delimit=True, 
                    forward_delimit=True, start_index=0):
        """ Locates all occurrences of symbol inside source up to the given
            quantity of times. Matches only count if the symbol is not inside
            a quote or behind a comment. """
        strings = [range(start, end + 1) 
                   for start, end in Parser.get_string_indices(source)]
        delimiters = DELIMITERS + OPERATORS
        #print "Found strings: "
        #for _range in strings[:len(strings) / 2]:
        #    print source[_range[0]:_range[-1]], '...', " index: ", _range[0], _range[-1]
        indices = []
        symbol_size = len(symbol)
        source_index = start_index
        source_length = len(source)
    #    print "# Trying to find: {} ".format(symbol), start_index, len(source)#, source[source_index:]
        while symbol in source[source_index:] and quantity > 0:          
            start = source.index(symbol, source_index)
    #        print "Found start of symbol: ", start
            for string_range in strings:
                if start in string_range:
                   # print "Ignoring potential match that is inside string: ", source[string_range[0]:string_range[-1]]
                    source_index += string_range[-1]
                    break
            else: # did not break, symbol is not inside a quote
                end = start + symbol_size
                #print start-1, end, end-start, len(source), symbol, source
    #            print "->Found potential match: {} in ".format(symbol), source[start-1:end+1]
                is_back_delimited = (start - 1 >= 0 and source[start-1] in delimiters or start == 0)
                is_forward_delimited = (end == source_length or source[end] in delimiters)
                if back_delimit:
                    if is_back_delimited:
                        if forward_delimit:
                            if is_forward_delimited:
    #                            print "Found forward/back delimited ", symbol, (start, end)
                                quantity -= 1
                                indices.append((start, end))
                        else:
    #                        print "Found back delimited {}".format(symbol), (start, end)
                            quantity -= 1
                            indices.append((start, end))                
                elif forward_delimit:
                    if is_forward_delimited:
    #                    print "Found forward delimited ", symbol, (start, end)
                        quantity -= 1
                        indices.append((start, end))
                elif not (back_delimit or forward_delimit):
    #                print "Found non delimited ", symbol, (start, end)
                    quantity -= 1
                    indices.append((start, end))
                else:
                    print "Found non properly delimited symbol: {} at {}".format(symbol, (start, end))
        #            print source[start-20:end+20], (start - 1 >= 0 and source[start-1] in delimiters), start ==0
                source_index = end
    #        print "Incrementing index by {} to {}".format(end, source_index)
        return indices
        
    @staticmethod
    def replace_symbol(symbol, source, replacement, back_delimit=True,
                       forward_delimit=True, start_index=0):
        delimiters = DELIMITERS + OPERATORS
        #print "\nReplacing {} with {}".format(symbol, replacement)
        _count = 0
        while symbol in source:
            slice_information = Parser.find_symbol(symbol, source, 1, 
                                                   back_delimit, forward_delimit,
                                                   start_index)
            if not slice_information: # last symbol in source was in a string
        #        print "last symbol in source was a string", slice_information
                break
            symbol_start, _end = slice_information[0]
          #  print "\nFound string replacement: ...", source[symbol_start-10:_end+10] + "...", "index: ", symbol_start, _end
            for index, character in enumerate(source[symbol_start + 1:]):
                if character in delimiters:
        #            print "Found word delimiter: ", character, source[symbol_start:symbol_start + index + 1]
                    delimiter = delimiters[delimiters.index(character)]
                    end_index = index
                    break
            else:
                end_index = index
            name = source[symbol_start + 1:symbol_start + end_index + 1]
            replaced = replacement.format(name)
        #    print "Created replacement symbol: ", replacement
            source = ''.join((source[:symbol_start], replaced,
                              source[symbol_start + 1 + len(name):]))
            _count += 1
            start_index = symbol_start + 1 + len(replaced)
      #  assert symbol not in source, source
    
      #  print "Created replacement source: ", source
        return source 
        
    @staticmethod
    def remove_comments(source):
        new_source = []
        for line in source.split('\n'):
            if '#' in line:
                _line = line[:line.index('#')]
                if not _line.replace('\t', '    ').replace('    ', ''):
                    #print "removing comment line: ", line
                    continue
            new_source.append(line)
        return '\n'.join(new_source)
        
    @staticmethod
    def remove_docstring(source):
        """ Returns source without docstring """
        indices = Parser.get_string_indices(source)
        result = source
        if indices:
            start_of_string, end_of_string = indices[0]
            if (source[start_of_string-4:start_of_string] == '    ' or
                source[start_of_string-1] == '\t'):
                result = source[:start_of_string] + source[end_of_string:]            
        return result
      
    @staticmethod
    def remove_header(source):
        """ Returns source without a class or def header. """
        if not (':' in source and '\n' in source and 
                ('    ' in source or '\t' in source)):
            raise ValueError("Could not find class or def header in {}".format(source))      
        colon_found = newline_found = indent_found = False 
        enclosing_characters = ('{', '[', '(')
        end_enclosing_characters = ('}', ']', ')')
        enclose_count = 0
        for index, character in enumerate(source):
            if character in enclosing_characters:
            #    print "Found opening character: ", character
                enclose_count += 1
            elif character in end_enclosing_characters:
           #     print "Found closing character: ", character
                enclose_count -= 1
            if not enclose_count:
                if character == ':' and not colon_found:
                    colon_found = True
                elif character == '\n':
                    newline_found = True
                elif character == '\t' or source[index:index+4] == "    ":
                    indent_found = True
            if colon_found and newline_found and indent_found:
                end_of_header = index
                break
        return source[end_of_header:]
                
    @staticmethod
    def extract_code(source):
        """ Returns source without header, comments, or docstring. """
        return Parser.remove_docstring(Parser.remove_header(Parser.remove_comments(source)))
        
        
class Compiler(object):
    """ Compiles python source to bytecode. Source may be preprocessed.
        This object is automatically instantiated and inserted into
        sys.meta_path as the first entry. """
    def __init__(self, preprocessors=tuple()):
        self.preprocessors = preprocessors
        self.path_loader, self.module_source = {}, {}
                            
    def find_module(self, module_name, path):
        modules = module_name.split('.')
        loader = None
        end_of_modules = len(modules) - 1
        for count, module in enumerate(modules):
            try:
                _file, _path, description = imp.find_module(module, path)
            except ImportError:
                pass
            else:
                if _path.split('.')[-1] == "pyd":
                    continue
                if _file:
                    if ".pyc" in _path:
                        print "Unable to import {} @ {}; No source, only bytecode available".format(module_name, _path)
                        break
                    self.module_source[module_name] = (_file.read(), _path)
                    if count == end_of_modules:
                        loader = self
        return loader    
    
    def load_module(self, module_name):
        if module_name not in sys.modules:
            source, path = self.module_source[module_name]
            module_code = self.compile(source, path)
            self.compile_module(module_name, module_code, path)
 #       print "Loading: ", module_name
        return sys.modules[module_name]
                    
    def compile_module(self, module_name, module_code, path):
        new_module = types.ModuleType(module_name) 
    #    print '\n\ncompiling: ', module_name
        sys.modules[module_name] = new_module
        new_module.__name__ = module_name
        new_module.__file__ = path
        exec module_code in new_module.__dict__
        if not hasattr(new_module, "__package__"):
            split = module_name.split('.', 1)
            if len(split) > 1:
                new_module.__package__ = split[0]
            else:
                print "No package available for: ", module_name
        return new_module
    
    def preprocess(self, source):
        for preprocessor in self.preprocessors:
            source = preprocessor.handle_source(source)
        return source
        
    def compile(self, source, filename=''):
        return compile(self.preprocess(source), filename, 'exec')         
        
        
class Dollar_Sign_Directive(object):
    """ Replaces '$' directive with pride.objects lookup. This
        facilitates the syntatic sugar $Component, which is
        translated to pride.objects['Component']. """
        
    def handle_source(self, source):
      #  _source = Parser.remove_comments(source)
      #  print _source
        return Parser.replace_symbol('$', source, "pride.objects['{}']", False, False)     
        
  
class Function_Inliner(object):

    def handle_source(self, source):
        delimiters = DELIMITERS + OPERATORS
        _source = Parser.replace_symbol('$', source, '{}')
        print source
        print _source
        bytecode = compile(_source, 'inline_test', 'exec')
        module = sys.meta_path[0].compile_module('', bytecode, '')
        sources = []
        for start, end in Parser.find_symbol('$', source):
            for end_of_symbol, character in enumerate(source[end:]):
                if character in delimiters:
                    break
            function_name = source[end:end + end_of_symbol + 1]
            print 'Function name: ', function_name, end, end + end_of_symbol + 1
            function_source = inspect.getsource(getattr(module, function_name))
            sources.append((function_name, Parser.extract_code(function_source)))
            
        for function_name, inline_source in sources:
            source = Parser.replace_symbol('$' + function_name, inline_source)
        print "Returning: ", source
        return source
        
        
class New_Keyword(object):
    
    def handle_source(self, source):
        pass
            
            
class AntipatternError(BaseException):
    meaning = "Source code error indicating poor design"
    

class Name_Enforcer(object):
    
    cache = {}
    
    def is_variable_name(self, token):
        if token in self.cache:
            return True
            
        if ' ' not in token:
            for character in special_symbols:
                if character in token:
                    break
            else:
                self.cache[token] = True
                return True        

    def handle_source(self, source): 
        strings = Parser.get_string_indices(source)
        source_pieces = []
        last_end = 0
        for _range in strings:
            source_pieces.append(source[last_end:_range[0]])
            last_end = _range[1]
        source_pieces.append(source[last_end:])
        _source = '\n'.join(source_pieces)
        for name in _source.split():
            print name
            if self.is_variable_name(name):            
                if len(name) < 3 or (name in string.letters and 
                                     name not in ('x', 'y', 'z', 't')):
                    raise AntipatternError("Short variable name '{}'".format(name))
                    
                _name =(name.replace('a', '').replace('e', '').replace('i', '')
                        .replace('o', '').replace('u', '').replace('y', ''))
                if _name == name:
                    raise AntipatternError("Encountered variable name without vowels '{}'".format(name))                   
        return source                 
                    
# for subcomponents
# cannot be in base.py because a reference to Config is needed in metaclass
def deep_update(d1, d2):
    for key, value in d2.items():
        if isinstance(value, dict):
            try:
                deep_update(d1[key], value)
            except KeyError:
                if key in d1:
                    raise
                d1[key] = value
        else:
            d1[key] = value

class Config(dict):
    """ A `dict` that does "deep" updates, i.e.
        nested dictionaries are updated instead of replaced.
        Is otherwise identical to a normal `dict`

        Used by the `subcomponents` mechanism. """

    def update(self, E=None, **kwargs):
        if E is not None:
            if hasattr(E, "keys"):
                deep_update(self, E)
            else:
                for k, v in E: # if E is a list of tuples, it overwrites
                    self[k] = value   # and does not update nested dicts
        for key, value in kwargs.items():
            self[key] = value        

# end code for subcomponents


class Interface(tuple):

    def __init__(self, args=tuple()):
        super(Interface, self).__init__()
        try:
            methods = args[0]
        except IndexError:
            methods = tuple()
            attrs = tuple()
        else:
            try:
                attrs = args[1]
            except IndexError:
                attrs = tuple()
        self.methods = methods
        self.attrs = attrs

    def __getitem__(self, key):
        if key == 0:
            return self.methods
        elif key == 1:
            return self.attrs
        else:
            raise IndexError()

    def __iadd__(self, rhs):
        return Interface((self[0] + rhs[0], self[1] + rhs[1]))

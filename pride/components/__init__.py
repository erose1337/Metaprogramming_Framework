# for subcomponent_kwargs
# cannot be in base.py because a reference to Config is needed in metaclass
def _update_dict(d1, d2):
    for key, value in d2.items():
        if isinstance(value, dict):
            try:
                _update_dict(d1[key], value)
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

        Used by the `subcomponent_kwargs` mechanism. """

    def update(self, E=None, **kwargs):
        if E is not None:
            if hasattr(E, "keys"):
                _update_dict(self, E)
            else:
                for k, v in E: # if E is a list of tuples, it overwrites
                    self[k] = value   # and does not update nested dicts
        for key, value in kwargs.items():
            self[key] = value
# end code for subcomponent_kwargs

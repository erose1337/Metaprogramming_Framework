# implement "pointers" in python by:
#
# - make pointerid attribute that is a descriptor
# - set the object that is pointed-to as the value read by the descriptor
# - have to declare pointers before/when the class is compiling
# - can have type checking

# move descriptor creation process into metaclass
import pride.components.base

def create_pointers(pointers):
    for pointer_id, pointer_type in pointers.items():
        pointer_name = "_pointer_{}".format(pointer_id)
        def _getter(self, _pointer_name=pointer_name):
            return getattr(self, _pointer_name)
        def _deler(self, _pointer_name=pointer_name):
            delattr(self, _pointer_name)

        if pointer_type == any:
            def _setter(self, value, _pointer_name=pointer_name):
                setattr(self, _pointer_name, value)
        else:
            def _setter(self, value, _pointer_name=pointer_name, _type=pointer_type):
                #assert isinstance(value, _type)
                if not isinstance(value, _type):
                    raise Warning("Tried to store value of type {} in pointer for type {}".format(type(value), _type))
                setattr(self, _pointer_name, value)
        yield pointer_id, property(_getter, _setter, _deler)

def create_pointers_to_base_object(pointers):
    for pointer_id, pointer_type in pointers.items():
        if pointer_type == any:
            pointer_type = pride.components.base.Base
        pointer_name = "_pointer_{}".format(pointer_id)
        def _getter(self, _pointer_name=pointer_name):
            try:
                return pride.objects[getattr(self, _pointer_name)]
            except AttributeError:
                raise Warning("Pointer '{}' value not set before pointer was accessed".format(_pointer_name[9:]))
        def _deler(self, _pointer_name=pointer_name):
            delattr(self, _pointer_name)
        def _setter(self, value, _pointer_name=pointer_name, _type=pointer_type):
            #assert isinstance(value, _type)
            if not isinstance(value, _type):
                raise Warning("Tried to store value of type {} in pointer for type {}".format(type(value), _type))
            setattr(self, _pointer_name, value.reference)
        yield pointer_id, property(_getter, _setter, _deler)

class Object(object):

    pointers = {"pointer1" : list, "pointer2" : any}
    inherited_attributes = ("pointers", )

    _vars = vars()
    for pointer_name, _property in create_pointers(pointers):
        _vars[pointer_name] = _property
    del _vars, pointer_name, _property


class Subclass(Object):

    pointers = {"subclass1" : Object}
    _vars = vars()
    for pointer_name, _property in create_pointers(pointers):
        _vars[pointer_name] = _property
    del _vars, pointer_name, _property


class PointerMetaclass(type):

    def __new__(cls, name, bases, attributes):
        print(name, attributes["pointers"])
        for pointer_name, _property in create_pointers_to_base_object(attributes["pointers"]):
            attributes[pointer_name] = _property
        return super(PointerMetaclass, cls).__new__(cls, name, bases, attributes)


class Object2(object, metaclass=PointerMetaclass):

    pointers = {"component" : pride.components.base.Base}
    inherited_attributes = ("pointers", )

class Object3(Object2):

    pointers = {"test3" : pride.components.base.Base}

o = Object2()
o.component = pride.components.base.Base()
print(o.component)

o3 = Object3()
o3.component = pride.components.base.Base()
o3.test3 = pride.components.base.Base()
print(o3.test3)
#s = Subclass()
#s.pointer1 = l1 = [1, 2, 3]
#assert s._pointer_pointer1 == l1, (s.pointer1, s._pointer_pointer1, l1)
#try:
#    s.pointer2
#except AttributeError:
#    # pointer unassigned
#    pass
#
#try:
#    s._pointer_subclass1
#except AttributeError:
#    # pointer not yet assigned
#    pass
#else:
#    print("Failure!")
#
##print "s.subclass1: ", s.subclass1
#try:
#    s.subclass1 = 1
#except Warning:
#    # pointer is Object type, cannot assign int
#    pass
#else:
#    raise Warning("Type checking Failure!")
#
#s.subclass1 = Object()
#assert hasattr(s, "_pointer_subclass1"), dir(s)
#
#s2 = Subclass2()
#try:
#    s2.component = 1
#except Warning:
#    pass
#else:
#    raise Warning("Base type checking failure!")
#
#b = pride.components.base.Base()
#s2.component = b
#print s2.component, b, s2.component is b

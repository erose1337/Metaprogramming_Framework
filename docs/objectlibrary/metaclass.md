metaclass
==============



Defaults
--------------

	No documentation available


Method resolution order: 

	(<class 'metaclass.Defaults'>,
	 <class 'metaclass.Inherited_Attributes'>,
	 <type 'type'>,
	 <type 'object'>)

Docstring
--------------

	 A descriptor object used by the Documented metaclass. Augments
        instance docstrings with introspected information


Method resolution order: 

	(<class 'metaclass.Docstring'>, <type 'object'>)

Documented
--------------

	 A metaclass that uses the Docstring object to supply
        abundant documentation for classes


Method resolution order: 

	(<class 'metaclass.Documented'>, <type 'type'>, <type 'object'>)

- **make_docstring**(attributes):

				No documentation available


Inherited_Attributes
--------------

	No documentation available


Method resolution order: 

	(<class 'metaclass.Inherited_Attributes'>, <type 'type'>, <type 'object'>)

Metaclass
--------------

	 A metaclass that applies other metaclasses. 
        
        Also Produces class dictionaries keyed by equivalent values.
        This makes mass attribute assignment slightly faster. 
        
        i.e.:
            
            {'attribute' : True, 'attribute2' : True, 'attribute3' : True}
            
        becomes:
            
            {True: ('attribute', 'attribute1', 'attribute2')}
            
        This is an optimization used to speed up Base.__init__


Method resolution order: 

	(<class 'metaclass.Metaclass'>,
	 <class 'metaclass.Documented'>,
	 <class 'metaclass.Parser_Metaclass'>,
	 <class 'metaclass.Method_Hook'>,
	 <class 'metaclass.Defaults'>,
	 <class 'metaclass.Inherited_Attributes'>,
	 <class 'metaclass.Site_Configuration'>,
	 <type 'type'>,
	 <type 'object'>)

- **remove_metaclass**(cls, metaclass):

				No documentation available


- **update_metaclass**(cls):

				No documentation available


- **insert_metaclass**(cls, metaclass, index):

				No documentation available


Method_Hook
--------------

	 Provides a hook for decorating methods for the new class. 


Method resolution order: 

	(<class 'metaclass.Method_Hook'>, <type 'type'>, <type 'object'>)

- 	No documentation available


Method resolution order: 

	(<class 'metaclass.alert_on_call'>, <type 'object'>)

- **get_method_name**(method):

				No documentation available


- **decorate**(cls, new_class):

				No documentation available


Parser
--------------

	 Faciltates automatically generated command line parsers. Parser
        instances are class attributes assigned by the Parser_Metaclass


Method resolution order: 

	(<class 'metaclass.Parser'>, <type 'object'>)

- **get_options**(self):

				No documentation available


- **get_arguments**(self):

				No documentation available


Parser_Metaclass
--------------

	 Provides a command line parser for a class based upon 
        the class.defaults dictionary


Method resolution order: 

	(<class 'metaclass.Parser_Metaclass'>, <type 'type'>, <type 'object'>)

- **make_parser**(new_class, name, modifiers, exit_on_help):

				No documentation available


- 

Runtime_Decorator
--------------

	 Provides the ability to call a method with a decorator, decorators,
        or monkey patch specified via keyword argument. This decorator
        inherits from object and utilizes the Documented metaclass.

        usage: wrapped_method(my_argument, decorator="decorators.Tracer")


Method resolution order: 

	(<class 'metaclass.Runtime_Decorator'>, <type 'object'>)

Site_Configuration
--------------

	No documentation available


Method resolution order: 

	(<class 'metaclass.Site_Configuration'>, <type 'type'>, <type 'object'>)

alert_on_call
--------------

	No documentation available


Method resolution order: 

	(<class 'metaclass.alert_on_call'>, <type 'object'>)

- **get_method_name**(method):

				No documentation available


copy
--------------

**copy**(x):

		Shallow copy operation on arbitrary Python objects.

    See the module's __doc__ string for more info.
    

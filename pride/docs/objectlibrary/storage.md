storage
==============



Persistent_Storage
--------------

	 Usage: 
            
        storage = pride.objects["/Python/Persistent_Storage"]
        
        storage["my_persistent_data"] = data
        or
        data = storage["my_persistent_data"]
        
        Acts like a dictionary, but stores data persistently. 
        Can store basic python objects, i.e. ints, floats, strings, sets, lists, and dicts
        
        Similar to anydbm:
            - Uses pride.functions.persistence instead of pickle for serialization (safer)
            - Stored in a sqlite3 database 
                - Less likely then anydbm to end up with a corrupted .db file


Instance defaults: 

	{'auto_commit': True,
	 'connection': None,
	 'cursor': None,
	 'database_name': '',
	 'deleted': False,
	 'detect_types_flags': 1,
	 'dont_save': False,
	 'parse_args': False,
	 'replace_reference_on_load': True,
	 'return_cursor': False,
	 'startup_components': (),
	 'text_factory': <type 'str'>,
	 'wrapped_object': None}

Method resolution order: 

	(<class 'storage.Persistent_Storage'>,
	 <class 'pride.objectlibrary.database.Database'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

test_Persistent_Storage
--------------

**test_Persistent_Storage**():

				No documentation available

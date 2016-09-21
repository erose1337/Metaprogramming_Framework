database
==============

 Provides a Object oriented interface for working with sqlite3 databases 

ArgumentError
--------------

	No documentation available


Method resolution order: 

	(<class 'pride.errors.ArgumentError'>,
	 <type 'exceptions.TypeError'>,
	 <type 'exceptions.StandardError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

Database
--------------

	 An object with methods for dispatching sqlite3 commands. 
        Database objects may be simpler and safer then directly
        working with sqlite3 queries. Note that database methods
        do not commit automatically.


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

	(<class 'database.Database'>,
	 <class 'pride.objectlibrary.base.Wrapper'>,
	 <class 'pride.objectlibrary.base.Base'>,
	 <type 'object'>)

- **update_table**(self, table_name, where, arguments):

				No documentation available


- **drop_table**(self, table_name):

		 Removes a table from the underlying sqlite3 database. Note
            that this will remove all entries in the specified table, and
            the data cannot be recovered.


- **insert_or_replace**(self, table_name, new_values):

				No documentation available


- **query**(self, table_name, retrieve_fields, where, group_by, having, order_by, distinct):

		 Retrieves information from the named database table.
            retrieve_fileds is an iterable containing string names of
            the fields that should be returned. The where argument
            is a dictionary of field name:value pairs. 


- **alter_table**(self, table_name, mode, argument):

		 Alters the specified table. Available modes are
            "ADD" and "RENAME", while argument should be 
            an additional field definition or new name. Added
            columns are appended. 


- **delete**(self):

				No documentation available


- **create_table**(self, table_name, fields, if_not_exists):

		 Creates a table in the underlying sqlite3 database. 
            fields is an iterable containing field names. The if_not_exists
            flag, which defaults to True, will only create the table
            if it does not exist already. 


- 	No documentation available


Method resolution order: 

	(<class 'sqlite3.IntegrityError'>,
	 <class 'sqlite3.DatabaseError'>,
	 <class 'sqlite3.Error'>,
	 <type 'exceptions.StandardError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

- **delete_from**(self, table_name, where):

		 Removes an entry from the specified table. The where
            argument is a dictionary containing field name:value pairs.


- **get_last_auto_increment_value**(self, table_name):

				No documentation available


- **open_database**(self, database_name, text_factory):

		 Opens database_name and obtain a sqlite3 connection and cursor.
            Database objects call this implicitly when initializing.
            Database objects wrap the connection and store the cursor
            as Database.cursor. 


- **on_load**(self, state):

				No documentation available


- **table_info**(self, table_name):

		 Returns a generator which yields field information for the
            specified table. Entries consist of the field index, field name,
            field type, and more.


- **insert_into**(self, table_name, values, columns, batch):

		 Inserts values into the specified table. The values must
            be the correct type and the correct amount. Value types
            and quantity can be introspected via the table_info method.


create_assignment_string
--------------

**create_assignment_string**(items):

				No documentation available


create_where_string
--------------

**create_where_string**(where):

		 Helper function used by Database objects 


test_db
--------------

**test_db**():

				No documentation available

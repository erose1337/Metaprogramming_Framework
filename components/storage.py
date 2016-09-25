import pride.components.database
import pride.functions.persistence

class Persistent_Storage(pride.components.database.Database):
    """ Usage: 
            
        storage = pride.objects["/Python/Persistent_Storage"]
        
        storage["my_persistent_data"] = data
        or
        data = storage["my_persistent_data"]
        
        Acts like a dictionary, but stores data persistently. 
        Can store basic python objects, i.e. ints, floats, strings, sets, lists, and dicts
        
        Similar to anydbm:
            - Uses pride.functions.persistence instead of pickle for serialization (safer)
            - Stored in a sqlite3 database 
                - Less likely then anydbm to end up with a corrupted .db file"""
            
    database_structure = {"Entries" : ("identifier BLOB PRIMARY_KEY UNIQUE", "entry_data BLOB")}
    primary_key = {"Entries" : "identifier"}
    default_entries = {"registered_users" : list}
    inherited_attributes = {"default_entries" : dict}
    
    def __init__(self, **kwargs):
        super(Persistent_Storage, self).__init__(**kwargs)
        for entry, value_callable in self.default_entries.items():
            if entry not in self:
                self[entry] = value_callable()
        
    def __getitem__(self, item):
        data = self.query("Entries", retrieve_fields=("entry_data", ), where={"identifier" : item})        
        if not data:
            raise KeyError("'{}' not in database".format(item))
        else:
            return pride.functions.persistence.load_data(data)
        
    def __setitem__(self, item, value):
        data = pride.functions.persistence.save_data(value)
        self.insert_or_replace("Entries", (item, data))

    def __delitem__(self, item):
        self.delete_from("Entries", where={"identifier" : item})
        
    
def test_Persistent_Storage():
    storage = Persistent_Storage()
    test_values = [0, 'a', '', None, 1.0, set(), dict(), list(), (1, 2, 3)]
    for count, value in enumerate(test_values):
        name = str(count)
        try:
            _value = storage[name]
        except KeyError:
            storage[name] = value
            _value = storage[name]
        assert value == _value
        del storage[name]    
        
        storage[name] = value
        storage[name] = "MODIFIED VALUE"
        assert storage[name] == "MODIFIED VALUE"
        
        
if __name__ == "__main__":
    test_Persistent_Storage()
    
import platform

import pride
import pride.components.base

if platform.system() == "Windows":
    import pride.functions.dpapi
    os_encrypt = pride.functions.dpapi.cryptData
    os_decrypt = pride.functions.dpapi.decryptData
else:
    def _not_implemented(*args):
        raise NotImplementedError("Encryption provider '{}' not implemented".format(platform.system()))
    os_encrypt = _not_implemented
    os_decrypt = _not_implemented

class Encryption_Service(pride.components.base.Base):

    defaults = {"pride_file_type" : "pride.components.fileio.Database_File",
                "os_file_type" : "pride.components.fileio.File"}
    
    verbosity = {"unit_test_pass" : 0}
    
    def save_to_file(self, filename, data, mode, file_system="pride", crypto_provider="pride"):            
        data = self.encrypt(data, crypto_provider)
        
        if file_system == "pride":
            file_object = self.pride_file_type
        elif file_system == "OS":
            file_object = self.os_file_type
                
        with self.create(file_object, filename, mode) as _file:
            _file.write(data)
                        
    def read_from_file(self, filename, file_system="pride", crypto_provider="pride"):
        if file_system == "pride":
            file_object = self.pride_file_type
        elif file_system == "OS":
            file_object = self.os_file_type
        else:
            raise ValueError("Unsupported file_system '{}'".format(file_system))
            
        with self.create(file_object, filename, 'rb') as _file:            
            data = _file.read()
        return self.decrypt(data, crypto_provider)                
                
    def encrypt(self, data, crypto_provider="session", entropy="\x00" * 16):        
        if crypto_provider == "OS":
            return os_encrypt(data, entropy)
        elif crypto_provider == "pride":
            return pride.objects["/User"].encrypt(data)
        elif crypto_provider == "session":
            return pride.objects["/Python/Session"].encrypt(data)
        else:
            raise ValueError("Invalid crypto_provider: '{}'; Supported: ('{}', '{}', '{}')".format(crypto_provider, "OS", "pride", "session"))
            
    def decrypt(self, data, crypto_provider="session", entropy="\x00" * 16):
        if crypto_provider == "OS":
            return os_decrypt(data, entropy)
        elif crypto_provider == "pride":
            return pride.objects["/User"].decrypt(data)
        elif crypto_provider == "session":
            return pride.objects["/Python/Session"].decrypt(data)
        else:
            raise ValueError("Invalid crypto_provider: '{}'; Allowed: ('{}', '{}', '{}')".format(crypto_provider, "OS", "pride", "session"))
            
def test_Encryption_Service():
    data = "Message!" * 2    
    storage = pride.objects["/Python/Encryption_Service"]    
    for provider in ("pride", "OS", "session"):
        encrypted_memory = storage.encrypt(data, provider)
        assert storage.decrypt(encrypted_memory, provider) == data
        
        filename = "__{}_unit_test".format(storage.reference)
        storage.save_to_file(filename, data, 'wb')
        assert storage.read_from_file(filename)    
    storage.alert("Test passed", level=storage.verbosity["unit_test_pass"])
    
if __name__ == "__main__":
    test_Encryption_Service()
    
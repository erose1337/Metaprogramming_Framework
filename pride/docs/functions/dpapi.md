dpapi
==============



ARRAY
--------------

**ARRAY**(typ, len):

				No documentation available


ArgumentError
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.ArgumentError'>,
	 <type 'exceptions.Exception'>,
	 <type 'exceptions.BaseException'>,
	 <type 'object'>)

Array
--------------

	XXX to be provided


Method resolution order: 

	(<type '_ctypes.Array'>, <type '_ctypes._CData'>, <type 'object'>)

BigEndianStructure
--------------

	Structure with big endian byte order


Method resolution order: 

	(<class 'ctypes._endian.BigEndianStructure'>,
	 <type '_ctypes.Structure'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

CDLL
--------------

	An instance of this class represents a loaded dll/shared
    library, exporting functions using the standard C calling
    convention (named 'cdecl' on Windows).

    The exported functions can be accessed as attributes, or by
    indexing with the function name.  Examples:

    <obj>.qsort -> callable object
    <obj>['qsort'] -> callable object

    Calling the functions releases the Python GIL during the call and
    reacquires it afterwards.
    


Method resolution order: 

	(<class 'ctypes.CDLL'>, <type 'object'>)

CFUNCTYPE
--------------

**CFUNCTYPE**(restype, *argtypes, **kw):

		CFUNCTYPE(restype, *argtypes,
                 use_errno=False, use_last_error=False) -> function prototype.

    restype: the result type
    argtypes: a sequence specifying the argument types

    The function prototype can be called in different ways to create a
    callable object:

    prototype(integer address) -> foreign function
    prototype(callable) -> create and return a C callable function from callable
    prototype(integer index, method name[, paramflags]) -> foreign function calling a COM method
    prototype((ordinal number, dll object)[, paramflags]) -> foreign function exported by ordinal
    prototype((function name, dll object)[, paramflags]) -> foreign function exported by name
    


CryptProtectData
--------------

**CryptProtectData**:

				No documentation available


CryptUnprotectData
--------------

**CryptUnprotectData**:

				No documentation available


DATA_BLOB
--------------

	No documentation available


Method resolution order: 

	(<class 'dpapi.DATA_BLOB'>,
	 <type '_ctypes.Structure'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

DWORD
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

DllCanUnloadNow
--------------

**DllCanUnloadNow**():

				No documentation available


DllGetClassObject
--------------

**DllGetClassObject**(rclsid, riid, ppv):

				No documentation available


GetLastError
--------------

**GetLastError**:

				No documentation available


HRESULT
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.HRESULT'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

LibraryLoader
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.LibraryLoader'>, <type 'object'>)

- **LoadLibrary**(self, name):

				No documentation available


LittleEndianStructure
--------------

	Structure base class


Method resolution order: 

	(<type '_ctypes.Structure'>, <type '_ctypes._CData'>, <type 'object'>)

LocalFree
--------------

**LocalFree**:

				No documentation available


OleDLL
--------------

	This class represents a dll exporting functions using the
        Windows stdcall calling convention, and returning HRESULT.
        HRESULT error values are automatically raised as WindowsError
        exceptions.
        


Method resolution order: 

	(<class 'ctypes.OleDLL'>, <class 'ctypes.CDLL'>, <type 'object'>)

PYFUNCTYPE
--------------

**PYFUNCTYPE**(restype, *argtypes):

				No documentation available


PyDLL
--------------

	This class represents the Python library itself.  It allows to
    access Python API functions.  The GIL is not released, and
    Python exceptions are handled correctly.
    


Method resolution order: 

	(<class 'ctypes.PyDLL'>, <class 'ctypes.CDLL'>, <type 'object'>)

SetPointerType
--------------

**SetPointerType**(pointer, cls):

				No documentation available


Structure
--------------

	Structure base class


Method resolution order: 

	(<type '_ctypes.Structure'>, <type '_ctypes._CData'>, <type 'object'>)

Union
--------------

	Union base class


Method resolution order: 

	(<type '_ctypes.Union'>, <type '_ctypes._CData'>, <type 'object'>)

WINFUNCTYPE
--------------

**WINFUNCTYPE**(restype, *argtypes, **kw):

				No documentation available


Win32CryptProtectData
--------------

**Win32CryptProtectData**(plainText, entropy):

				No documentation available


Win32CryptUnprotectData
--------------

**Win32CryptUnprotectData**(cipherText, entropy):

				No documentation available


WinDLL
--------------

	This class represents a dll exporting functions using the
        Windows stdcall calling convention.
        


Method resolution order: 

	(<class 'ctypes.WinDLL'>, <class 'ctypes.CDLL'>, <type 'object'>)

WinError
--------------

**WinError**(code, descr):

				No documentation available


c_bool
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_bool'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_buffer
--------------

**c_buffer**(init, size):

				No documentation available


c_byte
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_byte'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_char
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_char'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_char_p
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_char_p'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

- **from_param**:

				No documentation available


c_double
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_double'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_float
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_float'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_int
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_long'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_int16
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_short'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_int32
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_long'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_int64
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_longlong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_int8
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_byte'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_long
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_long'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_longdouble
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_double'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_longlong
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_longlong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_short
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_short'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_size_t
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_ssize_t
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_long'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_ubyte
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ubyte'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_uint
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_uint16
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ushort'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_uint32
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_uint64
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulonglong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_uint8
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ubyte'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_ulong
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_ulonglong
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ulonglong'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_ushort
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_ushort'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_void_p
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_void_p'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

- **from_param**:

				No documentation available


c_voidp
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_void_p'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

- **from_param**:

				No documentation available


c_wchar
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_wchar'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

c_wchar_p
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.c_wchar_p'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

- **from_param**:

				No documentation available


cast
--------------

**cast**(obj, typ):

				No documentation available


create_string_buffer
--------------

**create_string_buffer**(init, size):

		create_string_buffer(aString) -> character array
    create_string_buffer(anInteger) -> character array
    create_string_buffer(aString, anInteger) -> character array
    


create_unicode_buffer
--------------

**create_unicode_buffer**(init, size):

		create_unicode_buffer(aString) -> character array
        create_unicode_buffer(anInteger) -> character array
        create_unicode_buffer(aString, anInteger) -> character array
        


cryptData
--------------

**cryptData**(text, extraEntropy):

				No documentation available


decryptData
--------------

**decryptData**(cipher_text, extraEntropy):

				No documentation available


getData
--------------

**getData**(blobOut):

				No documentation available


memcpy
--------------

**memcpy**:

				No documentation available


py_object
--------------

	No documentation available


Method resolution order: 

	(<class 'ctypes.py_object'>,
	 <type '_ctypes._SimpleCData'>,
	 <type '_ctypes._CData'>,
	 <type 'object'>)

string_at
--------------

**string_at**(ptr, size):

		string_at(addr[, size]) -> string

    Return the string at addr.


test_crypt_decrypt
--------------

**test_crypt_decrypt**():

				No documentation available


wstring_at
--------------

**wstring_at**(ptr, size):

		wstring_at(addr[, size]) -> string

        Return the string at addr.

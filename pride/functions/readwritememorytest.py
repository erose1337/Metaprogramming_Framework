from ctypes import wintypes
import ctypes

rPM = ctypes.WinDLL('kernel32',use_last_error=True).ReadProcessMemory
rPM.argtypes = [wintypes.HANDLE,wintypes.LPCVOID,wintypes.LPVOID,ctypes.c_size_t,ctypes.POINTER(ctypes.c_size_t)]
rPM.restype = wintypes.BOOL
wPM = ctypes.WinDLL('kernel32',use_last_error=True).WriteProcessMemory
wPM.argtypes = [wintypes.HANDLE,wintypes.LPVOID,wintypes.LPCVOID,ctypes.c_size_t,ctypes.POINTER(ctypes.c_size_t)]
wPM.restype = wintypes.BOOL

def test_rPM_wPM():
    ADDRESS1 = 0x00E97074
    ADDRESS2 = ctypes.create_string_buffer(64)
    bytes_read = ctypes.c_size_t()
    print(rPM(PROCESS,ADDRESS1,ADDRESS2,64,ctypes.byref(bytes_read)))
    print(ctypes.get_last_error())
    
if __name__ == "__main__":
    test_rPM_wPM()
    
from libcpp.string cimport string


cdef extern from "paq9a.h":
    string compress_string(string&)
    string decompress_string(string&)


def compress(bytes data):
    cdef string s = data
    cdef bytes r = compress_string(s)
    return r
    

def decompress(bytes data):
    cdef string s = data[:len(data)]
    cdef bytes r = decompress_string(s)
    return r

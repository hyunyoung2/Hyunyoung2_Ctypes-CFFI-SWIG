import ctypes

mylib = ctypes.CDLL("./libflags.so")

original_string = "Hi C, I am from Python!"

mutable_string = ctypes.create_string_buffer(str.encode(original_string))

mylib.welcome_msg(mutable_string)

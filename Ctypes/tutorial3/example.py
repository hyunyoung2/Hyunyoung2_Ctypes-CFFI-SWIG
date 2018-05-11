import ctypes

mylib = ctypes.CDLL("./libflags.so")
mylib.welcome_msg("Hi C, I am from Python!")

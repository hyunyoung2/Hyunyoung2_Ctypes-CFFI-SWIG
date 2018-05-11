import ctypes

mylib = CDLL("./libflags.so")
mylib.welcome_msg("Hi C, I am from Python!")

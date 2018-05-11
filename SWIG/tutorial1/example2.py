# from _flags_wrap.so
import _flags_wrap
print(_flags_wrap.welcome_msg("Hi C, I am from Python"))

_flags_wrap.set_flag(1)
print(_flags_wrap.get_flag())

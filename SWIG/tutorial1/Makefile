# Step to build python wrapper - build-python-wrapper-so.sh
all:
	swig -python pyflags.i
	gcc -fPIC -c flags.c pyflags_wrap.c -I/usr/include/python3.5
	ld -shared flags.o pyflags_wrap.o -o _flags_wrap.so
clean:
	rm flags.o flags_wrap.py _flags_wrap.so pyflags_wrap.c pyflags_wrap.o 
	rm -rf __pycache__

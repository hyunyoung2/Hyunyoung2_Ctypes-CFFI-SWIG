all: test

clean:
	rm -f *.o *.so *.html

clib1.so: clib1.o
	gcc -shared -o libclib1.so clib1.o

clib1.o: clib1.c
	gcc -c -Wall -Werror -fpic clib1.c

test: clib1.so
	python ./callclib1.py

doc:
	markdown README.md > README.html
	firefox README.html

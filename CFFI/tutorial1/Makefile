all: point

clean:
	rm -f *.o *.so *.html _point.c

libpoint.so: Point.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^
	
point: libpoint.so
	./build_point.py
	./test_point.py
  
doc:
	pandoc README.md > README.html
	firefox README.html

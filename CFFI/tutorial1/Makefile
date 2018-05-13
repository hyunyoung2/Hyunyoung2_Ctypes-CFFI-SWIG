all: point

clean:
	rm -f *.o *.so *.html _point.c _line.c Line.h.preprocessed

libpoint.so: Point.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^
	
point: libpoint.so
	python3 build_point.py
	python3 test_point.py
  
doc:
	pandoc README.md > README.html
	firefox README.html

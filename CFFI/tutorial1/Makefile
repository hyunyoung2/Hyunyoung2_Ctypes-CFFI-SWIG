all: point

clean:
	rm -f *.o *.so *.html _point.c _line.c Line.h.preprocessed

libpoint.so: Point.o
	gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^
	
point: export LD_LIBRARY_PATH = $(shell pwd)
point: libpoint.so
	python3 build_point.py
	python3 testPoint.py
  
doc:
	pandoc README.md > README.html
	firefox README.html

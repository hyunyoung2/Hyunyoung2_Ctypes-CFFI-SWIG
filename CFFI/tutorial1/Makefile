all: point

clean:
  rm -f *.o *.so *.html _point.c _line.c Line.h.preprocessed

libpoint.so: Point.o
  gcc -shared $^ -o $@

%.o: %.c
	gcc -c -Wall -Werror -fpic $^


point: libpoint.so
	./build_point.py
	./testPoint.py
  
doc:
	pandoc README.md > README.html
	firefox README.html

# CFFI tutorial 1

 CFFI is better environment than Ctypes. 

 Let's see an example code explaining how to use CFFI to interface python with native library.
 
 The code is composed of a Point structure and functions using it.
 
```c
/* Point.h */
/* Simple structure for CFFI example */
typedef struct {
    int x;
    int y;
} Point;

/* point.c */
/* display a Point value */
void show_point(Point point){
   printf("Point in C is (%d, %d)\n", point.x point.y);
}

/* Increment a Point which was passed by value */
void move_point(Point point){
    show_point(point);
    point.x++;
    point.y++;
    show_point(point);
}

/* increment a Point which was passed by reference */
void move_point_by_ref(Point *point){
    show_point(*point);
    point->x++;
    point->y++;
    show_point(*point);
}

/* Return by value */
Point get_default_point(void) {
    static int x_counter = 0; 
    static int y_counter = 0; 
    x_counter++;
    y_counter--;
    return get_point(x_counter, y_counter);
}

Point get_point(int x, int y) {
    Point point = {x, y};
    printf("Return Point   (%d, %d)\n", point.x, point.y);
    return point;
}
```

Normally, CFFI has four mode. "ABI"  versus "API" with in-line or out-line mode. 

But I would deal with "API-out-line" mode. Basically "API" is more fast than "ABI"

To cap, you would make c source file using python.h so you can use the shared object as module on python. 

In other words. after writing cython code, and then you generate c source so creat shared object for python. 

the shared object behave like interface python with c function. 

CFFI automatically make c source file to wrap c functions to use on python code. 

Let's make the library to c interface. 

Basicall, When you use the CFFI, CFFI is used to generate the wrapped c source to be able to call in python with shared object. 

```python 
ffi = cffi.FFI()

with open(os.path.join(os.path.dirname(__file__), "point.h)) as f:
    ffi.cdef(f.read()) # here CFFI is using the cdef from cython.
 
ffi.set_source("_point",
    '#include "Point.h"', 
    libraries=["libpoint"], 
    library_dirs=[os.path.dirname(__file__),],
)

ffi.compile()
```


# Reference 

 - [Python's CFFI module](https://cffi.readthedocs.io/en/latest/index.html)
 
 - [Dan Bader's CFFI](https://dbader.org/blog/python-cffi)
 
 - [How to use libffi](https://eli.thegreenplace.net/2013/03/04/flexible-runtime-interface-to-shared-libraries-with-libffi/)

# CFFI tutorial 1

 CFFI is better environment than Ctypes. 

 Let's see an example code explaining how to use CFFI to interface python with native library.
 
 The code is composed of Point and Line structure. a Line structure has a start point and end point. 
 
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

Let's see the line structure and functions using it. 

```c
/* Line.h */
typedef struct {
    Point start; 
    Point end;
} Line;

/* Line.c */ 
void show_line(Line line){
    printf("Line in C  is (%d, %d) -> (%d, %d)\n", line.start.x, line.start.y, line.end.x, line.end.y);
}

void move_line_by_ref(Line *line){
    show_line(*line);
    move_point_by_ref(&line -> start);
    move_point_by_ref(&line -> end);
    show_line(*line);
}

Line get_line(void) {
    Line l = { get_default_point(), get_defaut_point() };
    return l;
}
```

Befor diving into CFFI, CFFI can be used in one of four mode, but in here I would deal with API level, i.e. it out-of-line mode.

When you use CFFI module, The LD_LIBRARY_PATH is needed because the CFFI module is going to be loading a library we have built in the local directory. 


 
 


# Reference 

 - [Python's CFFI module](https://cffi.readthedocs.io/en/latest/index.html)
 
 - [Dan Bader's CFFI](https://dbader.org/blog/python-cffi)
 
 - [How to use libffi](https://eli.thegreenplace.net/2013/03/04/flexible-runtime-interface-to-shared-libraries-with-libffi/)

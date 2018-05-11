# SWIG

In this time I will wrap c function with [SWIG](http://www.swig.org/). 

SWIG is a software development tool that connects programs written in C and C++ with a variety of high-level programming languages.

Frist of all, install SWIG on ubuntu:

> sudo apt install SWIG  

When you use SWIG, you need to a interface file called pyflags.i, i.e. the extension is normally **i**. which will be used by [SWIG](http://www.swig.org/)

```c
/* flags.c - Source file */
# include <stdio.h>
# inlcude "flags.h"

int gFlag = 0;

void welcome_msg(char *msg){
    printf("%s\n", msg);
    return;
}

int get_flag(){
    return flag;
}

void set_flag(int flag){
    gFlag = flag;
    return;
}

/* flags.h - Header file */
void welcome_msg(char *msg);
int get_flag();
void set_flag(int flag);
```

From now on, you have to write a interface file as shown below for the above c library. 

```
/* pyflags.i - interface file*/
% module flags_wrap
%{
#include "flags.h"
%}

%include "flags.h"
```

Let's type in commands to make output files \_flags\_wrap.so with input file pyflags.i. 

```shell
# Step to build python wrapper - build-python-wrapper-so.sh

swig -python pyflags.i
gcc -fPIC -c flags.c pyflags_wrap.c -l/usr/include/python3
ld -shared flags.o pyflags_wrap.o -o _flags_wrap.so
```

i.e. Let's see normally how to use SWIG.

```shell
$ cd <path-to-source>
$ swig -<wrap-language> <module-name>.i
$ gcc -c <module-name>.c <module-name>_wrap.c -I<path-to-wrap-language-headers>
$ ld -shared <module-name>.o <module-name>_wrap.o -o _<module-name>.so
```

Let's execute it on python interpreter.

```python
import flags_wrap
print(flags_wrap.welcome_msg("Hi C, I am from Python")

flag_wrap.set_flag(1)
print(flag_wrap.get_flag())
```

# Reference 

 - [SWIG](http://www.swig.org/)
 
 - [SWIG's tutorial](http://www.swig.org/tutorial.html)
 
 - [Another SWIG's reference](http://www.ittc.ku.edu/kusp/kusp_docs/kusp_swig_guide/index.html)

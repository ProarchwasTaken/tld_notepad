Greetings. This app is basically a Notepad clone written for the purpose 
of learning more about using Python and C++ together using pybind11. The 
app will be able to do a multitude of things like saving and opening 
files. 

The frontend is typically handled by Python by using the tkinter library,
while the backend code will be written in C++. The frontend access the
backend code though a compiled python module that's generated using 
pybind11 itself. That's personally how I believe it would work anyway.


# How to set up.
The first step is to generate the Makefile using cmake. You would have to
install pybind11 as a submodule. I think that process should be easy given
that there's already ".gitmodules" file when you cloned the repo. In the
cmake file, it is already expected that the pybind11 directory would be
located in ".extern" so you may have to create that directory first.

Sometimes you would have to specify which python interpreter to use. I've
encounter this problem while writing the cmake file, but I have a way to
fix it. Add this to your cmake command, and it should generate the
Makefile without issues.

```
-DPYTHON_EXECUTABLE="Path to python executable"
```

Final step is to go where ever you generated the Makefile, and compile
backend.cpp into a ".pyd" file. Then move it to the root of the project,
or the directory of which "main.py" is located. Run main.py and it should
work.

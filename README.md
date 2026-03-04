# PCL-Server
Python-C++-Linux-server

This is a test-project to explore creating a primarily C++-type server using a light Python-layer for the API process.
The reason for choosing C++ is its potential for faster and efficient data processing.
However, C++ has little framework support regarding server development.

Therefore, the idea is to use Python (Django in this case) for the basic server operations. The python server then taps into a C++ library for the data processing.

Pybind11 is using a binding between the c++ library files and the Python server.

The code is meant to be fully test-driven, and can be fully run by cmake.

Example of use:

```bash
git submodule init
git submodule update
mkdir build
cd build
cmake ..
make
ctest
cd ../server
python3 manage.py runserver
```



#include <pybind11/pybind11.h>
#include <iostream>


PYBIND11_MODULE(backend, m) {
  std::cout << "Tyler's Notepad - v1.0";
  m.doc() = "The backend code for the notepad application.";
}

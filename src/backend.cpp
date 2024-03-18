#include <pybind11/pybind11.h>


PYBIND11_MODULE(backend, m) {
  m.doc() = "The backend code for the notepad application.";
}

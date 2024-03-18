cmake_minimum_required(VERSION 3.10)
project("backend")

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
add_subdirectory(".extern/pybind11")

pybind11_add_module("backend" src/backend.cpp)
target_link_libraries("backend" PRIVATE -static -lpthread -static-libgcc -static-libstdc++)

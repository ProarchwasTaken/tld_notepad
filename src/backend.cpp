#include <pybind11/pybind11.h>
#include <iostream>
#include <fstream>
#include <string>

using std::string, std::ofstream, std::ifstream;
namespace py = pybind11;

string _current_path = "";


string getCurrentPath();
void setCurrentPath(string file_path, bool force);

void saveFile(string buffer);
string getFileContents();


PYBIND11_MODULE(backend, m) {
  std::cout << "Tyler's Notepad - v1.0\n";
  m.doc() = "The backend code for the notepad application.";

  m.def("saveFile", &saveFile, 
        "For saving the current buffer to the current path and\n"
        "filename. Should be called whenever the user clicks the\n"
        "'Save' or 'Save As' buttons.",
        py::arg("buffer"));

  m.def("getCurrentPath", &getCurrentPath,
        "Gets the current path and file name of which the buffer will\n"
        "be saved to. It starts empty and the frontend is responsible\n"
        "for filling it out when the file is saved.");

  m.def("setCurrentPath", &setCurrentPath,
        "For setting the current path and filename of which the buffer\n"
        "will be saved to. Should be called when the current_path is\n"
        "empty, or the user wants to save to a different file.",
        py::arg("file_path"), py::arg("force") = false);

  m.def("getFileContents", &getFileContents,
        "Opens a file from the current path and returns it's contents\n"
        "as a string. If the current_path is empty, an empty string\n"
        "will be returned instead.");
}


string getCurrentPath() { return _current_path; }

void setCurrentPath(string file_path, bool force) {
  if (file_path == "" && force == false) return;

  _current_path = file_path;
}


void saveFile(string buffer) {
  if (getCurrentPath() == "") {
    std::cout << "Path is empty! File saving aborted!\n";
    return;
  }

  std::cout << "Saving file to: " << getCurrentPath() << "\n";
  ofstream saved_file(getCurrentPath());
  saved_file << buffer;
  saved_file.close();
  std::cout << "Successfully saved file.\n";
}


string getFileContents() {
  if (getCurrentPath() == "") {
    std::cout << "Path is empty! Returning empty string.\n";
    return "";
  }

  std::cout << "Opening file: " << getCurrentPath() << "\n";
  ifstream file(getCurrentPath());

  string line;
  string file_contents = "";

  while (std::getline(file, line)) {
    file_contents += (line + "\n");
  }

  file.close();

  return file_contents;
}


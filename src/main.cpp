#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>

namespace py = pybind11;

double add(double a, double b) {
    return a + b;
}

PYBIND11_MODULE(my_module, m)
{
    m.def("add", &add, "Add two numbers");
}

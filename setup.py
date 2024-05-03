from glob import glob
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext

name = 'my_module'
__version__ = '0.0.1'

ext_modules = [
    Pybind11Extension(
        name,
        sorted(glob('src/main.cpp')),
        include_dirs=['src'],
        define_macros=[('VERSION_INFO', __version__)],
    ),
]

setup(
    name=name,
    version=__version__,
    description='A Python module with C++ code',
    ext_modules=ext_modules,
    cmdclass={'build_ext': build_ext},
    install_requires=['pybind11', 'numpy'],
    python_requires='>=3.6'
)

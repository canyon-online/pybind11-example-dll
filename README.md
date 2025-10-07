# pybind11-example-dll

A simple example project demonstrating how to use pybind11 to create Python bindings for C++ code that uses a separate DLL library.

## Overview

This project creates a Python module `example` that exposes C++ functions to Python. The project demonstrates:
- Building a shared library (DLL on Windows) with exported functions
- Creating pybind11 bindings that use the DLL functions
- Cross-platform compilation (Windows/Linux)
- Modern Python packaging with scikit-build-core

The module exposes three functions:
- `square()` - takes a number and returns its square
- `greet()` - takes a name string and returns a greeting
- `times_two()` - takes a number and returns it multiplied by 2

## Project Structure

```
pybind11-example-dll/
├── src/
│   ├── example/
│   │   ├── __init__.py             # Python package initialization
│   │   └── CMakeLists.txt          # Package-specific CMake config
│   ├── mylib/
│   │   ├── CMakeLists.txt          # Library-specific CMake config
│   │   ├── mylib.cpp                   # Shared library implementation
│   │   └── mylib.h                     # Shared library header with exports
│   └── example.cpp                 # C++ source with pybind11 bindings
├── extern/
│   └── pybind11/                   # pybind11 submodule (v3.0.1)
├── CMakeLists.txt                  # Main CMake build configuration
├── pyproject.toml                  # Python project configuration
└── README.md
```

## Requirements

- Python 3.9+
- CMake 3.18+
- Visual Studio 2022+ (on Windows) or GCC 4.8+/Clang 3.3+ (on Linux)
- Git (for submodules)

## Building

1. Clone the repository with submodules:
   ```bash
   git clone --recursive <repository-url>
   cd pybind11-example-dll
   ```

2. **Recommended: Using scikit-build-core (pip install)**
   ```bash
   pip install .
   ```

3. **Alternative: Direct CMake build**

   **Windows (Visual Studio):**
   ```bash
   mkdir build
   cd build
   cmake .. -G "Visual Studio 17 2022" -A x64
   cmake --build . --config Release
   ```

   **Linux/macOS:**
   ```bash
   mkdir build
   cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build .
   ```

The build creates:
- `mylib.dll/.so` - the shared library with core functionality
- `example.pyd/.so` - the Python extension module
- Python package installed to `site-packages/example/`

## Installation Structure

After installation, the package is organized as:
```
site-packages/
└── example/
    ├── __init__.py                 # Package initialization
    ├── example.so/.pyd             # Compiled pybind11 module
    └── mylib.dll/.so               # Shared library
```

## Usage

After installation, you can use the module:

```python
import example

# Square a number
result = example.square(5)
print(result)  # 25.0

# Greet someone
greeting = example.greet("World")
print(greeting)  # "Hello, World"

# Double a number
doubled = example.times_two(3.5)
print(doubled)  # 7.0
```

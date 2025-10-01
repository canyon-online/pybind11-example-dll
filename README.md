# pybind11-example-dll

A simple example project demonstrating how to use pybind11 to create Python bindings for C++ code that uses a separate DLL library.

## Overview

This project creates a Python module `example` that exposes C++ functions to Python. The project demonstrates:
- Building a shared library (DLL on Windows) with exported functions
- Creating pybind11 bindings that use the DLL functions
- Cross-platform compilation (Windows/Linux)

The module exposes three functions:
- `square()` - takes a number and returns its square
- `greet()` - takes a name string and returns a greeting
- `times_two()` - takes a number and returns it multiplied by 2

## Project Structure

```
pybind11-example-dll/
├── src/
│   ├── example.cpp                 # C++ source with pybind11 bindings
│   ├── mylib.cpp                   # Shared library implementation
│   └── mylib.h                     # Shared library header with exports
├── tests/
│   ├── __init__.py                 # Test package
│   └── test_example.py             # Tests for example module
├── extern/
│   └── pybind11/                   # pybind11 submodule
├── CMakeLists.txt                  # CMake build configuration
├── pyproject.toml                  # Python project configuration
├── pytest.ini                     # pytest configuration
├── requirements-test.txt           # Test dependencies
├── example.pyi                     # Type stubs
└── README.md
```

## Requirements

- Python 3.12+
- CMake 3.15+
- Visual Studio 2017+ (on Windows) or GCC/Clang (on Linux)
- Git (for submodules)

## Building

1. Clone the repository with submodules:
   ```bash
   git clone --recursive <repository-url>
   cd pybind11-example-dll
   ```

2. Configure and build with CMake:

   **Windows:**
   ```bash
   mkdir build
   cd build
   cmake .. -G "Visual Studio 17 2022" -A x64
   cmake --build . --config Release
   ```

   **Linux:**
   ```bash
   mkdir build
   cd build
   cmake .. -DCMAKE_BUILD_TYPE=Release
   cmake --build .
   ```

   Alternatively, you can use scikit-build-core:
   ```bash
   pip install scikit-build-core pybind11
   pip install .
   ```

The build creates two artifacts:
- `mylib.dll` (Windows) or `libmylib.so` (Linux) - the shared library
- `example.pyd` (Windows) or `example.so` (Linux) - the Python extension module

## Usage

After building, you can use the module:

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

## Testing

Install pytest and run the tests:

```bash
pip install -r requirements-test.txt
pytest tests/
```

The tests automatically handle path configuration to find the built modules in the correct build directory.

## Development

This project uses:
- **pybind11** for C++/Python bindings
- **scikit-build-core** for modern Python packaging
- **CMake** for build configuration with shared library support
- **pytest** for testing
- **GitHub Actions** for cross-platform CI (Windows/Linux)
- **Visual Studio Code** with CMake and Python extensions for development

The project includes:
- Cross-platform DLL export macros (`__declspec(dllexport/import)` on Windows, `__attribute__((visibility("default")))` on Linux)
- Type stubs (`example.pyi`) for better IDE support and type checking
- Automated testing on multiple platforms via GitHub Actions

## Architecture

The project demonstrates a common pattern where:
1. Core functionality is implemented in a shared library (`mylib`)
2. The shared library exports functions with proper platform-specific decorators
3. A pybind11 module (`example`) imports and wraps the library functions
4. Python code can call the wrapped functions seamlessly

This approach is useful for larger projects where you want to share C++ code between multiple Python extensions or other applications.

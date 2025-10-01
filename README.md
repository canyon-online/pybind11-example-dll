# pybind11-example

A simple example project demonstrating how to use pybind11 to create Python bindings for C++ code.

## Overview

This project creates a Python module `example` that exposes a C++ function `square()` to Python. The function takes a number and returns its square.

## Project Structure

```
pybind11-example/
├── src/
│   └── example.cpp                 # C++ source with pybind11 bindings
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
- Visual Studio 2017+ (on Windows)
- Git (for submodules)

## Building

1. Clone the repository with submodules:
   ```bash
   git clone --recursive <repository-url>
   cd pybind11-example
   ```

2. Configure and build with CMake:
   ```bash
   mkdir build
   cd build
   cmake .. -G "Visual Studio 17 2022" -A x64
   cmake --build . --config Release
   ```

   Alternatively, you can use scikit-build-core:
   ```bash
   pip install scikit-build-core pybind11
   pip install .
   ```

## Usage

After building, the `example.pyd` file will be created in the build directory:

```python
import example

# Square a number
result = example.square(5)
print(result)  # 25.0

result = example.square(2.5)
print(result)  # 6.25
```

## Testing

Install pytest and run the tests:

```bash
pip install -r requirements-test.txt
pytest tests/
```

## Development

This project uses:
- **pybind11** for C++/Python bindings
- **scikit-build-core** for modern Python packaging
- **CMake** for build configuration
- **pytest** for testing
- **Visual Studio Code** with CMake and Python extensions for development

The project includes type stubs (`example.pyi`) for better IDE support and type checking.

cmake_minimum_required(VERSION 3.15)
project(pybind11_example_dll LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_subdirectory(extern/pybind11)

add_library(mylib SHARED
    src/mylib.cpp
)
target_include_directories(mylib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_compile_definitions(mylib PRIVATE BUILDING_MYLIB)

pybind11_add_module(example
    src/example.cpp
)
target_link_libraries(example PRIVATE mylib)

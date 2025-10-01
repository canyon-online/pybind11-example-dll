cmake_minimum_required(VERSION 3.15...4.0)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(extern/pybind11)

add_library(mylib SHARED src/mylib.cpp)
target_include_directories(mylib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_compile_definitions(mylib PRIVATE BUILDING_MYLIB)

pybind11_add_module(example src/example.cpp)
target_link_libraries(example PRIVATE mylib)

install(TARGETS example LIBRARY DESTINATION .)
install(TARGETS mylib 
    RUNTIME DESTINATION .
    LIBRARY DESTINATION .
)

cmake_minimum_required(VERSION 3.18...4.0)
project(${SKBUILD_PROJECT_NAME} LANGUAGES CXX)
message(STATUS "Configuring ${SKBUILD_PROJECT_NAME}")

set(PYBIND11_FINDPYTHON ON)
add_subdirectory(extern/pybind11)
add_subdirectory(src/mylib)

target_compile_definitions(mylib PRIVATE BUILDING_MYLIB)
set_target_properties(mylib PROPERTIES
    RUNTIME_OUTPUT_DIRECTORY $<TARGET_FILE_DIR:example>
)

pybind11_add_module(example src/example.cpp)
target_include_directories(example PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)
target_link_libraries(example PRIVATE mylib)

install(TARGETS example LIBRARY DESTINATION .)
install(TARGETS mylib 
    RUNTIME DESTINATION .
    LIBRARY DESTINATION .
)

cmake_minimum_required(VERSION 3.18...4.0)
project(mylib LANGUAGES CXX)

add_library(mylib SHARED
    mylib.cpp
    mylib.h
)

if(MSVC)
    target_compile_definitions(mylib PRIVATE UNICODE _UNICODE)
endif()

target_compile_features(mylib PUBLIC cxx_std_20)

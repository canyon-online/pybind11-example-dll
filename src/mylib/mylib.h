#pragma once

#include <string>

#ifdef _WIN32
#ifdef BUILDING_MYLIB
#define MYLIB_API __declspec(dllexport)
#else
#define MYLIB_API __declspec(dllimport)
#endif
#else
#define MYLIB_API
#endif

MYLIB_API std::string greet(const std::string &name);
MYLIB_API double times_two(double x);

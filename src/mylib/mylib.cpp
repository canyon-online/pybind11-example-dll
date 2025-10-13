#include "mylib.h"
#include <string>
#include <sstream>

namespace mylib
{
    std::string greet(const std::string &name)
    {
        std::ostringstream os;
        os << "Hello, " << name;
        return os.str();
    }

    double times_two(double x)
    {
        return x * 2.0;
    }
} // namespace mylib

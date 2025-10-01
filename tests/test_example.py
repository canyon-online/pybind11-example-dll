import os
import sys

# Add the build directory to Python path
sys.path.insert(
    0, os.path.join(os.path.dirname(__file__), "..", "build", "Release")
)  # or "Debug"

import example


def test_square_with_valid_int_returns_square():
    result = example.square(2)
    assert result == 4.0


def test_square_with_valid_float_returns_square():
    result = example.square(2.0)
    assert result == 4.0

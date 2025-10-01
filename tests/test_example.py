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


def test_greet_returns_greeting():
    result = example.greet("World")
    assert result == "Hello, World"


def test_greet_with_empty_string():
    result = example.greet("")
    assert result == "Hello, "


def test_times_two_with_int():
    result = example.times_two(5)
    assert result == 10.0


def test_times_two_with_float():
    result = example.times_two(3.5)
    assert result == 7.0


def test_times_two_with_zero():
    result = example.times_two(0)
    assert result == 0.0

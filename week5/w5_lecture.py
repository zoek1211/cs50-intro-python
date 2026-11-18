# UNIT TESTS

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n

# main function is not automatically called when the file is imported
# so we need to call it explicitly
# this is a common practice in Python to avoid running code when the file is imported as a
if __name__ == "__main__":
    main()

# manal testing 

# corner cases
# what about 0? negative?

# make another file test_calculator.py

# assert kewyord
# assert that something is true
# if it is not true, raise an AssertionError

# this is test_calculator.py
from calculator import square 

def main():
    test_square()

# if there is an error in the square function, this will print an error message
# otherwise, it will not print anything
def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")
    
    # use assert keyword instead of if statements
    # assert that the square function returns the expected value
    # use try except to catch AssertionError
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared was not 9")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared was not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")

    
    
if __name__ == "__main__":
    main()

# AssertionError is raised if the condition is not met

# too many lines of code for test function
# tools like pytest 

import pytest

# no main function, no conditional just test function
def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0


# something else does try except for us and reports the errors
# pip install pytest

# run pytest in terminal
# pytest test_calculator.py


# break code into functions they are testable 

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")


# hello world
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    print("hello,", to) # testing this would not work because it doesn't return a value
    return f"hello, {to}" # this is better for testing more testable 

if __name__ == "__main__":
    main()

from hello import hello

def test_hello():
    assert hello("David") == "hello, David"


# packages are python modules that are organized inside a folder
# create __init__.py file in the folder
# can run a folder of tests 





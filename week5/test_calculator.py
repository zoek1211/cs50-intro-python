from calculator import square 

# def main():
#     test_square()

# # if there is an error in the square function, this will print an error message
# # otherwise, it will not print anything
# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")
    
#     assert square(2) == 4
#     assert square(3) == 9

#     # use assert keyword instead of if statements
#     # assert that the square function returns the expected value
#     # use try except to catch AssertionError
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
    
# if __name__ == "__main__":
#     main()

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

import pytest

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

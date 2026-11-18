#Lecture 3: Exceptions 

print("hello, world")

# unterminated string literal  
# syntax error happens before code runs, must be fixed by you 
# print("hello, world"

#runtime error happens while code is running

x = int(input("What's x? "))
print(f"X is {x}") # format string fstring

# What could go wrong?
# User inputs a string instead of an integer
# ValueError: invalid literal for int() with base 10: 'hello'
# program defensively handles this error
# keyword try and except

try:
    x = int(input("What's x? "))
    print(f"X is {x}")  # format string fstring
except ValueError:
    print("x is not an integer, please try again")

# figure out what kind of errors could happen and handle them

# best practice make few lines of code 
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer, please try again")

print(f"x is {x}")

# NaemeError: name 'x' is not defined
# name of variable is not defined if it is not defined in the try block

# order of operations
# int(input("What's x? ")) this creates value error
# no value assigned to x
# print(f"x is {x}") this creates name error

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer, please try again")
else:
    print(f"x is {x}")

# use loop to prompt user until they enter a valid integer

while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer, please try again")
    else:
        break  # exit the loop if no error

print(f"x is {x}")

# try till user enters a valid integer
# break out of the loop if no error
# else clause associated with try not 
# if there is no exception, then the else block is executed

# this works too but design is not as good
while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer, please try again")

print(f"x is {x}")


def main():
    x = get_int()  # call the function to get an integer
    print(f"x is {x}")  # print the value of x

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer, please try again")
        else:
            break
    return x

# use return to exit the function and return the value instead of break
def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer, please try again")
        else:
            return x # return the value if no error

# return stronger than break 
# break exits the loop, return exits the function
# return breaks and returns the value to the caller

# or do
def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer, please try again")

# which one is better?
# tightening up the code, fewer lines but less readable

main()

# pass simply ignnores the error

def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass # say nothing, ignore the error, doesn't print anything

# pythonic way to handle errors is to use try and except
# try to do something, if it fails, handle the error gracefully
# don't use pass unless you have a good reason to ignore the error

# reusable code using prompt 
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

# raise exceptions to hanlde errors 

# errors are inevitable, so handle them gracefully
# raise exceptions to signal that something went wrong
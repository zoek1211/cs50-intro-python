# cs50 introduction to python lecture 1
# functions, variables

# ask user for their name
print("Hello World")
name = input("What's your name? ")
print("hello, ")
print(name)
# type in one line
print("hello, " + name)

# pseudocode outline your program
# structure your to-do list 
"""
ask user for their name
say hello to user
"""

# mulfiple function arguments automatically inserts a space for you
print("multiple function arguments")
print("hello, ", name)
print("hello,", name)

# string in python is str

# python official documentation
# docs.pythong.org/3/library/functions.html

# python documentation for print
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=Flush)
# print function can take any # of objects
# separator default value single blank space when pass multiple arguments, separated by space
# end default value adds \n newline 

# override default  value so there is no new line at the end
print("override default behaviour")
# override end value
print("hello, ", end="")
print(name)
print("hello, ", end="???")
print(name)
# override separator value
print("hello,", name, sep="???")

# escape characters
print('hello, "freind"')
print("hello, \"friend\"")

# f-strings, format strings
print(f"hello, {name}")

# string methods
# if user types spaces in their input?
# remove whitespace from str
# strip function removes spaces in left and right, not between
# lstrip, rstrip
name = name.strip()

# equal sign assignment operator

# capitalize user's input
# capitalie only first letter
# Zoe kim
name = name.capitalize()
print(name)

# title based capitalization
# capitalize first letter of first word, second word... 
# Zoe Kim
name = name.title()
print(name)

# write in one line
name = name.strip().title()

name = input("What is your name? ").strip().title()

# split
# Split user's name into first name and last name
# split by white space
first, last = name.split(" ")
print(f"hello, {first}")

# integera and operators 
# +, -, *, /, %

# python supports interactive mode
# type python3 in terminal 
# >>>

# calculator
x = 1
y = 2

z = x + y

print(z)

# take user input to calculate 
x = input("What is x? ")
y = input("What is y? ")

# string concatenation
z = x + y 
print(z)

# convert str to int
z = int(x) + int(y)
print(z)

# do i need z variable?

# nest functions
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

# write in one line? not always 
print(int(input("What is x? ")) + int(input("What is y?")))

# floating point variables
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

# round to nearest integer
# python documentation 
# round(number[, ndigits])
# take one number as first argument
# [] in documentation means optional
# can specify number of digits by adding comma and number

z = round(x + y)
print(z)

# format like 1,000
print(f"{z:,}")

# division
# round two digits
z = round(x / y, 2) 
# print 2 digits in fstring
print(f"{z:.2f}")

# defining functions
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)

# write in one line
def hello(to):
    print("hello,", to)

name = input("What's your name? ")
hello(name)

# assign default value 
def hello(to="World"):
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)

# this prints
# hello world
# What's your name?
# hello, Zoe

# generally put main part of code at the top of your file
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

# scope
# vairable only existing in the context in which you defined it
# variable name only exists in main function

# return 
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()

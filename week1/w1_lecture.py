# lecture 1 conditionals
"""
conditionals allow your program to make decisions
as if your program has the choice between 
taking the left hand road or the right hand road
based upon certain conditions
"""
# set of operators that are used to ask mathematical qustions
# >, >=, <, <=, ==, !=

# if, elif, else 
# or, and 

# compare
x = int(input("What is x? "))
y = int(input("What is y? "))

if x < y: # boolean true/false 
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# improved asking in one line
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# further improved 
# remove or and simply ask in one question
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# == evaluates if what is on the left and right are equal to one another
if x == y: 
    print("x is equal to y")
else:
    print("x is not equal to y")

# input a score and get a grade
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score <70:
    print("Grade: D")
else:
    print("Grade: F")

# cleaner code
# python allows you to chain together operations and conditions
if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# cleaner, readable, succinct 
# elif makes it mutually exclusive 
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# parity: even or odd?
# modulo % operator: see if two numbers divide evenly or have a remainder
# eg. 4 % 2 is 0 
# a number is even when it is divisible by two with no remainder
x = int(input("What is x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# create a parity function
def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True # boolean starts with uppercase
    else:
        return False

# pythonic expressions only seen in python 
# return statement like a sentence in english
def is_even(n):
    return True if n % 2 == 0 else False

# refine even further
# evaluate what is happening within n % 2 == 0 
# as either true or false and return that to the main function
def is_even(n):
    return n % 2 == 0 

main()

# return a hogwarts house 
name = input("What's your name? ")

if name == "Harry":
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# improve using or
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# use match like switch statement
# map names to houses
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _: # whatever cas is not handled. like else
        print("Who?")

# make it concise
# use | like or 
# check for multiple values in the same case statement 
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
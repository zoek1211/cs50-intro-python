# lecture 2 loops 

i = 0
while i < 3:
    print("meow")
    i += 1 # each iteration update i value
    # python doesn't have ++ 

# use ctrl+c to get out of an infinite loop

# for loop iterates through a list of items
# i begins with 0, meow, assigned 1, meow, 2 assigned, meow
for i in [0, 1, 2]:
    print("meow")

# improve by using a range function
for i in range(3): 
    print("meow")

# pythonic improvement
# python needs i as a place to store the number of iteration of the loop
# but i is never used for any other purpose
# if variable has no other significance, 
# name variable as underscore _ 
for _ in range(3):
    ...

# possibilities within python 
# this prints meowmeowmoew
print("meow" * 3)

# print meow on separate lines 
# but extra blank line at the end
print("meow\n" * 3)

# remove the additional blank line 
print("meow\n" * 3, end="")

# improving with user input
# user input that matches expectation you have 
# promt the user for a number greater than 0
n = int(input("What is n? "))
if n < 0:
    n = int(input("What's n? "))
    if n < 0:
        ...

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue # continue to stay in this loop
    else:
        break # break out of a loop 

# improve redundancy of continue
# loop runs until n > 0. breaks when >0
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

# further improvement
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n #break out of loop, return value

def meow(n):
    for _ in range (n):
        print("meow")

main()

# list 
students = ["Hermione", "Harry", "Ron"]
# print out list
# index into list
print(students[0]) # count from 0
print(students[1])
print(students[2])

# use for loop to iterate over a list
# don't use _ when variable is explicitly used 
for student in students:
    print(student)

# use range in a for loop, len function
for i in range(len(students)):
    print(i + 1, student[i]) 

# dictionaries associate one value with another
# associate keys with values 
students = {
    "Hermione": "Gryffidor", 
    "Harry": "Gryffindor", 
    "Ron": "Gryffindor", 
    "Draco": "Slytherin"
}

print(students["Hermione"]) # print value "Gryffindor"

for student in students:
    print(student, students[student], sep=", ") # print the keys, values
# print Hermione, Gryffindor

# List of dictionaries
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]
# keyword None absence of value 

# print names, houses, patronus
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")


# mario game
# jumping over bricks
print("#")
print("#")
print("#")

# can be written as
for _ in range(3):
    print("#")

# also like this
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        # print("#")
        print("#\n" * height, end="")

# print a row horizontally
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

# implement both rows and columns
def main():
    print_square(3)

def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="") # end="" prevents new line
        # after printing all bricks in row, print new line
        print()# print blanck line

# further abstract
def print_square(size):
    for i in range(size):
        print("# " * size) # print with no arguments, automatically adds new line



def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)
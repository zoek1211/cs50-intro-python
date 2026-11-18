# file i/o 



names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

# clean it up a bit
for _ in range(3):
    names.append(input("What's your name? "  ))

# sort them alphabetically
for name in sorted(names):
    print(f"hello, {name}")

# save names in a file
name = input("What's your name? ")
# open a file for writing 
# "w" means write mode, will overwrite existing file
file = open("names.txt", "w")
file.write(name)
file.close

file = open("names.txt", "a") # "a" means append mode
file.write(f"{name}\n")

# keyword with open
# instead of file=open, use with open
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# read from a file
with open("names.txt", "r") as file: # "r" means read mode
    lines = file.readlines() # read all lines into a list

for line in lines:
    print("hello, ", line.strip()) # strip() removes whitespace/newline characters
    # rstrip removes only right side whitespace

# alternative iterate over file object directly
# but can't sort it this way
with open("names.txt", "r") as file:
    for line in file: # iterate over lines in the file
        print("hello, ", line.rstrip())

# read names into a list and sort them
names = []

# don't have to explicitly say "r" for read mode, it's the default
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

# sort them alphabetically
for name in sorted(names):
    print(f"hello, {name}")

# reverse sort
for name in sorted(names, reverse=True):
    print(f"hello, {name}")

# sort more simply
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# we want to add houses to names in a file
# use csv file comma separated values
# parse a csv file 
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # split into a list at each comma
        print(f"{row[0]} is in {row[1]}") # row is a list with two values [0] is the first element [1] is the second element


# can also use two variables 
# we know there are two values in each row when split into a list at each comma
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",") 
        print(f"{name} is in {house}")


# store formatted strings in a list
students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}") # append a formatted string to the list

for student in sorted(students):
    print(student)

# create a dictionary that stores names as keys and houses as values
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student) # append a dictionary to the list

for student in students:
    print(f"{student['name']} is in {student['house']}") # use single quotes for dictionary keys inside f-strings


# do it all at once
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house} # create a dictionary with two key-value pairs
        students.append(student)

for student in sorted(students):
    print(f"{student['name']} is in {student['house']}")

# function to get name from student dictionary
def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"] 

# function as argument to sorted as key
# sorted funcion uses the get_name function to extract the name from each student dictionary
# and sorts the list of dictionaries based on those names
for student in sorted(students, key=get_name): # sort by name using the get_name function
    print(f"{student['name']} is in {student['house']}")

# sort by house
for student in sorted(students, key=get_house): # sort by name using the get_name function
    print(f"{student['name']} is in {student['house']}")


# tighthen the code
# use lambda function instead of defining a separate function
# anonymous function defined using the lambda keyword
# lambda function takes a student dictionary as input and returns the value associated with the "name"
# use lambda when you want to pass a simple function as an argument to another function
for student in sorted(students, key=lambda student: student["name"]): # sort by name using a lambda function 
    print(f"{student['name']} is in {student['house']}")

# what if there are two commas in one line how do we split it then?

# python library to read and write csv files
# module called csv
# docs.python.org/3/library/csv.html
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file) # create a csv reader object
    for name, home in reader: # iterate over reader instead of a file
        students.append({"name": name, "home": home}) # row is a list of values in each row

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# when the first line of csv file contains headers
# use dictionary reader instead of reader
# access to values by column names instead of index
# reader returns lists, DictReader returns dictionaries
with open("students.csv") as file:
    reader = csv.DictReader(file) # create a csv reader object
    for row in reader: # iterate over reader instead of a file
        students.append({"name": row["name"], "home": row["home"]}) # row is a list of values in each row

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


name = input("What's your name? ")
home = input("Where's your home? ")

with open(students.csv, "a") as file: # append mode
    writer = csv.writer(file) # create a csv writer object
    writer.writerow([name, home]) # write a row to the csv file


with open(students.csv, "a") as file: # append mode
    writer = csv.Dictwriter(file, fieldnames=["name", "home"]) # write a dictionary to a csv file
    writer.writerow({"name": name, "home": home}) # write a row to the csv file


# pillow library for image processing
# pillow.readthedocs.io


import sys
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg) # open an image file
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=images[1], duration=200, loop=0
)
# ## libraries, modules

# ## random.py module

# ## python documentation: https://docs.python.org/3/library/random.html

# # import keyword 

# # random.choice(seq)
# # function exsits in random module 
# # seq for sequence, can be a list, tuple, string

# # only import the random module 
# import random  

# coin = random.choice(["heads", "tails"]) 
# print(coin)

# # alternative way to import 
# from random import choice 
# coin = choice(["heads", "tails"])


# number = random.randint(1, 10)  # inclusive of both ends
# print(number)

# # random.shuffle shuffles a list 
# cards = ["jack", "queen", "king"]
# random.shuffle(cards)
# print(cards)

# # print one at a time
# for card in cards:
#     print(card)


# # statistics library
# import statistics

# print(statistics.mean([100, 90]))


# # command line arguments
# # allows you to provide arguments to a Python script when you run it from the command line
# # sys module

# import sys 

# print("helo, my name is", sys.argv[1]) 
# # write python name.py David in the command line
# # sys.argv[0] is the name of the file executing followed by the arguments
# # sys.argv[1] is the first argument, sys.argv[2] is the second argument, and so on

# try:
#     print("helo, my name is", sys.argv[1])
# except IndexError:
#     print("too few arguments")



# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")
# else:
#     print("Hello, my name is", sys.argv[1])

# # full name type "David Miller"

# # Check for errors 
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
#     print("Too many arguments")

# # PRint name tags
# print("Hello, my name is", sys.argv[1])

# # sys.exit
# if len(sys.argv) < 2:
#     sys.exit("Too few arguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arguments")

# print("Hello, my name is", sys.argv[1])


# for arg in sys.argv:
#     print("hello, my name is", arg)

# # slices of a subset of a list
# # specify a range of indices
# # use [:-1] to exclude the last element
# for arg in sys.argv[1:]:
#     print("hello, my name is", arg)

# # packages are third party libraries that can be installed and used in Python
# # pypi website: https://pypi.org/
# # cowsay package pypi.org/project/cowsay/
# # pip program to install packages

# import cowsay
# import sys

# # cow
# if len(sys.argv) == 2:
#     cowsay.cow("hello, " + sys.argv[1])

# # trex
# if len(sys.argv) == 2:
#     cowsay.trex("hello, " + sys.argv[1])


# APIs 
# third party services that provide data or functionality over the internet

# requests library 
# pip install requests
# pypi.org/project/requests/

# https://itunes.apple.com/search?entity=song&limit=1&term=weezer

# json language agnostic format for data exchange 

import requests
import sys

# if len(sys.argv) != 2: # if the user does not provide exactly one argument (name of file, band)
#     sys.exit() # exit the program

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]) # let user provide a band name

# # print(response.json()) # print the response in json format

# # format data clearly
# # docs.python.org/3/library/json.html
# import json # comes with python

# print(json.dumps(response.json(), indent=2)) # format nicely indent two places 



# if len(sys.argv) != 2: # if the user does not provide exactly one argument (name of file, band)
#     sys.exit() # exit the whole program

# response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # let user provide a band name

# o = response.json() # convert response to json format
# for result in o["results"]: # iterate over the results
#     print(result["trackName"]) # print the track name



# create own library 

def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")


main()

import sys 

from sayings import hello
if len(sys.argv) == 2:
    hello(sys.argv[1])

if __name__ == "__main__":
    main()

# __name__ is a special variable in Python that represents the name of the current module.
# when you run a file from command line, Python sets __name__ to "__main__" for that file.
# when you import a file as a module in another file, Python sets __name__ to the name of that module.
# this allows you to write code that can be run as a script or imported as a module without executing certain parts of the code when imported.
# by using if __name__ == "__main__":, you can ensure that certain code only runs when the file is executed directly, and not when it is imported as a module in another file.
# this is useful for testing or providing example usage of the module without affecting its functionality when imported elsewhere.


# style guide # PEP 8
# https://peps.python.org/pep-0008/

# indentation
# tabs or spaces?
# maximum line length 
# blank lines
# imports 

# pylint 
# pip install pylint
# pycodestyle.pycqa.org

# pycodestyle formerly known as pep8
# pycodestyle.pycqa.org

# black 
# pip intall black
# black.readthedocs.io

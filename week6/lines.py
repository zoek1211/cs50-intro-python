import sys
import os

def main():
    # check if correct number of command-line arguments are provided
    if len(sys.argv) != 2:
        sys.exit("too few command-line arguments")

    # get the filename from command-line argument
    # argv[1] is the first argument after the script name
    filename = sys.argv[1] 

    # check if the file has a .py extension
    if not filename.endswith(".py"):
        sys.exit("not a Python file")
    
    # try to open file
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("file does not exist")
    
    # count lines of code
    count = 0
    for line in lines:
        stripped = line.lstrip() # remove leading whitespace

        # skip blank lines
        if stripped == "" or stripped.startswith("#"):
            continue

        count += 1
    
    print(count)


if __name__ == "__main__":
    main()
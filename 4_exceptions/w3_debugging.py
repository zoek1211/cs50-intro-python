# debugging
# print a pyramid of height n

def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print(i, end=" ") # print the current row number
        print("#" * (i + 1)) # start from 0 so i+1 is the number of hashes to print

# python idiom used to run the main function
# this allows the main function to be run when the script is executed directly
# but not when it is imported as a module in another script
# this is a common practice in Python to avoid running code when the module is imported
# it is a way to organize code and make it reusable
# it allows the script to be run as a standalone program
if __name__ == "__main__":
    main()


# built in debugger 

# breakpoints pause the program at a certain point
# step through the code line by line

# step into a function to see what it does
# step over a function to skip it and continue with the next line
# variables are shown in the debugger
# debugger shows variables and their values

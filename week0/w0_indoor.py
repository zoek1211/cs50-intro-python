"""
promt the user for input and then output the same input in lowercase
punctuation and white space should be outputted unchanged
prompt the user the explicitly, by passing a str of your own as an argument to input
"""

def main():
    user_input = str(input("Enter a string: "))
    return user_input.lower()

print(main())
# promt the user input then output the same input,
# replacing each space with ... (i.e., three periods)

def main():
    user_input = input("Enter a string: ")
    return user_input.replace(" ", "...")

print(main())
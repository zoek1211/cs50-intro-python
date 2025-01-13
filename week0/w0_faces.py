# implement a function called convert that accepts a str as input
# and returns that same input with any :) converted to 🙂
# and any :( converted to 🙁
# all other text should be returend unchanged
# then, implement a function called main that prompts the user for input,
# calls concvert on that input, and prints the result
# prompt the user explicitly, by passing a str as an argument to input
# call main at the bottom of your file

def convert(input):
    if ":)" in input:
        return input.replace(":)", "🙂")
    elif ":(" in input:
        return input.replace(":(", "🙁")

def main():
    user_input = str(input("Enter a string: "))
    print(convert(user_input))


main()
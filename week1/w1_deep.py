# prompt the user for answer to the great question of life, the universe and everything
# output yes if the user inputs 42 (case-insensitively) or forty-two or forty two
# otherwise output no

# using if else
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.casefold()

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")
    
main()

# using match 
def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.casefold()

    match answer:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")

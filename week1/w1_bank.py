# promt the user for a greeting
# if the greeting starts with "hello" output $0
# if the greeting starts with an "h" but not "hello", output $20
# otherwise, output $100
# ignore white space in the user's greeting
# treat the user's greeting case insensitively

def main():
    greeting = input("Hello! ").strip().casefold()

    if greeting.startswith("hello"):
        print("$0")
    elif greeting.startswith("h"):
        print("$20")
    else:
        print("$100")

main()
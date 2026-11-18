def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n + n

# main function is not automatically called when the file is imported
# so we need to call it explicitly
# this is a common practice in Python to avoid running code when the file is imported as a
if __name__ == "__main__":
    main()

# break code into functions they are testable 
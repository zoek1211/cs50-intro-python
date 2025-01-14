# prompt the user for an arithmetic expression
# and then calculate and output the result as a floating point value formatted to one decimal place
# assume user input will be formatted as x y z
# with one space between x, y, and z 
# x is an integer
# y is +, -, * or /
# z is an integer

def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    x = int(x)
    z = int(z)

    if y == "+":
        answer = float(x + z)
    elif y == "-":
        answer = float(x - z)
    elif y == "*":
        answer = float(x * z)
    elif y == "/":
        answer = float(x / z)
    else:
        print("Please enter a valid expression")
    
    print(f"{answer:.1f}")

main()
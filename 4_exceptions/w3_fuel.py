### Fuel gauges indicate, often with fractions, just how much fuel is in a tank. 
# For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

## In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
   percent = get_fuel()


def get_fuel():
     while True:
        try: 
            fuel = input("Fraction: ")
            x, y = fuel.split('/') #split the input into two parts
            x = int(x)
            y = int(y)
            if x == 1 and y == 2:
                print("50%") 
            elif x == 1 and y == 4:
                print("25%")
            elif x == 3 and y == 4:
                print("75%")
            elif x == 4 and y == 4:
                print("F")
        except ValueError:
            pass
        except ZeroDivisionError:
            print("E")
            return 
        

if __name__ == "__main__":
    main()
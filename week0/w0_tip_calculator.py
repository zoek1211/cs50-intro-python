# calculate the amount of tip you want to leave to your server

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

# accept a string as input (formatted as $##.##)
# remove the leading $
# return the amoount as a float 
def dollars_to_float(d):
    d = float(d.strip("$"))
    print(d)
    return d

# accept string as input (formatted as ##%)
# remove the % 
# return the percentage as a float 
def percent_to_float(p):
    return float(p.strip("%"))/100

main()
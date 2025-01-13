"""
implement a program that prompts the user for mass as an integer (in kilograms)
and then outputs the equivalent number of joules as an integer
assume that the user will input an integer
"""

mass = int(input("Enter Mass in kilograms: "))
cSpeed = 300000000
energy = mass * cSpeed ** 2
print("Energy:", energy)
#Coded by AbrahamAdeboye (Elitepreneur)
#Modules
from math import *  # This is simply to import all functions from a python Mathematics module.




# variables
x = 4
y = 8
z = 3
a = 10

print("In this program file, we have four variables and we are gonna perform different sums operation on them.")
print("The variables are as follows: x = 4, y = 8, z = 3 and a = 10")

# Additions

print("Starting with additions, lets add 'a' with 'y'.")
additions = (y + a)
additions = additions.__str__()
print("Which is " + additions)

# Subtraction
print("We will subtract 'z' from 'x'.")
subtraction = x - z
subtraction = subtraction.__str__()
print("Answer is " + subtraction)

# Multiplication
print("Moving on with multiplication.")
multiplication = x * y
multiplication = multiplication.__str__()
print("Multiplying 'x' and 'y' will give us " + multiplication)

# Division
print("and the division goes with 'y' divided by 'x'.")
division = y / x
division = division.__str__()
print("And that will be 8 divided by 4 which is " + division)


# Modulus
print("And lastly, we will be treating Modulus commonly know as Mod.")
print("Let's just use 'a' and 'z' in this case.")
mod = a % z
mod = mod.__str__()
print("Which will be 10 mod 3.")
print("Answer is " + mod + ".")
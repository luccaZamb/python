from math import hypot
cop = float(input("Length of the opposite leg: "))
cadj = float(input("Length of adjacent leg: "))
hip = hypot(cop, cadj)
print(f"The value of the hypotenuse is {hip:.2f}")
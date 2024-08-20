from math import trunc

num = float(input("Write a number: "))
print(f"The number you wrote is {num} and it's entire portion is {trunc(num)}")

# tried with the :.0f formatation but if you put a ex:8.99999 it will make it 9 
# so you need to import the trunc function or make the int(num)
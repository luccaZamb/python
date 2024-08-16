# The excise was with a lot of print() so I tried to make a for function to make it cleaner

x = int(input("Write a number to see it's multiplication table: "))
print("-----------")
for y in range(1, 11):
    z = x*y
    print(f"{x} x {y:2} = {z}")
print("-----------")
import math

num = int(input("Write a number:"))
d = num * 2
t = num * 3
sqrt_root = math.sqrt(num)
# Used the \n to break the line and used the f in the beginning of the print line to format cause I belive this way is cleaner than the .format one
print(f"The double of {num} is {d}. \nThe triple of {num} is {t}. \nThe square root of {num} is {sqrt_root:.2f}.")


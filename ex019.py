import random
# s1 = input("First student: ")
# s2 = input("Second student: ")
# s3 = input("Third student: ")
# s4 = input("Fourth student: ")

# std = [s1, s2, s3, s4]

std = []

for x in range(1, 5):
    s1 = input(f"student number {x}: ")
    std.append(s1)

cho = random.choice(std)

print(f"The chosen one is {cho}!")
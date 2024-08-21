import random

std = []

for x in range(1, 5):
    s1 = input(f"student number {x}: ")
    std.append(s1)

random.shuffle(std)

print(f"the order of presentation will be... \n{std}!")
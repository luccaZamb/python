import time
name = input("Write your full name: ").strip()
up = name.upper()
low = name.lower()
qty = len(name.replace(" ", ""))
first = name.split()

print("Analyzing your name...")
time.sleep(3)
print(f"Your name in uppercase is {up}!\nYour name in lowercase is{low}!\nYour name has {qty} letters in total!\nYour first name is {first[0]} and it has {len(first[0])} letters!")
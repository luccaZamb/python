from time import sleep
num = int(input("Write a number: "))

print(f"Analyzing the number {num}...")
sleep(2)
print(f"Unit: {num // 1 % 10}\nTen: {num // 10 % 10}\nHundred: {num // 100 % 10}\nThousand: {num // 1000 % 10}")
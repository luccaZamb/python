g1 = float(input("Write the first grade:"))
g2 = float(input("Write the second grade:"))

avg = (g1+g2)/2

#Added a IF function just 4 fun
if avg >= 6.950:
    final = "Approved!"
else:
    final = "Failed!"

print(f"The average between {g1} and {g2} is {avg:.1f}! \nResult:{final}")

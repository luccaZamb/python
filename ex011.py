wth = float(input("Width of the wall: "))
hgt = float(input("Height of the wall: "))

sqrm = wth*hgt
# in this exercise, the qty to paint the wall was 1L to 2m²
paint = sqrm/2
print(f"Your wall has {wth}x{hgt}, and the area is {sqrm}m² \nTo paint this wall you will need {paint}L of Paint")
from math import sin, cos, tan, radians

num = float(input("Write the angle wanted: "))
ang = radians(num)
cosi = cos(ang)
sine = sin(ang)
tang = tan(ang)

print(f"The angle of {num} has the sine of {sine:.2f} \nThe angle of {num} has the cosine of {cosi:.2f}\n The angle of {num} has the tangent of {tang:.2f}")
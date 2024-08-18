# the exercise was just to turn Celsius in Fahrenheit but I made a way so the user can chose wich scale he wants.
# the exercise answer is commented after the code

temp = float(input("Write the temperature: "))

type = input("Write the scale you want \nEx: C or Celsius, F or Fahrenheit, K or Kelvin ")

if type=="C" or type=="c" or type=="Celsius" or type=="celsius":
    fah = temp*(5/9)+32
    kel = temp+273.15
    print(f"The temperature of {temp}°C is iqual to {fah:.3f}°F and {kel}°K!")
elif type=="F" or type=="f" or type=="Fahrenheit" or type=="fahrenheit":
    cel = (temp-32)*(5/9)
    kel = ((temp-32)*(5/9))+273.15
    print(f"The temperature of {temp}°F is iqual to {cel:.3f}°C and {kel:.3f}°K!")
elif type=="K" or type=="k" or type=="Kelvin" or type=="elvin":
    cel = temp-273.15
    fah = (temp-273.15)*9/5+32
    print(f"The temperature of {temp}°K is iqual to {cel:.2f}°C and {fah:.2f}°F!")
else:
    print("TYPE ERROR!\nTry Again with one of the following temperature scale type: C or Celsius, F or Fahrenheit, K or Kelvin")




# cel = float(input("Write the temperature in °C: "))
# fah = cel*1.8+32
# kel = cel+273

# print(f"The temperature of {cel}°C is iqual to {fah}°F and {kel}°K!")
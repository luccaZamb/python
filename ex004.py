import time

v = input("Type something:")
print("Here is the description of the reported value:")
time.sleep(2)
print("Loading...")
time.sleep(2)
print("The type of this value is:", type(v))
print("Has only spaces?", v.isspace())
print("Is it a number?", v.isnumeric())
print("Is it alphabetic?", v.isalpha())
print("Is it alphanumeric?", v.isalnum())
print("Is it in uppercase?", v.isupper())
print("Is it in lowercase?", v.islower())
print("Is it capitalized?", v.istitle())
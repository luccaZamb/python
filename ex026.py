frase = input("Write something: ").lower().strip()
print(f"The letter A appears {frase.count("a")} times!")
print(f"The letter A appears for the first time in the position {frase.find("a")+1}!")
print(f"The letter A appears for the last time in the position {frase.rfind("a")+1}!")

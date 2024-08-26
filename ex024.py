city = input("City you where born: ").strip().lower()
# print(city[:5] == "santo")
if city[:5] == "santo" or city[:6] == "santos":
    print(True)
else:
    print(False)
# Maybe I could make it a little cleaner but it does the job :D

m = float(input("Write a distance in meters: "))

km = m/1000
hm = m/100
dam = m/10
cm = m*100
mm = m*1000

print(f"Your metric in meters is equal to: \n{km} Km \n{hm} hm \n{dam} dam \n{cm} cm \n{mm} mm")
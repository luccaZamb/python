# the exercise gave a fixed R$60 per day and a R$0.15 per Km. 
# To make the code better, I created 2 more variables so the price is not fixed anymore

days = int(input("Days with the rented car: "))
dist = float(input("Distance traveled in KM: "))
tdays = float(input("Price per day rented: "))
tdist = float(input("Price per KM traveled: "))

pdays = days*tdays
pdist = dist*tdist
total = pdays+pdist

print(f"Total left to pay is R${total:.2f}")
# In this exercise the discount was fixed 5% but I created a variable to make it better so the user can choose whatever discount he wants
price = float(input("Price of the product? R$ "))
discount = float(input("Discount to this product: "))
final = price-((price*discount)/100)
print(f"The price of the product was R${price:.2f}, with {discount:.0f}% discount it will cost R${final:.2f}")
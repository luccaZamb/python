# In this exercise the raise was fixed 15% but I created a variable to make it better so the user can choose whatever raise he wants
sal = float(input("What is the employee salary? R$ "))
rse = float(input("Raise to this employee: "))
final = sal+((sal*rse)/100)
print(f"The salary was R${sal:.2f}, with {rse:.0f}% raise it will be R${final:.2f}!")
print("Welcome to Vela's shop!")
print("******** \ n___n / **********")
item = input("What item are you purchasing?")
price = float(input(f"What is the price of {item}?"))
amount = float(input(f"How many {item} are you buying?"))

print(f"added {price} {item}(s) to shopping cart!")

result = str(amount * price )
print(f'''
Subtotal: ${result}
************************
Awesome! 
Now hand over the money!

Thanks for shopping with Vela! 
 \ n_____n/ o_o xD

''')



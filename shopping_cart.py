# shopping_cart.py

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


import random
import os
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

z = os.getenv("TAX_RATE")


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output
selected_products = []

while True:
     selected_id = input("Please enter product ID for each item separately. When finished entering all items, type 'DONE'. ")
     #print(selected_id)
     if selected_id == "DONE":
        break
     else:
        matching_product = None
        for p in products:
            if str(p["id"]) == str(selected_id):
                #print(selected_id)
                matching_product = p
            
        #print(matching_product)
        
        if matching_product:
            selected_products.append(matching_product)
        else:
            print("Whoops, please make sure you've entered the correct product identifier.")         
            
            
# selected_product = selected_products[0]
#####print(selected_product)
            ###else: ____
            #if str(item["id"]) != str(selected_id):
             #   print("Whoops, please make sure you've entered the correct product identifier.")
  # if # correct, print(products["name"], products["price"])
#print(products["name"], products["price"])
#print(selected_products)
print("You selected", len(selected_products), "items.", "Below is your receipt.")

print(" ---------------------------------")
print("Sedina's Marvelous Groceries") # A grocery store name of your choice
print("(555)-555-5555")# A grocery store phone number and/or website URL and/or address of choice
print(" ---------------------------------")
import datetime
now = datetime.datetime.now()
#print(type(now))
#print("Checkout At:", now) #The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
print("Checked Out At:", now.strftime("%Y-%m-%d %H:%M:%S"))
print(" ---------------------------------")
# # The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
from operator import itemgetter
sorted_selected_products= sorted(selected_products, key=itemgetter("name"))

for item in sorted_selected_products:
    #print(item.keys())
    print(item["name"], ".....", to_usd(item["price"]))
   # print(item.values())

from statistics import mean
print(" ---------------------------------")
# # The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
#for item in sorted_selected_products:
    #print(item.keys())
    #print(to_usd(item["price"]))
prices = [item["price"] for item in sorted_selected_products]
subtotal = sum(prices)

print("Subtotal:", to_usd(subtotal))

# # The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
# tax = float(subtotal) * 0.0875
#tax = subtotal * 0.0875 ## I guess I don't need to convert it to a float now that I've removed the dollar sign?
tax = subtotal * float(z)

print("Sales tax:", to_usd(tax))
print(" ---------------------------------")
print(" ---------------------------------")

# # The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
total_price = subtotal + tax
print("**TOTAL:**", to_usd(total_price))

print(" ---------------------------------")
print("Thank you, please come back soon :)")# A friendly message thanking the customer and/or encouraging the customer to shop again

#print(products)
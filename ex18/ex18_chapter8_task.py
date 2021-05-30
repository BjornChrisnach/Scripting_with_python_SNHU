"""
Task: create the empty data structure

1) Create an empty dictionary with the variable name grocery_item
2) Create an empty grocery_history list

-------------------------------------------------------------------------------
"""

# Task: create the empty data structure
# remove comment tags and initialize the dictonary (grocery_item)
# and list (grocery_history) accordingly.

grocery_item = dict()

grocery_history = list()

# item_name = input("Item name: \n")
# quantity = int(input("Quantity purchased: \n"))
# cost = float(input("Price per item: \n"))

# grocery_item = ({'name': item_name, 'number': quantity, 'price': cost})
# grocery_history.append(grocery_item)

grocery_item = ({'name': 'eggs', 'number': 12, 'price': 2.99})
grocery_history.append(grocery_item)

grocery_item = ({'name': 'milk', 'number': 1, 'price': 3.99})
grocery_history.append(grocery_item)

print(grocery_history)
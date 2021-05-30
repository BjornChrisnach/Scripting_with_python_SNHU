# 1. Initialize data structures
# 2. Prepare control structure and obtain User Input
# 3. Loop through the grocery list
# 4. Provide output to the console

item_name = None
quantity = 0
price = 0.0
grocery_item = {'name': item_name, 'quantity': quantity, 'price': price}
grocery_history = list()

while True:
    item_name = input("Type in the name of the grocery item, or done if you \
finished creating your grocery list: \n")
    if item_name == 'done':
        break
    else:
        quantity = int(input('Type in the quantity of the grocery item: \n'))
        price = float(input('Type in the price per grocery item: \n'))
        
        grocery_item['name'] = item_name
        grocery_item['quantity'] = quantity
        grocery_item['price'] = price

        grocery_history.append(grocery_item.copy())
    
print(grocery_history)
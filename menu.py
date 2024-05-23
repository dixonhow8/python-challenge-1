# Menu dictionary
sub_menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# Create an empty list to store customer orders
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to Bridget's Variety Food Truck!")

# Function to print the sub-menu
def print_menu(menu):
    print("Sub-Menu:")
    for category, items in menu.items():
        print(f"{category}:")
        if isinstance(items, dict):
            for item, price in items.items():
                if isinstance(price, dict):
                    print(f"  {item}:")
                    for sub_item, sub_price in price.items():
                        print(f"    - {sub_item}: ${sub_price}")
                else:
                    print(f"  - {item}: ${price}")

# Main loop for orders 
place_order = True
while place_order:
    # Print the sub-menu
    print_menu(sub_menu)
    
    # Prompt the customer to enter their selection from the menu
    menu_selection = input("Enter your category from the menu: ")

    if menu_selection in sub_menu:
        menu_category = menu_selection

        # Check if the selected category is in dictionary
        if isinstance(sub_menu[menu_category], dict):
            item_name = input(f"Enter the name of the item from '{menu_category}': ")

            # If item is not found in dictionary
            item_found = False
            for key, value in sub_menu[menu_category].items():
                if isinstance(value, dict):
                    if item_name in value:
                        item_price = value[item_name]
                        item_found = True
                        break
                else:
                    if item_name == key:
                        item_price = value
                        item_found = True
                        break
            # If item is found in dictionary
            if item_found:
                # Ask the customer for the quantity of the menu item
                quantity = input(f"Enter the quantity for '{item_name}': ")

                # Check if the quantity is a number, default to 1 if not
                if quantity.isdigit():
                    quantity = int(quantity)
                else:
                    print("Quantity set to default (1).")
                    quantity = 1

                # Add the item name, price, and quantity to the order list
                order_list.append({
                    "Item name": item_name,
                    "Price": item_price,
                    "Quantity": quantity
                })
            else:
                print(f"'{item_name}' is not a valid item in '{menu_category}'.")
        else:
            print(f"'{menu_selection}' does not contain valid items.")
    else:
        print(f"'{menu_selection}' is not a valid menu category.")
    while True:
        #Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").lower()
        match keep_ordering:
            case 'y':
                place_order = True
                break
            case 'n':
                place_order = False
                print("Thank you for your order")
                break
            case _:
                print("Please try again because that wasn't a valid input.")

# Print out the customer's order
print("This is what we are preparing for you.\n")

# Display the final order in a receipt format
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|---------")
for order in order_list:
    item_name = order['Item name']
    price = order['Price']
    quantity = order['Quantity']
    
    # Calculate the spaces needed for formatting
    item_name_spaces = ' ' * (26 - len(item_name))
    price_spaces = ' ' * (6 - len(f"${price:.2f}"))
    quantity_spaces = ' ' * (7 - len(str(quantity)))
    
    # Print the formatted receipt line
    print(f"{item_name}{item_name_spaces}| ${price:.2f}{price_spaces}| {quantity}{quantity_spaces}")

# Calculate and display the total cost
total_cost = sum([order['Price'] * order['Quantity'] for order in order_list])
print(f"\nTotal cost: ${total_cost:.2f}")

# =========================================================
# BOOKACHINO CAFE – CLI ORDERING SYSTEM
# =========================================================
# This program provides a command-line interface that allows
# users to browse menus, manage a cart, and place orders.
# =========================================================


# -----------------------------
# MENU DATA
# -----------------------------

# Coffee menu items with price, description, and stock level
coffee_menu = {
    "Espresso": {"price": 2.5, "description": "Strong espresso shot", "stock": 50},
    "Americano": {"price": 2.0, "description": "Espresso with hot water", "stock": 40},
    "Latte": {"price": 3.0, "description": "Espresso with steamed milk", "stock": 30},
    "Cappuccino": {"price": 3.5, "description": "Espresso, steamed milk & foam", "stock": 25},
    "Mocha": {"price": 3.75, "description": "Espresso with chocolate and milk", "stock": 20},
    "Flat White": {"price": 3.25, "description": "Espresso with microfoam milk", "stock": 20},
    "Macchiato": {"price": 2.75, "description": "Espresso with foamed milk", "stock": 15},
    "Ristretto": {"price": 2.25, "description": "Short, concentrated espresso shot", "stock": 15},
}

# Food menu items
food_menu = {
    "Pancakes": {"price": 5.5, "description": "Fluffy pancakes with syrup and butter", "stock": 30},
    "Avocado Toast": {"price": 6.0, "description": "Sourdough with smashed avocado", "stock": 25},
    "Veggie Sandwich": {"price": 6.5, "description": "Grilled veggies & hummus", "stock": 20},
    "Chicken Wrap": {"price": 7.0, "description": "Grilled chicken wrap", "stock": 20},
    "Caesar Salad": {"price": 5.75, "description": "Lettuce with Caesar dressing", "stock": 15},
    "Quiche": {"price": 6.25, "description": "Egg tart with cheese & vegetables", "stock": 15},
    "Soup of the Day": {"price": 4.5, "description": "Ask for today's soup", "stock": 10},
    "Fruit Bowl": {"price": 3.75, "description": "Mixed seasonal fruits", "stock": 20},
}

# Book menu items
book_menu = {
    "1984": {"price": 9.99, "description": "By George Orwell", "stock": 12},
    "To Kill a Mockingbird": {"price": 7.99, "description": "By Harper Lee", "stock": 8},
    "The Great Gatsby": {"price": 10.50, "description": "By F. Scott Fitzgerald", "stock": 10},
    "Pride and Prejudice": {"price": 6.75, "description": "By Jane Austen", "stock": 14},
    "Moby Dick": {"price": 11.25, "description": "By Herman Melville", "stock": 6},
    "The Catcher in the Rye": {"price": 8.99, "description": "By J.D. Salinger", "stock": 9},
    "Brave New World": {"price": 9.50, "description": "By Aldous Huxley", "stock": 7},
    "The Hobbit": {"price": 12.00, "description": "By J.R.R. Tolkien", "stock": 5},
}


# -----------------------------
# GLOBAL DATA
# -----------------------------

# Combined menu used for stock management
full_menu = {**coffee_menu, **food_menu, **book_menu}

# Stores items added to the customer's cart
cust_basket = {}


# -----------------------------
# MENU DISPLAY FUNCTIONS
# -----------------------------

def get_numbered_menu(menu):
    """Return a numbered version of a menu for user selection."""
    items = list(menu.items())
    return {i + 1: (name, details) for i, (name, details) in enumerate(items)}


def display_numbered_menu(numbered_menu, category_name):
    """Display a numbered menu for a given category."""
    print(f"\n{category_name} Menu:")
    for num, (name, details) in numbered_menu.items():
        print(
            f"{num}. {name} - ${details['price']:.2f} "
            f"({details['description']}) [Stock: {details['stock']}]"
        )
    return numbered_menu


# -----------------------------
# CART MANAGEMENT
# -----------------------------

def add_to_cart(item_name, quantity, full_menu):
    """Add an item and quantity to the cart if stock allows."""
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if item_name not in full_menu:
        print(f"Item '{item_name}' not found.")
        return

    if full_menu[item_name]["stock"] < quantity:
        print(f"Not enough stock for '{item_name}'.")
        return

    if item_name in cust_basket:
        cust_basket[item_name]["quantity"] += quantity
    else:
        cust_basket[item_name] = {
            "price": full_menu[item_name]["price"],
            "quantity": quantity
        }

    full_menu[item_name]["stock"] -= quantity
    print(f"Added {quantity} x '{item_name}' to cart.")


def remove_from_cart(item_name, quantity, full_menu):
    """Remove a quantity of an item from the cart."""
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        return

    if item_name not in cust_basket:
        print(f"Item '{item_name}' not in cart.")
        return

    current_quantity = cust_basket[item_name]["quantity"]

    if quantity >= current_quantity:
        del cust_basket[item_name]
        full_menu[item_name]["stock"] += current_quantity
        print(f"Removed all of '{item_name}'.")
    else:
        cust_basket[item_name]["quantity"] -= quantity
        full_menu[item_name]["stock"] += quantity
        print(f"Removed {quantity} x '{item_name}'.")


def view_cart():
    """Display all items currently in the cart."""
    if not cust_basket:
        print("Cart is empty.")
        return

    print("\nCart Contents:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal

    print(f"\nTotal: ${total:.2f}")


def checkout():
    """Complete the order and clear the cart."""
    if not cust_basket:
        print("Nothing to checkout.")
        return

    print("\nCheckout Summary:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal

    print(f"\nOrder complete. Total paid: ${total:.2f}")
    cust_basket.clear()


# -----------------------------
# MAIN PROGRAM LOOP
# -----------------------------

def main_cli():
    """Main application loop."""
    while True:
        print("\n========= BookAchino Cafe =========")
        print("1. View Coffee Menu")
        print("2. View Food Menu")
        print("3. View Book Menu")
        print("4. View Cart")
        print("5. Add Item to Cart")
        print("6. Remove Item from Cart")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Select an option (1-8): ").strip()

        if choice == '1':
            display_numbered_menu(get_numbered_menu(coffee_menu), "Coffee")

        elif choice == '2':
            display_numbered_menu(get_numbered_menu(food_menu), "Food")

        elif choice == '3':
            display_numbered_menu(get_numbered_menu(book_menu), "Books")

        elif choice == '4':
            view_cart()

        elif choice == '5':
            print("\nChoose a category:")
            print("1. Coffee\n2. Food\n3. Books")
            cat_choice = input("Enter category number: ").strip()

            if cat_choice == '1':
                menu = coffee_menu
                name = "Coffee"
            elif cat_choice == '2':
                menu = food_menu
                name = "Food"
            elif cat_choice == '3':
                menu = book_menu
                name = "Books"
            else:
                print("Invalid category.")
                continue

            numbered = display_numbered_menu(get_numbered_menu(menu), name)

            try:
                item_num = int(input("Enter item number: "))
                item_name = numbered[item_num][0]
                qty = int(input("Enter quantity: "))
                add_to_cart(item_name, qty, full_menu)
            except (ValueError, KeyError):
                print("Invalid input.")

        elif choice == '6':
            if not cust_basket:
                print("Cart is empty.")
                continue

            print("\nItems in Cart:")
            numbered = {i + 1: (name, details)
                        for i, (name, details) in enumerate(cust_basket.items())}

            for num, (name, details) in numbered.items():
                print(f"{num}. {name} - {details['quantity']} x ${details['price']:.2f}")

            try:
                item_num = int(input("Enter item number: "))
                item_name = numbered[item_num][0]
                qty = int(input("Enter quantity to remove: "))
                remove_from_cart(item_name, qty, full_menu)
            except (ValueError, KeyError):
                print("Invalid input.")

        elif choice == '7':
            checkout()

        elif choice == '8':
            print("Goodbye.")
            break

        else:
            print("Invalid choice.")


# -----------------------------
# PROGRAM ENTRY POINT
# -----------------------------

main_cli()

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



def remove_from_cart(item_name, quantity, full_menu):
    if quantity <= 0:
        print(" Quantity must be greater than 0.")
        return
    if item_name not in cust_basket:
        print(f" Item '{item_name}' not in cart.")
        return
    current_quantity = cust_basket[item_name]["quantity"]
    if quantity >= current_quantity:
        del cust_basket[item_name]
        full_menu[item_name]["stock"] += current_quantity
        print(f" Removed all of '{item_name}'.")
    else:
        cust_basket[item_name]["quantity"] -= quantity
        full_menu[item_name]["stock"] += quantity
        print(f" Removed {quantity} x '{item_name}'.")

def view_cart():
    if not cust_basket:
        print(" Cart is empty.")
        return
    print("\n Cart Contents:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal
    print(f"\n Total: ${total:.2f}")

def checkout():
    if not cust_basket:
        print(" Nothing to checkout.")
        return
    print("\n Checkout Summary:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal
    print(f"\n Order complete! Total paid: ${total:.2f}")
    cust_basket.clear()


# Combine menus
full_menu = {**coffee_menu, **food_menu, **book_menu}
cust_basket = {}

# Helper to display numbered menu and get item by number
def get_numbered_menu(menu):
    items = list(menu.items())
    numbered = {i + 1: (name, details) for i, (name, details) in enumerate(items)}
    return numbered

def display_numbered_menu(numbered_menu, category_name):
    print(f"\n📋 {category_name} Menu:")
    for num, (name, details) in numbered_menu.items():
        print(f"{num}. {name} - ${details['price']:.2f} ({details['description']}) [Stock: {details['stock']}]")
    return numbered_menu

# Cart and menu operations (same as before)
def add_to_cart(item_name, quantity, full_menu):
    if quantity <= 0:
        print(" Quantity must be greater than 0.")
        return
    if item_name not in full_menu:
        print(f" Item '{item_name}' not found in the menu.")
        return
    if full_menu[item_name]["stock"] < quantity:
        print(f" Not enough stock for '{item_name}'. Available: {full_menu[item_name]['stock']}")
        return
    if item_name in cust_basket:
        cust_basket[item_name]["quantity"] += quantity
    else:
        cust_basket[item_name] = {
            "price": full_menu[item_name]["price"],
            "quantity": quantity
        }
    full_menu[item_name]["stock"] -= quantity
    print(f" ✅ Added {quantity} x '{item_name}' to cart.")

def remove_from_cart(item_name, quantity, full_menu):
    if quantity <= 0:
        print(" Quantity must be greater than 0.")
        return
    if item_name not in cust_basket:
        print(f" Item '{item_name}' not in cart.")
        return
    current_quantity = cust_basket[item_name]["quantity"]
    if quantity >= current_quantity:
        del cust_basket[item_name]
        full_menu[item_name]["stock"] += current_quantity
        print(f" 🗑️ Removed all of '{item_name}'.")
    else:
        cust_basket[item_name]["quantity"] -= quantity
        full_menu[item_name]["stock"] += quantity
        print(f" 🗑️ Removed {quantity} x '{item_name}'.")

def view_cart():
    if not cust_basket:
        print("🛒 Cart is empty.")
        return
    print("\n🛒 Cart Contents:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal
    print(f"\n🧾 Total: ${total:.2f}")

def checkout():
    if not cust_basket:
        print("🛍️ Nothing to checkout.")
        return
    print("\n✅ Checkout Summary:")
    total = 0
    for item, details in cust_basket.items():
        subtotal = details["price"] * details["quantity"]
        print(f"- {item}: {details['quantity']} x ${details['price']:.2f} = ${subtotal:.2f}")
        total += subtotal
    print(f"\n🎉 Order complete! Total paid: ${total:.2f}")
    cust_basket.clear()

# CLI Loop
def main_cli():
    while True:
        print("\n========= BookAchino Cafe Menu =========")
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
            print("\nChoose a category to add from:")
            print("1. Coffee\n2. Food\n3. Books")
            cat_choice = input("Enter category number: ").strip()
            if cat_choice == '1':
                menu = coffee_menu
                cat_name = "Coffee"
            elif cat_choice == '2':
                menu = food_menu
                cat_name = "Food"
            elif cat_choice == '3':
                menu = book_menu
                cat_name = "Books"
            else:
                print("❌ Invalid category.")
                continue

            numbered = display_numbered_menu(get_numbered_menu(menu), cat_name)
            try:
                item_num = int(input("Enter item number to add: "))
                if item_num not in numbered:
                    print("❌ Invalid item number.")
                    continue
                item_name = numbered[item_num][0]
                qty = int(input(f"Enter quantity for '{item_name}': "))
                add_to_cart(item_name, qty, full_menu)
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
        elif choice == '6':
            if not cust_basket:
                print("🛒 Cart is empty.")
                continue
            print("\n🗑️ Items in Cart:")
            numbered = {i + 1: (name, details) for i, (name, details) in enumerate(cust_basket.items())}
            for num, (name, details) in numbered.items():
                print(f"{num}. {name} - {details['quantity']} x ${details['price']:.2f}")
            try:
                item_num = int(input("Enter item number to remove: "))
                if item_num not in numbered:
                    print("❌ Invalid item number.")
                    continue
                item_name = numbered[item_num][0]
                qty = int(input(f"Enter quantity to remove from '{item_name}': "))
                remove_from_cart(item_name, qty, full_menu)
            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")
        elif choice == '7':
            checkout()
        elif choice == '8':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 8.")

# Start the CLI
main_cli()

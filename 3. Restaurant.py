# Restaurant Ordering System

# Menu setup
menu = [
    {"name": "Paneer Curry", "price": 250, "type": "Veg"},
    {"name": "Dal Tadka", "price": 150, "type": "Veg"},
    {"name": "Salad", "price": 100, "type": "Veg"},
    {"name": "Chicken Biryani", "price": 300, "type": "Non-Veg"},
    {"name": "Fish Fry", "price": 280, "type": "Non-Veg"}
]

FREE_DESSERT = {"name": "Ice Cream", "price": 0, "type": "Dessert"}

# Function to display menu
def show_menu(veg_only=False):
    print("\n--- Restaurant Menu ---")
    for idx, item in enumerate(menu, start=1):
        if veg_only and item["type"] != "Veg":
            continue
        print(f"{idx}. {item['name']} - ₹{item['price']} ({item['type']})")
    print()

# Function to take order
def add_to_order(veg_only=False):
    cart = {}
    while True:
        show_menu(veg_only)
        choice = input("Enter the item name to order (or type 'done' to finish): ").strip().title()
        if choice.lower() == "done":
            break
        
        # Find the menu item
        selected = next((item for item in menu if item["name"] == choice), None)
        if not selected:
            print("Invalid item. Please choose from the menu.")
            continue
        
        # Veg restriction
        if veg_only and selected["type"] != "Veg":
            print("Vegetarian mode selected. Cannot order Non-Veg items.")
            continue
        
        # Quantity input
        try:
            qty = int(input(f"Enter quantity for {choice}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Enter a number.")
            continue
        
        # Add to cart
        if choice in cart:
            cart[choice]["quantity"] += qty
        else:
            cart[choice] = {"quantity": qty, "price": selected["price"], "type": selected["type"]}
    
    return cart

# Function to calculate bill and show summary
def calculate_bill(cart):
    if not cart:
        print("No items ordered.")
        return
    
    print("\n--- Order Summary ---")
    print("{:<15} {:<10} {:<10}".format("Item", "Quantity", "Subtotal"))
    
    total = 0
    for item, details in cart.items():
        subtotal = details["quantity"] * details["price"]
        total += subtotal
        print("{:<15} {:<10} ₹{:<10}".format(item, details["quantity"], subtotal))
    
    # Free dessert rule
    if total > 1000:
        cart[FREE_DESSERT["name"]] = {"quantity": 1, "price": 0, "type": "Dessert"}
        print(f"\nCongratulations! You get a free dessert: {FREE_DESSERT['name']}")
    
    print(f"\nTotal Bill: ₹{total}")
    if FREE_DESSERT["name"] in cart:
        print("Free Dessert Added: Ice Cream")

# Main function to control restaurant system
def restaurant_system():
    print("Welcome to the Restaurant Ordering System!")
    mode = input("Select mode (Veg/Non-Veg) [V/N]: ").strip().lower()
    veg_only = True if mode == "v" else False
    
    cart = add_to_order(veg_only)
    calculate_bill(cart)
    print("\nThank you for dining with us!")

# Run the program
if __name__ == "__main__":
    restaurant_system()

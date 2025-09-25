# Shopping Cart / Billing System

# Predefined product list
products = {
    "Milk": 40,
    "Rice": 100,
    "Oil": 200,
    "Bread": 50,
    "Eggs": 10,
    "Cheese": 150,
    "Butter": 120
}

# Function to display products
def show_products():
    print("\n--- Available Products ---")
    for item, price in products.items():
        print(f"{item}: ₹{price}")
    print()

# Function to add items to cart
def add_to_cart():
    cart = {}
    while True:
        show_products()
        item = input("Enter the product name to add to cart (or type 'checkout' to finish): ").strip().title()
        if item.lower() == "checkout":
            break
        if item not in products:
            print("Invalid product name. Please choose from the list.")
            continue
        try:
            qty = int(input(f"Enter quantity for {item}: "))
            if qty <= 0:
                print("Quantity must be greater than 0.")
                continue
            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty
        except ValueError:
            print("Invalid input. Please enter a valid quantity.")
    return cart

# Function to calculate bill
def calculate_bill(cart):
    print("\n--- Detailed Bill ---")
    print("{:<10} {:<10} {:<10}".format("Item", "Quantity", "Price"))
    subtotal = 0
    for item, qty in cart.items():
        price = products[item] * qty
        subtotal += price
        print("{:<10} {:<10} ₹{:<10}".format(item, qty, price))
    
    # Apply discount
    discount = 0
    if subtotal > 2000:
        discount = 0.1 * subtotal
    
    # Apply GST
    gst = 0.05 * (subtotal - discount)
    
    net_payable = subtotal - discount + gst
    
    print("\nTotal Amount: ₹{:.2f}".format(subtotal))
    print("Discount: ₹{:.2f}".format(discount))
    print("GST @5%: ₹{:.2f}".format(gst))
    print("Net Payable Amount: ₹{:.2f}".format(net_payable))

# Main shopping cart flow
def shopping_cart():
    print("Welcome to the Supermarket Shopping Cart System!")
    cart = add_to_cart()
    if cart:
        calculate_bill(cart)
    else:
        print("No items in cart. Thank you for visiting!")

# Run the program
if __name__ == "__main__":
    shopping_cart()

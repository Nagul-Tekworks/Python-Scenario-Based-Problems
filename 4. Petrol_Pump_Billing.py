# Petrol Pump Billing System

# Fuel types and prices
fuels = {
    "Petrol": 110,
    "Diesel": 95
}

# Function to show fuel options
def show_fuels():
    print("\n--- Available Fuel Types ---")
    for fuel, price in fuels.items():
        print(f"{fuel}: ₹{price} per litre")
    print()

# Function to calculate bill
def calculate_bill(fuel_type, litres):
    price_per_litre = fuels[fuel_type]
    subtotal = litres * price_per_litre
    
    # Apply discount if litres > 50
    discount = 200 if litres > 50 else 0
    total = subtotal - discount
    
    # Print receipt
    print("\n--- Petrol Pump Receipt ---")
    print(f"Fuel Type      : {fuel_type}")
    print(f"Litres Purchased: {litres} L")
    print(f"Price per Litre : ₹{price_per_litre}")
    print(f"Subtotal        : ₹{subtotal}")
    print(f"Discount        : ₹{discount}")
    print(f"Total Payable   : ₹{total}")
    print("-------------------------------\n")

# Main petrol pump system
def petrol_pump_system():
    print("Welcome to the Petrol Pump Billing System!")
    while True:
        show_fuels()
        fuel_type = input("Select fuel type (Petrol/Diesel): ").strip().title()
        if fuel_type not in fuels:
            print("Invalid fuel type. Please select Petrol or Diesel.")
            continue
        
        try:
            litres = float(input("Enter number of litres to fill: "))
            if litres <= 0:
                print("Invalid input. Litres must be greater than 0.")
                continue
            elif litres > 100:
                print("Maximum 100 litres per transaction allowed.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        calculate_bill(fuel_type, litres)
        
        # Ask for another transaction
        again = input("Do you want to perform another transaction? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for visiting the Petrol Pump!")
            break

# Run the program
if __name__ == "__main__":
    petrol_pump_system()

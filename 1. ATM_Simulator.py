# ATM Machine Simulator

# Predefined user data
users = {
    "user1": {"pin": "1234", "balance": 10000},
    "user2": {"pin": "4321", "balance": 5000}
}

# Function to check balance
def check_balance(username):
    print(f"Your current balance is: ₹{users[username]['balance']}")

# Function to deposit money
def deposit(username):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Invalid amount. Must be greater than 0.")
        elif amount > 50000:
            print("Deposit limit exceeded. Try again.")
        else:
            users[username]["balance"] += amount
            print(f"₹{amount} deposited successfully.")
            check_balance(username)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function to withdraw money
def withdraw(username):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        balance = users[username]["balance"]
        
        if amount <= 0:
            print("Invalid amount. Must be greater than 0.")
        elif amount % 100 != 0:
            print("Withdrawal amount must be in multiples of 100.")
        elif amount > 20000:
            print("Withdrawal limit exceeded. Max ₹20,000 per transaction.")
        elif amount > balance - 1000:
            print("Insufficient funds or minimum balance requirement not met.")
        else:
            users[username]["balance"] -= amount
            print(f"₹{amount} withdrawn successfully.")
            check_balance(username)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Function for PIN verification
def verify_pin(username):
    attempts = 3
    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")
        if pin == users[username]["pin"]:
            print("PIN verified successfully!\n")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. Attempts left: {attempts}")
    print("Card Blocked. Please contact bank.")
    return False

# Main ATM menu
def atm(username):
    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            check_balance(username)
        elif choice == "2":
            deposit(username)
        elif choice == "3":
            withdraw(username)
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice. Please try again.")

# Main program
def main():
    print("Welcome to the Python ATM Simulator!")
    username = input("Enter your username: ")
    
    if username in users:
        if verify_pin(username):
            atm(username)
    else:
        print("User not found. Exiting...")

if __name__ == "__main__":
    main()

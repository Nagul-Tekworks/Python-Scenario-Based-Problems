# Movie Ticket Booking System

# Movie data
movies = [
    {"name": "Avengers", "price": 200, "rating": "U", "seats": 50},
    {"name": "Joker", "price": 250, "rating": "A", "seats": 30},
    {"name": "Pushpa 2", "price": 300, "rating": "UA", "seats": 40}
]

GST_RATE = 0.05  # 5%

# Function to display available movies
def show_movies():
    print("\n--- Available Movies ---")
    print("{:<3} {:<15} {:<10} {:<6} {:<6}".format("No.", "Movie Name", "Price", "Rating", "Seats"))
    for idx, movie in enumerate(movies, start=1):
        print("{:<3} {:<15} ₹{:<10} {:<6} {:<6}".format(idx, movie["name"], movie["price"], movie["rating"], movie["seats"]))

# Function to calculate total price with GST
def calculate_bill(price, tickets):
    subtotal = price * tickets
    gst = subtotal * GST_RATE
    total = subtotal + gst
    return subtotal, gst, total

# Function to handle ticket booking
def book_tickets():
    show_movies()
    try:
        choice = int(input("Select movie by number: "))
        if choice < 1 or choice > len(movies):
            print("Invalid movie selection.")
            return
    except ValueError:
        print("Invalid input. Enter a number.")
        return
    
    movie = movies[choice - 1]
    
    try:
        tickets = int(input("Enter number of tickets to book (max 6): "))
        if tickets < 1 or tickets > 6:
            print("Ticket limit exceeded. Max 6 tickets per booking.")
            return
        if tickets > movie["seats"]:
            print(f"Only {movie['seats']} seats available. Cannot book {tickets} tickets.")
            return
    except ValueError:
        print("Invalid input. Enter a number.")
        return
    
    # Age restriction for 'A' rated movies
    if movie["rating"] == "A":
        try:
            age = int(input("Enter your age: "))
            if age < 18:
                print("Age restriction: Must be 18+ for this movie.")
                return
        except ValueError:
            print("Invalid input. Enter a number.")
            return
    
    # Calculate bill
    subtotal, gst, total = calculate_bill(movie["price"], tickets)
    
    # Update seats
    movie["seats"] -= tickets
    
    # Show booking summary
    print("\n--- Booking Confirmation ---")
    print(f"Movie Name      : {movie['name']}")
    print(f"Tickets Booked  : {tickets}")
    print(f"Price per Ticket: ₹{movie['price']}")
    print(f"Subtotal        : ₹{subtotal:.2f}")
    print(f"GST @5%         : ₹{gst:.2f}")
    print(f"Total Amount    : ₹{total:.2f}")
    print(f"Remaining Seats : {movie['seats']}")

# Main movie booking system
def movie_system():
    print("Welcome to the Movie Ticket Booking System!")
    while True:
        book_tickets()
        again = input("\nDo you want to book another ticket? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Movie Ticket Booking System!")
            break

# Run the program
if __name__ == "__main__":
    movie_system()

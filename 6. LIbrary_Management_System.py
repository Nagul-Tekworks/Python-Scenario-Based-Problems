# Library Management System
from datetime import datetime, timedelta

# Books in the library
books = [
    {"name": "Python Basics", "author": "John Doe", "available": True},
    {"name": "Data Science 101", "author": "Jane Smith", "available": True},
    {"name": "Machine Learning", "author": "Alice Brown", "available": True},
    {"name": "Deep Learning", "author": "Bob Martin", "available": True},
    {"name": "Algorithms", "author": "Charles Lee", "available": True}
]

# Borrowed books record per student
borrowed_books = {}

# Function to display all books
def show_books():
    print("\n--- Library Books ---")
    print("{:<20} {:<15} {:<10}".format("Book Name", "Author", "Status"))
    for book in books:
        status = "Available" if book["available"] else "Issued"
        print("{:<20} {:<15} {:<10}".format(book["name"], book["author"], status))

# Function to issue a book
def issue_book(student_name, book_name):
    # Check student borrowed books count
    if student_name not in borrowed_books:
        borrowed_books[student_name] = []
    if len(borrowed_books[student_name]) >= 3:
        print("Cannot issue more than 3 books at a time.")
        return
    
    # Find the book
    book = next((b for b in books if b["name"].lower() == book_name.lower()), None)
    if not book:
        print("Book not found.")
        return
    if not book["available"]:
        print("Book is already issued.")
        return
    
    # Issue the book
    issue_date = datetime.today().date()
    borrowed_books[student_name].append({"book_name": book["name"], "issue_date": issue_date})
    book["available"] = False
    print(f"Book '{book['name']}' issued successfully on {issue_date}.")

# Function to return a book
def return_book(student_name, book_name, return_date_str):
    if student_name not in borrowed_books or not borrowed_books[student_name]:
        print("No books borrowed by this student.")
        return
    
    borrowed_record = next((b for b in borrowed_books[student_name] if b["book_name"].lower() == book_name.lower()), None)
    if not borrowed_record:
        print("This book was not borrowed by the student.")
        return
    
    try:
        return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    
    issue_date = borrowed_record["issue_date"]
    days_elapsed = (return_date - issue_date).days
    fine = 0
    if days_elapsed > 7:
        fine = (days_elapsed - 7) * 10
    
    # Update book availability
    book = next((b for b in books if b["name"].lower() == book_name.lower()), None)
    if book:
        book["available"] = True
    
    # Remove from borrowed list
    borrowed_books[student_name].remove(borrowed_record)
    
    print(f"Book '{book_name}' returned on {return_date}. Fine: ₹{fine}")

# Function to view borrowed books
def view_borrowed_books(student_name):
    print(f"\n--- Borrowed Books for {student_name} ---")
    if student_name not in borrowed_books or not borrowed_books[student_name]:
        print("No books borrowed.")
        return
    for record in borrowed_books[student_name]:
        issue_date = record["issue_date"]
        days_elapsed = (datetime.today().date() - issue_date).days
        fine = (days_elapsed - 7) * 10 if days_elapsed > 7 else 0
        print(f"Book: {record['book_name']}, Issued on: {issue_date}, Days elapsed: {days_elapsed}, Fine: ₹{fine}")

# Main library system
def library_system():
    print("Welcome to the Library Management System!")
    student_name = input("Enter your name: ").strip()
    
    while True:
        print("\nChoose an option:")
        print("1. Show all books")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. View borrowed books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == "1":
            show_books()
        elif choice == "2":
            book_name = input("Enter the book name to issue: ").strip()
            issue_book(student_name, book_name)
        elif choice == "3":
            book_name = input("Enter the book name to return: ").strip()
            return_date_str = input("Enter return date (YYYY-MM-DD): ").strip()
            return_book(student_name, book_name, return_date_str)
        elif choice == "4":
            view_borrowed_books(student_name)
        elif choice == "5":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    library_system()

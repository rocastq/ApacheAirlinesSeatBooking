import random
import string

# Simulate a database with a dictionary
database = {}

# Initialize the seat layout
seats = [
    ["1A", "2A", "3A", "4A", "78A", "77A", "79A", "80A"],
    ["1B", "2B", "3B", "4B", "78B", "77B", "79B", "80B"],
    ["1C", "2C", "3C", "4C", "78C", "79C", "79C", "80C"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["1D", "2D", "3D", "4D", "S", "S", "79D", "80D"],
    ["1E", "2E", "3E", "4E", "S", "S", "79E", "80E"],
    ["1F", "2F", "3F", "4F", "S", "S", "79F", "80F"]
]

# A set to store unique booking references
booking_references = set()

def generate_booking_reference():
    """Generate a unique 8-character alphanumeric booking reference."""
    while True:
        # Generate a random alphanumeric string of length 8
        reference = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        # Ensure the reference is unique
        if reference not in booking_references:
            booking_references.add(reference)
            return reference

def check_availability(row, column):
    """Check if a seat is available."""
    return seats[row][column] not in ["X", "S"] and not seats[row][column].startswith("B")

def book_seat(row, column, passport_number, first_name, last_name):
    """Book a seat if it is available and store traveler details."""
    if check_availability(row, column):
        # Generate a unique booking reference
        booking_reference = generate_booking_reference()
        # Store the booking reference in the seat layout
        seats[row][column] = f"B{booking_reference}"
        # Store traveler details in the database
        database[booking_reference] = {
            "passport_number": passport_number,
            "first_name": first_name,
            "last_name": last_name,
            "seat_row": row,
            "seat_column": column
        }
        print(f"Seat {row+1}{chr(65+column)} booked successfully. Booking reference: {booking_reference}")
    else:
        print("Seat is not available for booking.")

def free_seat(row, column):
    """Free a booked seat."""
    if seats[row][column].startswith("B"):
        # Remove the booking reference and free the seat
        booking_reference = seats[row][column][1:]
        del database[booking_reference]
        booking_references.remove(booking_reference)
        seats[row][column] = f"{row+1}{chr(65+column)}"
        print(f"Seat {row+1}{chr(65+column)} is now free.")
    else:
        print("Seat is not booked.")

def show_booking_state():
    """Display the current booking state of all seats."""
    for row in seats:
        print(" ".join(row))

def main():
    """Main function to provide menu options to the user."""
    while True:
        print("\nMenu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            row = int(input("Enter seat row (1-7): ")) - 1
            column = input("Enter seat column (A-F): ").upper()
            column = ord(column) - 65
            if check_availability(row, column):
                print("Seat is available.")
            else:
                print("Seat is not available.")
        
        elif choice == "2":
            row = int(input("Enter seat row (1-7): ")) - 1
            column = input("Enter seat column (A-F): ").upper()
            column = ord(column) - 65
            passport_number = input("Enter passport number: ")
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            book_seat(row, column, passport_number, first_name, last_name)
        
        elif choice == "3":
            row = int(input("Enter seat row (1-7): ")) - 1
            column = input("Enter seat column (A-F): ").upper()
            column = ord(column) - 65
            free_seat(row, column)
        
        elif choice == "4":
            show_booking_state()
        
        elif choice == "5":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    main()

# Apache Airlines Seat Booking System for Burak757

# Seat layout initialization
# 'F' represents a free seat
# 'R' represents a reserved seat
# 'X' represents an aisle
# 'S' represents a storage area

# Creating a 2D array to represent the seat layout with initial status as free ('F')
seat_layout = [['F' for _ in range(80)] for _ in range(6)]

# Marking aisles (X) and storage areas (S)
for i in range(6):
    if i == 3:  # Aisle row
        seat_layout[i] = ['X'] * 80
    elif i in [4, 5]:  # Storage row
        for j in range(78, 80):
            seat_layout[i][j] = 'S'

# Function to display the current seat layout
def display_seat_layout(layout):
    """Displays the current seat layout."""
    rows = ['A', 'B', 'C', 'D', 'E', 'F']
    for i, row in enumerate(layout):
        print(rows[i] + ' ' + ' '.join(row))
    print('\n')

# Function to check availability of a seat
def check_seat_availability(layout, row, seat_number):
    """Checks the availability of a given seat."""
    row_index = ord(row) - ord('A')
    seat_index = seat_number - 1
    if layout[row_index][seat_index] == 'F':
        return f"Seat {row}{seat_number} is available."
    elif layout[row_index][seat_index] == 'R':
        return f"Seat {row}{seat_number} is already booked."
    else:
        return f"Seat {row}{seat_number} cannot be booked (aisle or storage area)."

# Function to book a seat
def book_seat(layout, row, seat_number):
    """Books a given seat if it is free."""
    row_index = ord(row) - ord('A')
    seat_index = seat_number - 1
    if layout[row_index][seat_index] == 'F':
        layout[row_index][seat_index] = 'R'
        return f"Seat {row}{seat_number} successfully booked."
    elif layout[row_index][seat_index] == 'R':
        return f"Seat {row}{seat_number} is already booked."
    else:
        return f"Seat {row}{seat_number} cannot be booked (aisle or storage area)."

# Function to free a booked seat
def free_seat(layout, row, seat_number):
    """Frees a previously booked seat."""
    row_index = ord(row) - ord('A')
    seat_index = seat_number - 1
    if layout[row_index][seat_index] == 'R':
        layout[row_index][seat_index] = 'F'
        return f"Seat {row}{seat_number} has been freed."
    elif layout[row_index][seat_index] == 'F':
        return f"Seat {row}{seat_number} is already free."
    else:
        return f"Seat {row}{seat_number} cannot be freed (aisle or storage area)."

# Function to show the current booking state
def show_booking_state(layout):
    """Displays the current booking state."""
    display_seat_layout(layout)

# Main function to display the menu and handle user input
def main():
    """Main function to display the menu and handle user interactions."""
    while True:
        # Display the menu
        print("Seat Booking System Menu:")
        print("1. Check availability of seat")
        print("2. Book a seat")
        print("3. Free a seat")
        print("4. Show booking state")
        print("5. Exit program")

        # Get the user's choice
        choice = input("Please choose an option (1-5): ")

        # Handle the user's choice
        if choice == '1':
            row = input("Enter row (A-F): ").upper()
            seat_number = int(input("Enter seat number (1-80): "))
            print(check_seat_availability(seat_layout, row, seat_number))
        elif choice == '2':
            row = input("Enter row (A-F): ").upper()
            seat_number = int(input("Enter seat number (1-80): "))
            print(book_seat(seat_layout, row, seat_number))
        elif choice == '3':
            row = input("Enter row (A-F): ").upper()
            seat_number = int(input("Enter seat number (1-80): "))
            print(free_seat(seat_layout, row, seat_number))
        elif choice == '4':
            show_booking_state(seat_layout)
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()

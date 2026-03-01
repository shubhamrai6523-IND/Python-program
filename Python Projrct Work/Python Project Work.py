# Dynamic Seat Allocation System (Array/List based)
# Features: allocate, deallocate, search seat by roll no
# Concepts: linear search, insertion, deletion

def show_menu():
    print("\n=== Dynamic Seat Allocation System ===")
    print("1. Allocate seat (auto: first empty)")
    print("2. Allocate seat (manual: choose seat no.)")
    print("3. Deallocate seat by roll number")
    print("4. Search seat by roll number")
    print("5. Display seats (all / occupied / empty)")
    print("6. Exit")

def first_empty_seat(seats):
    for i, v in enumerate(seats):
        if v is None:
            return i
    return None

def roll_exists(seats, roll):
    # Linear search for duplicate roll number
    for v in seats:
        if v == roll:
            return True
    return False

def search_seat_by_roll(seats, roll):
    # Linear search to find the seat index for a roll number
    for i, v in enumerate(seats):
        if v == roll:
            return i
    return None

def allocate_auto(seats, roll):
    if roll_exists(seats, roll):
        print(f"Roll {roll} is already allocated a seat.")
        return

    idx = first_empty_seat(seats)
    if idx is None:
        print("No empty seats available!")
        return

    seats[idx] = roll  # insertion
    print(f"Allocated Seat No. {idx + 1} to Roll {roll}.")

def allocate_manual(seats, seat_no, roll):
    if seat_no < 1 or seat_no > len(seats):
        print("Invalid seat number.")
        return

    if roll_exists(seats, roll):
        print(f"Roll {roll} is already allocated a seat.")
        return

    idx = seat_no - 1
    if seats[idx] is not None:
        print(f"Seat No. {seat_no} is already occupied by Roll {seats[idx]}.")
        return

    seats[idx] = roll  # insertion
    print(f"Allocated Seat No. {seat_no} to Roll {roll}.")

def deallocate_by_roll(seats, roll):
    idx = search_seat_by_roll(seats, roll)
    if idx is None:
        print(f"Roll {roll} not found.")
        return

    seats[idx] = None  # deletion (mark empty)
    print(f"Deallocated Seat No. {idx + 1} from Roll {roll}.")

def display_seats(seats, mode="all"):
    if mode == "all":
        print("\nSeat Status (All):")
        for i, v in enumerate(seats, start=1):
            print(f"Seat {i:>3}: {'EMPTY' if v is None else 'Roll ' + str(v)}")
    elif mode == "occupied":
        print("\nOccupied Seats:")
        any_found = False
        for i, v in enumerate(seats, start=1):
            if v is not None:
                any_found = True
                print(f"Seat {i:>3}: Roll {v}")
        if not any_found:
            print("None")
    elif mode == "empty":
        print("\nEmpty Seats:")
        empties = [str(i + 1) for i, v in enumerate(seats) if v is None]
        print(", ".join(empties) if empties else "None")
    else:
        print("Invalid display mode.")

def main():
    try:
        n = int(input("Enter total number of seats: ").strip())
        if n <= 0:
            print("Seat count must be positive.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return

    seats = [None] * n  # array/list of seats, None means empty

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            roll = input("Enter roll number: ").strip()
            if not roll:
                print("Roll number cannot be empty.")
                continue
            allocate_auto(seats, roll)

        elif choice == "2":
            roll = input("Enter roll number: ").strip()
            if not roll:
                print("Roll number cannot be empty.")
                continue
            try:
                seat_no = int(input("Enter seat number to allocate: ").strip())
            except ValueError:
                print("Invalid seat number.")
                continue
            allocate_manual(seats, seat_no, roll)

        elif choice == "3":
            roll = input("Enter roll number to deallocate: ").strip()
            if not roll:
                print("Roll number cannot be empty.")
                continue
            deallocate_by_roll(seats, roll)

        elif choice == "4":
            roll = input("Enter roll number to search: ").strip()
            if not roll:
                print("Roll number cannot be empty.")
                continue
            idx = search_seat_by_roll(seats, roll)
            if idx is None:
                print(f"Roll {roll} not found.")
            else:
                print(f"Roll {roll} is seated at Seat No. {idx + 1}.")

        elif choice == "5":
            print("\nDisplay Options:")
            print("a) All seats")
            print("b) Occupied seats only")
            print("c) Empty seats only")
            sub = input("Choose (a/b/c): ").strip().lower()
            if sub == "a":
                display_seats(seats, "all")
            elif sub == "b":
                display_seats(seats, "occupied")
            elif sub == "c":
                display_seats(seats, "empty")
            else:
                print("Invalid option.")

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please choose 1-6.")

if __name__ == "__main__":
    main()
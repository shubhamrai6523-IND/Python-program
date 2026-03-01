# PRACTICAL 3 - LAB ASSIGNMENT 
# Tasks 1 to 7 

def get_int(prompt="Enter an integer: "):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

def task1():
    # 1
    # 12
    # 123
    # ...
    n = get_int("Enter number of rows: ")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()

def task2():
    # 1
    # 22
    # 333
    # ...
    n = get_int("Enter number of rows: ")
    for i in range(1, n + 1):
        for _ in range(i):
            print(i, end="")
        print()

def task3():
    # Print 123...n without string methods
    n = get_int("Enter n: ")
    for i in range(1, n + 1):
        print(i, end="")
    print()

def task4():
    # Inverted star pattern (right shifted)
    # * * * * *
    #  * * * *
    #   * * *
    #    * *
    #     *
    n = get_int("Enter number of rows: ")
    for i in range(n, 0, -1):
        spaces = n - i
        print(" " * spaces + "* " * i)

def task5():
    # Diamond (up then down) stars
    # *
    # * *
    # ...
    # * * * * *
    # * * * *
    # ...
    # *
    n = get_int("Enter number of rows (top half): ")

    for i in range(1, n + 1):
        print("* " * i)
    for i in range(n - 1, 0, -1):
        print("* " * i)

def task6():
    # Centered pyramid with 1,3,5,... stars
    n = get_int("Enter number of rows: ")
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * (2 * i - 1))

def task7():
    # Prime number finder between 2 numbers
    # while loop for validation + for loop for prime check

    while True:
        a = get_int("Enter first number: ")
        b = get_int("Enter second number: ")
        if a < b:
            break
        print("❌ Invalid input! First number must be less than second. Try again.\n")

    print(f"Prime numbers between {a} and {b} are:")

    start = max(2, a)
    found = False

    for num in range(start, b + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            found = True

    if not found:
        print("None", end="")
    print()

def show_menu():
    print("\n========= PRACTICAL 3 MENU =========")
    print("1. Task 1: Number pattern (1, 12, 123...)")
    print("2. Task 2: Repeated number pattern (1, 22, 333...)")
    print("3. Task 3: Print 123...n (no string methods)")
    print("4. Task 4: Inverted star pattern")
    print("5. Task 5: Diamond star pattern (up & down)")
    print("6. Task 6: Centered pyramid star pattern")
    print("7. Task 7: Prime numbers between 2 numbers")
    print("0. Exit")
    print("====================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-7): ").strip()

        if choice == "1":
            task1()
        elif choice == "2":
            task2()
        elif choice == "3":
            task3()
        elif choice == "4":
            task4()
        elif choice == "5":
            task5()
        elif choice == "6":
            task6()
        elif choice == "7":
            task7()
        elif choice == "0":
            print("✅ Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 0 to 7.")

if __name__ == "__main__":
    main()
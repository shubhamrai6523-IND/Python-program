# PRACTICAL 4 (NUMPY) - MENU DRIVEN PROGRAM
# Lab Assignment-1 (a, b) + Lab Assignment-2

import numpy as np

def get_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

def lab1_a_identity():
    print("\n--- Lab Assignment-1 (a): 4x4 Identity Matrix ---")
    I = np.eye(4, dtype=int)
    print(I)

def lab1_b_random_ops():
    print("\n--- Lab Assignment-1 (b): Random 3x3 Matrices + Add & Multiply ---")

    # Optional: allow user to set seed for same output every time
    use_seed = input("Do you want to set a seed for reproducible results? (y/n): ").strip().lower()
    if use_seed == "y":
        seed = get_int("Enter seed value (e.g., 10): ")
        np.random.seed(seed)

    A = np.random.randint(1, 10, (3, 3))  # 1..9
    B = np.random.randint(1, 10, (3, 3))

    print("\nMatrix A:")
    print(A)

    print("\nMatrix B:")
    print(B)

    print("\nA + B:")
    print(A + B)

    print("\nA x B:")
    print(A @ B)

def lab2_user_input_multiply():
    print("\n--- Lab Assignment-2: Multiply 5x3 by 3x2 (User Input) ---")
    print("Enter elements for 5x3 matrix A (15 integers):")

    A_vals = []
    for i in range(5):
        row = []
        for j in range(3):
            row.append(get_int(f"A[{i}][{j}] = "))
        A_vals.append(row)

    print("\nEnter elements for 3x2 matrix B (6 integers):")
    B_vals = []
    for i in range(3):
        row = []
        for j in range(2):
            row.append(get_int(f"B[{i}][{j}] = "))
        B_vals.append(row)

    A = np.array(A_vals)
    B = np.array(B_vals)

    print("\nMatrix A (5x3):")
    print(A)

    print("\nMatrix B (3x2):")
    print(B)

    product = A @ B
    print("\nProduct Matrix (A x B) (5x2):")
    print(product)

def show_menu():
    print("\n=========== PRACTICAL 4 (NUMPY) MENU ===========")
    print("1. Lab Assignment-1 (a): Create 4x4 Identity Matrix")
    print("2. Lab Assignment-1 (b): Random 3x3 Matrices + Addition + Multiplication")
    print("3. Lab Assignment-2: Multiply 5x3 Matrix by 3x2 Matrix (User Input)")
    print("0. Exit")
    print("================================================")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-3): ").strip()

        if choice == "1":
            lab1_a_identity()
        elif choice == "2":
            lab1_b_random_ops()
        elif choice == "3":
            lab2_user_input_multiply()
        elif choice == "0":
            print("✅ Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 0 to 3.")

if __name__ == "__main__":
    main()
# PRACTICAL NO: 6 - MENU DRIVEN PROGRAM
# Lab Assignment-1 + Lab Assignment-2

def lab_assignment_1():
    print("\n=== Lab Assignment-1: String Statistics ===")

    text = input("Enter a string: ")

    vowels = 0
    consonants = 0
    spaces = 0
    lowercase = 0

    for ch in text:
        if ch in "aeiouAEIOU":
            vowels += 1
        elif ch.isalpha():  # alphabet but not vowel
            consonants += 1

        if ch == " ":
            spaces += 1

        if ch.islower():
            lowercase += 1

    print("\n--- Statistics ---")
    print("Number of Vowels:", vowels)
    print("Number of Consonants:", consonants)
    print("Number of Spaces:", spaces)
    print("Number of Lowercase Letters:", lowercase)


def lab_assignment_2():
    print("\n=== Lab Assignment-2: Capitalize Sentence ===")

    print("Enter lines of text (Press ENTER on empty line to stop):")

    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    print("\n--- Output ---")
    for line in lines:
        print(line.upper())


def show_menu():
    print("\n========== PRACTICAL 6 MENU ==========")
    print("1. Lab Assignment-1 (String Statistics)")
    print("2. Lab Assignment-2 (Capitalize Sentences)")
    print("0. Exit")
    print("======================================")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (0-2): ").strip()

        if choice == "1":
            lab_assignment_1()
        elif choice == "2":
            lab_assignment_2()
        elif choice == "0":
            print("✅ Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 0, 1, or 2.")


if __name__ == "__main__":
    main()
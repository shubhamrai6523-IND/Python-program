# PRACTICAL 5 - Lab Assignment 1 (Tuples)

def get_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Enter a valid integer.")

# Input: series of integers -> store in tuple
n = get_int("How many integers do you want to enter? ")

nums = []
for i in range(n):
    nums.append(get_int(f"Enter integer {i+1}: "))

t = tuple(nums)
print("\nTuple =", t)

# a) total numbers in tuple
print("\n(a) Total number of elements in tuple:", len(t))

# b) last item in tuple
if len(t) > 0:
    print("(b) Last item in the tuple:", t[-1])
else:
    print("(b) Tuple is empty, no last item.")

# c) print elements in reverse order
print("(c) Tuple in reverse order:", t[::-1])

# d) print Yes if tuple contains 5 else No
print("(d) Contains 5? :", "Yes" if 5 in t else "No")

# e) remove first and last items, sort remaining, print result
if len(t) <= 2:
    print("(e) Not enough elements to remove first & last and sort remaining.")
else:
    remaining = list(t[1:-1])   # remove first & last
    remaining.sort()
    print("(e) After removing first & last and sorting:", tuple(remaining))

# Fibonacci Series Generator

n = int(input("Enter the number of terms: "))

first = 0
second = 1

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")

    for i in range(n):
        print(first, end=" ")

        next_num = first + second
        first = second
        second = next_num

    print()

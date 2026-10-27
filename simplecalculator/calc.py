
def calculator():
    print("\n===== SIMPLE CALCULATOR =====")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operator!")
                continue

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numbers.")

        choice = input("\nCalculate again? (yes/no): ").lower()
        if choice != "yes":
            print("Thank you for using the calculator!")
            break


calculator()

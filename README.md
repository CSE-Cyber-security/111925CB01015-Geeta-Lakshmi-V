# Factorial of a Number – Python

## 📌 Problem Statement

Write a Python program to find the factorial of a given number.

The factorial of a number `n` is the product of all positive integers from `1` to `n`.

For example:

`5! = 5 × 4 × 3 × 2 × 1 = 120`

## 💡 Features

* Accepts a number from the user.
* Calculates its factorial using a `for` loop.
* Displays the calculated factorial.
* Simple and beginner-friendly Python program.

## 🛠️ Technologies Used

* **Python 3**

## 📂 Project Structure

```text
Factorial/
│
├── factorial.py
└── README.md
```

## ▶️ How to Run

1. Make sure Python 3 is installed.
2. Open the terminal in the project folder.
3. Run the following command:

```bash
python factorial.py
```

## 🧑‍💻 Program

```python
n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial of", n, "=", factorial)
```

## 📥 Sample Input

```text
Enter a number: 5
```

## 📤 Sample Output

```text
Factorial of 5 = 120
```

## 📚 Concepts Used

* Variables
* User input
* Integer conversion
* `for` loop
* Multiplication
* Basic arithmetic operations

## 🎯 Learning Outcome

This program helps beginners understand how loops can be used to perform repeated calculations in Python.

## 👩‍💻 Author

**Geethalakshmi**

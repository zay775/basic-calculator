# Class-Based Python Calculator Program

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return "Error: division by zero."

def get_number(prompt):
    try:
        num = int(input(prompt))
        if 1 <= num <= 10:
            return num
        else:
            print("Error: Number must be between 1 and 10.")
            return None
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return None

def main():
    print("Class-Based Python Calculator (1–10 only)")
    print("----------------------------------------")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice (1-4): ")

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select a valid option.")
        return

    num1 = get_number("Enter first number (1–10): ")
    if num1 is None:
        return

    num2 = get_number("Enter second number (1–10): ")
    if num2 is None:
        return

    calc = Calculator(num1, num2)

    if choice == "1":
        print(f"Result: {calc.add()}")        # TC01
    elif choice == "2":
        print(f"Result: {calc.subtract()}")   # TC02
    elif choice == "3":
        print(f"Result: {calc.multiply()}")   # TC03
    elif choice == "4":
        print(f"Result: {calc.divide()}")     # TC04 & TC05

# Run the calculator
main()


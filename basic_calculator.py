class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    calc = Calculator()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if choice == '1':
            print("Result:", calc.add(num1, num2))
        elif choice == '2':
            print("Result:", calc.subtract(num1, num2))
        elif choice == '3':
            print("Result:", calc.multiply(num1, num2))
        elif choice == '4':
            print("Result:", calc.divide(num1, num2))
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    main()


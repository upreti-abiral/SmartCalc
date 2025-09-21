import math
import sys


class SmartCalc:
    """
    A modern Python calculator with support for:
    - Basic arithmetic (+, -, *, /)
    - Advanced operations (sqrt, ^, %)
    - Memory storage (M+, MR, MC)
    - History logging
    """

    def __init__(self):
        self.memory = 0
        self.history = []

    def add_to_history(self, expression, result):
        """Save each calculation to history."""
        self.history.append(f"{expression} = {result}")

    def add(self, x, y):
        result = x + y
        self.add_to_history(f"{x} + {y}", result)
        return result

    def subtract(self, x, y):
        result = x - y
        self.add_to_history(f"{x} - {y}", result)
        return result

    def multiply(self, x, y):
        result = x * y
        self.add_to_history(f"{x} * {y}", result)
        return result

    def divide(self, x, y):
        if y == 0:
            return "❌ Error: Division by zero"
        result = x / y
        self.add_to_history(f"{x} / {y}", result)
        return result

    def power(self, x, y):
        result = x ** y
        self.add_to_history(f"{x} ^ {y}", result)
        return result

    def square_root(self, x):
        if x < 0:
            return "❌ Error: Negative number"
        result = math.sqrt(x)
        self.add_to_history(f"√{x}", result)
        return result

    def percentage(self, x, y):
        """Calculate what % y is of x."""
        result = (x / y) * 100 if y != 0 else "❌ Error: Division by zero"
        self.add_to_history(f"{x} is what % of {y}", result)
        return result

    # Memory operations
    def memory_add(self, value):
        self.memory += value
        return f"💾 Stored {value} in memory."

    def memory_recall(self):
        return f"📂 Memory: {self.memory}"

    def memory_clear(self):
        self.memory = 0
        return "🗑️ Memory cleared."

    # History
    def show_history(self):
        if not self.history:
            return "📜 No history yet."
        return "\n".join(self.history)


def main():
    calc = SmartCalc()

    print("=" * 50)
    print("⚡ Welcome to SmartCalc ⚡")
    print("=" * 50)
    print("Available operations:")
    print(" +   → Addition")
    print(" -   → Subtraction")
    print(" *   → Multiplication")
    print(" /   → Division")
    print(" ^   → Exponentiation")
    print(" sqrt → Square root")
    print(" %   → Percentage")
    print("\nMemory: M+, MR, MC")
    print("History: H")
    print("Quit: Q")
    print("=" * 50)

    while True:
        choice = input("\nEnter operation: ").lower()

        if choice == 'q':
            print("👋 Thanks for using SmartCalc!")
            sys.exit()

        elif choice == 'h':
            print("\n📜 History:")
            print(calc.show_history())
            continue

        elif choice == 'm+':
            try:
                val = float(input("Enter number to store: "))
                print(calc.memory_add(val))
            except ValueError:
                print("⚠️ Invalid input.")
            continue

        elif choice == 'mr':
            print(calc.memory_recall())
            continue

        elif choice == 'mc':
            print(calc.memory_clear())
            continue

        try:
            if choice == 'sqrt':
                num = float(input("Enter number: "))
                print("Result:", calc.square_root(num))

            elif choice == '^':
                x = float(input("Enter base: "))
                y = float(input("Enter exponent: "))
                print("Result:", calc.power(x, y))

            elif choice == '%':
                x = float(input("Enter part: "))
                y = float(input("Enter whole: "))
                print("Result:", calc.percentage(x, y), "%")

            elif choice in ['+', '-', '*', '/']:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))

                if choice == '+':
                    print("Result:", calc.add(x, y))
                elif choice == '-':
                    print("Result:", calc.subtract(x, y))
                elif choice == '*':
                    print("Result:", calc.multiply(x, y))
                elif choice == '/':
                    print("Result:", calc.divide(x, y))

            else:
                print("⚠️ Invalid operation. Try again.")

        except ValueError:
            print("⚠️ Please enter valid numbers.")


if __name__ == "__main__":
    main()

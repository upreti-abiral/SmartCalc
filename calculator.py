import math


class SmartCalc:
    def __init__(self):
        self.memory = 0
        self.history = []

    def add_to_history(self, expression, result):
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
            return "Error: Division by zero"

        result = x / y
        self.add_to_history(f"{x} / {y}", result)
        return result

    def power(self, x, y):
        result = x ** y
        self.add_to_history(f"{x} ^ {y}", result)
        return result

    def square_root(self, x):
        if x < 0:
            return "Error: Cannot find square root of a negative number"

        result = math.sqrt(x)
        self.add_to_history(f"sqrt({x})", result)
        return result

    def percentage(self, x, y):
        if y == 0:
            return "Error: Division by zero"

        result = (x / y) * 100
        self.add_to_history(f"{x} is what % of {y}", result)
        return result

    def memory_add(self, value):
        self.memory += value
        return self.memory

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    def show_history(self):
        if not self.history:
            return "No history yet."

        return "\n".join(self.history)


def main():
    calc = SmartCalc()

    print("=" * 50)
    print("Smart Calculator")
    print("=" * 50)
    print("Operations:")
    print("+   Addition")
    print("-   Subtraction")
    print("*   Multiplication")
    print("/   Division")
    print("^   Exponentiation")
    print("sqrt Square root")
    print("%   Percentage")
    print()
    print("Memory: M+, MR, MC")
    print("History: H")
    print("Quit: Q")
    print("=" * 50)

    while True:
        choice = input("\nEnter operation: ").lower()

        if choice == "q":
            print("Thanks for using Smart Calculator!")
            return

        elif choice == "h":
            print("\nHistory:")
            print(calc.show_history())
            continue

        elif choice == "m+":
            try:
                value = float(input("Enter number to add to memory: "))
                print("Memory:", calc.memory_add(value))
            except ValueError:
                print("Please enter a valid number.")
            continue

        elif choice == "mr":
            print("Memory:", calc.memory_recall())
            continue

        elif choice == "mc":
            calc.memory_clear()
            print("Memory cleared.")
            continue

        try:
            if choice == "sqrt":
                number = float(input("Enter number: "))
                print("Result:", calc.square_root(number))

            elif choice == "^":
                base = float(input("Enter base: "))
                exponent = float(input("Enter exponent: "))
                print("Result:", calc.power(base, exponent))

            elif choice == "%":
                part = float(input("Enter part: "))
                whole = float(input("Enter whole: "))
                print("Result:", calc.percentage(part, whole), "%")

            elif choice in ["+", "-", "*", "/"]:
                first = float(input("Enter first number: "))
                second = float(input("Enter second number: "))

                if choice == "+":
                    print("Result:", calc.add(first, second))
                elif choice == "-":
                    print("Result:", calc.subtract(first, second))
                elif choice == "*":
                    print("Result:", calc.multiply(first, second))
                elif choice == "/":
                    print("Result:", calc.divide(first, second))

            else:
                print("Invalid operation. Try again.")

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()

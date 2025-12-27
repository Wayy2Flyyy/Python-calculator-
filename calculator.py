"""
A lightweight Python calculator module.

Performs fast, accurate computations with clean logic and minimal overhead.
Designed for simplicity, reliability, and easy reuse in larger projects.
"""


class Calculator:
    """A simple calculator class for basic and advanced arithmetic operations."""

    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Subtract b from a."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a, b):
        """
        Divide a by b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def power(a, b):
        """Raise a to the power of b."""
        return a ** b

    @staticmethod
    def modulo(a, b):
        """
        Calculate a modulo b.
        
        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero")
        return a % b

    @staticmethod
    def square_root(a):
        """
        Calculate the square root of a.
        
        Raises:
            ValueError: If a is negative.
        """
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5


def main():
    """CLI interface for the calculator."""
    calc = Calculator()
    
    print("=== Python Calculator ===")
    print("Available operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulo")
    print("7. Square Root")
    print("8. Exit")
    
    while True:
        try:
            choice = input("\nEnter operation (1-8): ").strip()
            
            if choice == "8":
                print("Goodbye!")
                break
            
            if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
                print("Invalid choice. Please enter a number between 1 and 8.")
                continue
            
            if choice == "7":
                a = float(input("Enter number: "))
                result = calc.square_root(a)
                print(f"Result: {result}")
            else:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                
                if choice == "1":
                    result = calc.add(a, b)
                elif choice == "2":
                    result = calc.subtract(a, b)
                elif choice == "3":
                    result = calc.multiply(a, b)
                elif choice == "4":
                    result = calc.divide(a, b)
                elif choice == "5":
                    result = calc.power(a, b)
                elif choice == "6":
                    result = calc.modulo(a, b)
                
                print(f"Result: {result}")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()

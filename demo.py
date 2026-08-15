#!/usr/bin/env python3
"""
Simple Calculator App - Production Ready Version
A basic calculator application with proper error handling and type hints.
"""

from typing import Union


def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Add two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Sum of a and b
    """
    return a + b


def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Difference of a and b
    """
    return a - b


def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        Product of a and b
    """
    return a * b


def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Divide two numbers with zero check.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Quotient of a and b
    
    Raises:
        ValueError: If divisor is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b


def power(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Raise a to the power of b.
    
    Args:
        a: Base number
        b: Exponent
    
    Returns:
        Result of a raised to power b
    """
    return a ** b

def calculator() -> None:
    """
    Main calculator loop that handles user interaction.
    Implements standard error handling and user input validation.
    """
    print("=" * 50)
    print("        CALCULATOR APPLICATION v1.0")
    print("=" * 50)
    
    operations = {
        '1': ('Add', add),
        '2': ('Subtract', subtract),
        '3': ('Multiply', multiply),
        '4': ('Divide', divide),
        '5': ('Power', power),
    }
    
    while True:
        try:
            print("\n" + "-" * 50)
            print("Select operation:")
            for key, (name, _) in operations.items():
                print(f"  {key}. {name}")
            print("  6. Exit")
            print("-" * 50)
            
            choice = input("\nEnter choice (1-6): ").strip()
            
            if choice == '6':
                print("\nThank you for using Calculator! Goodbye!")
                break
            
            if choice not in operations:
                print("❌ Invalid choice! Please select 1-6.")
                continue
            
            # Get user input
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("❌ Invalid input! Please enter numeric values.")
                continue
            
            # Perform operation
            operation_name, operation_func = operations[choice]
            result = operation_func(num1, num2)
            
            # Display result
            symbol_map = {
                '1': '+', '2': '-', '3': '×', '4': '÷', '5': '^'
            }
            print(f"\n✓ Result: {num1} {symbol_map[choice]} {num2} = {result}")
        
        except ValueError as e:
            print(f"❌ Error: {e}")
        except Exception as e:
            print(f"❌ Unexpected error: {e}")


def main() -> None:
    """Entry point for the calculator application."""
    calculator()


if __name__ == "__main__":
    main()

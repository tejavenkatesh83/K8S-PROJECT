#!/usr/bin/env python3
"""
A Python script to calculate the Least Common Multiple (LCM) of two integers.
Handles invalid inputs, zero, and negative numbers.
"""

import math

def lcm(a: int, b: int) -> int:
    """Return the Least Common Multiple of a and b."""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // math.gcd(a, b)

def main():
    try:
        # Get user input
        num1 = int(input("Enter the first integer: ").strip())
        num2 = int(input("Enter the second integer: ").strip())
    except ValueError:
        print("Error: Please enter valid integers.")
        return

    result = lcm(num1, num2)
    print(f"LCM of {num1} and {num2} is: {result}")

if __name__ == "__main__":
    main()

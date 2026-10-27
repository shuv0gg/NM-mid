# 1. Significant Digits
import math

x = float(input("Enter a number: "))
n = int(input("Enter number of significant digits: "))

# Significant digits must be a positive integer.
if n <= 0:
    print("Number of significant digits must be positive.")
elif x == 0:
    # Zero remains zero at any number of significant digits.
    print("Result:", 0)
else:
    # Convert significant digits into the decimal places needed by round().
    places = n - 1 - math.floor(math.log10(abs(x)))
    print("Rounded result:", round(x, places))


# Q2: Find a polynomial root using the Secant Method

# Function to evaluate a polynomial using Horner's rule
def horner(coeff, x):
    # Start with the leading coefficient
    p = coeff[0]

    # Evaluate the polynomial without using powers explicitly
    for i in range(1, len(coeff)):
        p = p * x + coeff[i]

    # Return the polynomial value f(x)
    return p


# Read the degree of the polynomial
n = int(input("Enter degree: "))

# Read coefficients from highest power to lowest power
coeff = list(map(float, input(
    "Enter coefficients (highest power first): "
).split()))

# Read the two initial guesses
x0, x1 = map(float, input("Enter x0 and x1: ").split())

# Read the required number of decimal places
d = int(input("Correct up to how many decimal places? "))

# Evaluate the polynomial at the initial guesses
f0 = horner(coeff, x0)
f1 = horner(coeff, x1)

# The initial guesses must have opposite signs of f(x)
if f0 * f1 >= 0:
    print("Invalid initial values")
else:
    # Print the iteration table heading
    print("\ni    x(i)       x(i-1)     f(x(i))"
          "     f(x(i-1))   x(i+1)")
    print("-" * 75)

    # Set the iteration counter
    i = 1

    # Continue until successive roots agree to d decimal places
    while True:
        # Evaluate the denominator of the Secant formula
        denominator = f1 - f0

        # Avoid division by zero
        if denominator == 0:
            print("Division by zero")
            break

        # Calculate the next approximation using the Secant formula
        x2 = x1 - f1 * (x1 - x0) / denominator

        # Print the current iteration and its function values
        print(f"{i:<5}{x1:<11.{d + 3}f}"
              f"{x0:<11.{d + 3}f}"
              f"{f1:<13.{d + 3}f}"
              f"{f0:<13.{d + 3}f}"
              f"{x2:.{d + 3}f}")

        # Stop if the current and next approximations
        # are equal when rounded to the required decimal places
        if round(x1, d) == round(x2, d):
            print(f"\nRoot = {x2:.{d}f}")
            break

        # Shift the approximations for the next iteration
        x0 = x1
        f0 = f1

        x1 = x2
        f1 = horner(coeff, x1)

        # Increase the iteration counter
        i += 1

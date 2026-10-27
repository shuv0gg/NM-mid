# 7. Newton-Raphson Method

def horner(coeff, x):
    # Evaluate a polynomial using Horner's recurrence.
    result = coeff[0]
    for a in coeff[1:]:
        result = result * x + a
    return result

degree = int(input("Enter degree: "))
coeff = list(map(float, input("Enter coefficients (highest power first): ").split()))
x = float(input("Enter initial guess x0: "))
tol = float(input("Enter positive tolerance (e.g. 0.0001): "))
max_iter = int(input("Enter maximum iterations: "))

if degree < 0 or len(coeff) != degree + 1 or tol <= 0 or max_iter <= 0:
    print("Invalid degree, coefficient count, tolerance, or iteration limit.")
else:
    # Differentiate each polynomial term to create derivative coefficients.
    derivative = [coeff[i] * (degree - i) for i in range(degree)]

    if not derivative:
        print("A constant polynomial cannot use Newton-Raphson iteration.")
    else:
        print("\nIter        x(i)             f(x(i))          x(i+1)")
        for i in range(1, max_iter + 1):
            fx = horner(coeff, x)
            dfx = horner(derivative, x)

            # The method divides by f'(x), so a zero derivative stops iteration.
            if dfx == 0:
                print("Derivative is zero. Cannot continue.")
                break

            # Newton-Raphson formula: x(next) = x - f(x) / f'(x).
            next_x = x - fx / dfx
            print(f"{i:<12}{x:<17.9f}{fx:<17.9g}{next_x:.9f}")

            if abs(next_x - x) < tol or abs(fx) < tol:
                print("Approximate root =", next_x)
                break
            x = next_x
        else:
            print("Maximum iterations reached. Last approximation =", x)

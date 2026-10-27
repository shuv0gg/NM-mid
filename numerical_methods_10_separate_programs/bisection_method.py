# 4. Bisection Method
# Enter polynomial coefficients from highest power to constant term.

def horner(coeff, x):
    # Evaluate the polynomial efficiently using Horner's recurrence.
    result = coeff[0]
    for a in coeff[1:]:
        result = result * x + a
    return result

degree = int(input("Enter degree: "))
coeff = list(map(float, input("Enter coefficients (highest power first): ").split()))
a = float(input("Enter left endpoint a: "))
b = float(input("Enter right endpoint b: "))
tol = float(input("Enter positive tolerance (e.g. 0.0001): "))

if degree < 0 or len(coeff) != degree + 1 or tol <= 0:
    print("Invalid degree, coefficient count, or tolerance.")
else:
    fa, fb = horner(coeff, a), horner(coeff, b)

    # Bisection needs a sign change across the interval, unless an endpoint is a root.
    if fa == 0:
        print("Root =", a)
    elif fb == 0:
        print("Root =", b)
    elif fa * fb > 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
    else:
        print("\nIter        a             b             midpoint       f(midpoint)")
        for i in range(1, 10001):
            # The midpoint divides the current interval into two halves.
            mid = (a + b) / 2
            fm = horner(coeff, mid)
            print(f"{i:<12}{a:<14.7f}{b:<14.7f}{mid:<15.7f}{fm:.7g}")

            # Stop when the function value or interval width is sufficiently small.
            if abs(fm) < tol or (b - a) / 2 < tol:
                print("Approximate root =", mid)
                break

            # Keep the half interval containing the sign change.
            if fa * fm < 0:
                b, fb = mid, fm
            else:
                a, fa = mid, fm
        else:
            print("Maximum iterations reached.")

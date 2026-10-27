# 5. False Position (Regula Falsi) Method

def horner(coeff, x):
    # Evaluate the polynomial using Horner's recurrence.
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

    # False position requires opposite signs, unless an endpoint is already a root.
    if fa == 0:
        print("Root =", a)
    elif fb == 0:
        print("Root =", b)
    elif fa * fb > 0:
        print("Invalid interval: f(a) and f(b) must have opposite signs.")
    else:
        print("\nIter        a             b             x             f(x)")
        for i in range(1, 10001):
            denominator = fb - fa
            # Protect against division by zero.
            if denominator == 0:
                print("Cannot continue: f(a) equals f(b).")
                break

            # The x-intercept of the line through (a, f(a)) and (b, f(b)).
            x = (a * fb - b * fa) / denominator
            fx = horner(coeff, x)
            print(f"{i:<12}{a:<14.7f}{b:<14.7f}{x:<14.7f}{fx:.7g}")

            if abs(fx) < tol:
                print("Approximate root =", x)
                break

            # Replace the endpoint that has the same sign as f(x).
            if fa * fx < 0:
                b, fb = x, fx
            else:
                a, fa = x, fx
        else:
            print("Maximum iterations reached.")

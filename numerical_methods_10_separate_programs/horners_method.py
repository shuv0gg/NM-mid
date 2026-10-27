# 3. Horner's Method
# Enter coefficients from highest power to the constant term.
degree = int(input("Enter degree of polynomial: "))
coeff = list(map(float, input("Enter coefficients (highest power first): ").split()))

if degree < 0 or len(coeff) != degree + 1:
    print("Invalid degree or coefficient count.")
else:
    x = float(input("Enter value of x: "))
    # Start with the leading coefficient.
    p = coeff[0]
    print("\nPower       Coefficient       P(k)")
    print("----------------------------------")
    print(f"{degree:<12}{coeff[0]:<18g}{p:g}")

    # Horner's recurrence: new P = previous P * x + next coefficient.
    for i in range(1, degree + 1):
        p = p * x + coeff[i]
        power = degree - i
        print(f"{power:<12}{coeff[i]:<18g}{p:g}")

    # The final value is the polynomial evaluated at x.
    print(f"\nf({x:g}) = {p:g}")

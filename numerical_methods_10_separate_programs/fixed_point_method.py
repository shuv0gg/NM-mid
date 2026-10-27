# 6. Fixed Point Iteration Method
import math

# Rewrite f(x) = 0 as x = g(x), then enter the expression for g(x).
# Supported names include x, sin, cos, tan, exp, log, sqrt, pi, and e.
expression = input("Enter g(x), e.g. cos(x) or (x + 2)**(1/3): ")
x = float(input("Enter initial guess x0: "))
tol = float(input("Enter positive tolerance (e.g. 0.0001): "))
max_iter = int(input("Enter maximum iterations: "))

# Provide only a limited set of names to the expression evaluator.
allowed = {
    "x": x, "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "exp": math.exp, "log": math.log, "sqrt": math.sqrt,
    "pi": math.pi, "e": math.e, "abs": abs
}

if tol <= 0 or max_iter <= 0:
    print("Tolerance and maximum iterations must be positive.")
else:
    print("\nIter        x(i)             x(i+1)           error")
    for i in range(1, max_iter + 1):
        try:
            # Calculate the next approximation: x(i+1) = g(x(i)).
            allowed["x"] = x
            next_x = float(eval(expression, {"__builtins__": {}}, allowed))
        except (ValueError, ZeroDivisionError, OverflowError, TypeError, NameError) as error:
            print("Could not evaluate g(x):", error)
            break

        error = abs(next_x - x)
        print(f"{i:<12}{x:<17.9f}{next_x:<17.9f}{error:.7g}")

        # Successive approximations are close enough when error is below tolerance.
        if error < tol:
            print("Approximate fixed point =", next_x)
            break
        x = next_x
    else:
        print("Maximum iterations reached. Last approximation =", x)

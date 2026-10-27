# 9. Newton's Forward and Backward Interpolation

import math

def difference_table(y):
    # Build successive difference columns: y, first differences, second differences...
    table = [list(y)]
    while len(table[-1]) > 1:
        previous = table[-1]
        table.append([
            previous[i + 1] - previous[i]
            for i in range(len(previous) - 1)
        ])
    return table

n = int(input("Enter number of data points: "))
x_values = list(map(float, input("Enter x values in order: ").split()))
y_values = list(map(float, input("Enter corresponding y values: ").split()))

if n < 2 or len(x_values) != n or len(y_values) != n:
    print("Enter at least two points and exactly n x and y values.")
else:
    h = x_values[1] - x_values[0]

    # Forward/backward interpolation assumes equally spaced x values.
    equally_spaced = h != 0 and all(
        math.isclose(x_values[i + 1] - x_values[i], h,
                     rel_tol=1e-9, abs_tol=1e-9)
        for i in range(1, n - 1)
    )

    if not equally_spaced:
        print("x values must be distinct and equally spaced.")
    else:
        target = float(input("Enter interpolation value: "))
        table = difference_table(y_values)

        # Print the triangular difference table.
        print("\nDifference table:")
        for i in range(n):
            row = [
                f"{table[j][i]:.6g}" if i < len(table[j]) else ""
                for j in range(n)
            ]
            print(f"{i:<5}" + "".join(f"{value:>14}" for value in row))

        # Choose forward near the start; backward near the end.
        if abs((target - x_values[0]) / h) <= abs((target - x_values[-1]) / h):
            u = (target - x_values[0]) / h
            result = y_values[0]
            term = 1.0

            # Forward formula uses Δy0, Δ²y0, etc.
            for order in range(1, n):
                term *= (u - (order - 1)) / order
                result += term * table[order][0]
            print("Method: Newton forward interpolation")
        else:
            u = (target - x_values[-1]) / h
            result = y_values[-1]
            term = 1.0

            # Backward formula uses the differences at the bottom of each column.
            for order in range(1, n):
                term *= (u + (order - 1)) / order
                result += term * table[order][n - order - 1]
            print("Method: Newton backward interpolation")

        print(f"Interpolated value at x = {target:g} is {result:.10g}")

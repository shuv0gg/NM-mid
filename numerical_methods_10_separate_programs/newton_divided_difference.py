# 10. Newton's Divided Difference Interpolation

n = int(input("Enter number of data points: "))
x_values = list(map(float, input("Enter x values: ").split()))
y_values = list(map(float, input("Enter corresponding y values: ").split()))

if n < 2 or len(x_values) != n or len(y_values) != n:
    print("Enter at least two points and exactly n x and y values.")
elif len(set(x_values)) != n:
    # Divided differences cannot divide by zero, so all x values must be distinct.
    print("All x values must be distinct.")
else:
    # Each row stores the value and successive divided differences for that point.
    table = [[0.0] * n for _ in range(n)]
    for i in range(n):
        table[i][0] = y_values[i]

    for order in range(1, n):
        for i in range(n - order):
            # Calculate f[x_i,...,x_(i+order)] from lower-order differences.
            table[i][order] = (
                table[i + 1][order - 1] - table[i][order - 1]
            ) / (x_values[i + order] - x_values[i])

    # Display the divided difference table.
    print("\nDivided difference table:")
    for i in range(n):
        values = [
            f"{table[i][j]:.7g}" if j < n - i else ""
            for j in range(n)
        ]
        print(f"{i:<5}{x_values[i]:<14.7g}" +
              "".join(f"{value:>14}" for value in values))

    target = float(input("Enter interpolation value: "))

    # Newton polynomial: f[x0] + f[x0,x1](x-x0) + ...
    result = table[0][0]
    product = 1.0
    for order in range(1, n):
        product *= target - x_values[order - 1]
        result += table[0][order] * product

    print(f"Interpolated value at x = {target:g} is {result:.10g}")

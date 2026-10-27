
# Newton's Backward Interpolation Method
# Print the backward difference table and calculate f(x).

# Read the number of data points
n = int(input("Enter number of points: "))

# Read x and y values
x = list(map(float, input("Enter x values: ").split()))
y = list(map(float, input("Enter y values: ").split()))

# Check whether the number of values is correct
if n < 2 or len(x) != n or len(y) != n:
    print("Invalid number of data points.")
else:
    # Calculate the equal spacing h between consecutive x values
    h = x[1] - x[0]

    # Newton's backward formula requires equally spaced x values
    equally_spaced = h != 0 and all(
        abs((x[i] - x[i - 1]) - h) < 1e-9
        for i in range(2, n)
    )

    if not equally_spaced:
        print("X values must be equally spaced.")
    else:
        # Store each order of backward differences in a separate column
        diff = [[0.0] * n for _ in range(n)]

        # The zeroth difference is the original y value
        for i in range(n):
            diff[i][0] = y[i]

        # Calculate first, second, third, ... differences
        for j in range(1, n):
            for i in range(j, n):
                # Backward difference:
                # ∇^j y[i] = ∇^(j-1)y[i] - ∇^(j-1)y[i-1]
                diff[i][j] = diff[i][j - 1] - diff[i - 1][j - 1]

        # Print the difference table heading
        print("\nx          Y          ", end="")
        for j in range(1, n):
            print(f"{j}st Diff   " if j == 1 else
                  f"{j}nd Diff   " if j == 2 else
                  f"{j}rd Diff   " if j == 3 else
                  f"{j}th Diff   ", end="")
        print()

        print("-" * (22 + 11 * (n - 1)))

        # Print x, y and backward differences for each row
        for i in range(n):
            print(f"{x[i]:<11.4f}{y[i]:<11.4f}", end="")

            # Only print differences available for this row
            for j in range(1, n):
                if j <= i:
                    print(f"{diff[i][j]:<11.4f}", end="")
                else:
                    print(f"{'':<11}", end="")
            print()

        # Read the x value whose function value is required
        value = float(input("\nEnter x to find f(x): "))

        # Calculate u using the last x value
        u = (value - x[-1]) / h

        # Start with the last y value
        result = y[-1]
        term = 1.0

        # Apply Newton's backward interpolation formula:
        # f(x) = yn + u∇yn
        #      + u(u+1)/2! ∇²yn + ...
        for j in range(1, n):
            # Update the product term for each difference order
            term *= (u + j - 1) / j

            # Add the corresponding backward difference term
            result += term * diff[n - 1][j]

        # Print the interpolated value to four decimal places
        print(f"\nf({value:g}) = {result:.4f}")

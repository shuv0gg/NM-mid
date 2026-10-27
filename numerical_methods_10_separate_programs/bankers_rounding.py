
n = int(input("How many numbers? "))
d = int(input("How many decimal places? "))

numbers = []

for i in range(n):
    x = input("Enter number " + str(i + 1) + ": ")
    numbers.append(x)

print("\nNumber\t\tBanker's Rounding")
print("--------------------------------------")

for x in numbers:
    negative = False

    if x[0] == '-':
        negative = True
        x = x[1:]

    if '.' in x:
        parts = x.split('.')
        integer = parts[0]
        fraction = parts[1]
    else:
        integer = x
        fraction = ""

    # Keep the required decimal digits
    fraction = fraction + "0" * (d + 1)
    kept = fraction[:d]
    dropped = fraction[d:]

    # Digit immediately after the kept digits
    next_digit = int(dropped[0])

    # Check whether any later digit is non-zero
    rest_nonzero = False
    for ch in dropped[1:]:
        if ch != '0':
            rest_nonzero = True

    # Determine whether to round up
    up = False

    if next_digit > 5:
        up = True
    elif next_digit == 5:
        if rest_nonzero:
            up = True
        else:
            if d > 0:
                last_digit = int(kept[-1])
            else:
                last_digit = int(integer[-1])

            if last_digit % 2 != 0:
                up = True

    # Convert the kept digits into an integer
    if d > 0:
        result = int(integer + kept)
    else:
        result = int(integer)

    if up:
        result += 1

    # Restore decimal point and trailing zeros
    result_str = str(result)

    if d > 0:
        result_str = result_str.zfill(d + 1)
        result_str = result_str[:-d] + "." + result_str[-d:]

    if negative and result != 0:
        result_str = "-" + result_str

    print(x + "\t\t" + result_str)

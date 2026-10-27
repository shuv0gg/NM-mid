def significant_figures(num):
    num = num.strip()

    if '.' in num:
        # Remove leading zeros
        num = num.lstrip('0')

        integer, decimal = num.split('.')

        # Remove leading zeros in decimal part
        if integer == '':
            decimal = decimal.lstrip('0')

        # Remove trailing zeros only if they are after decimal
        return len(integer + decimal)

    else:
        # Remove leading zeros and trailing zeros
        num = num.lstrip('0').rstrip('0')
        return len(num)


value = input("Enter a value: ")

print("Significant figures:", significant_figures(value))

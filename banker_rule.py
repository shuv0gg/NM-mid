from decimal import Decimal, ROUND_HALF_EVEN

value = input("Enter value: ")
n = int(input("Enter number of significant figures: "))

x = Decimal(value)

# Find the decimal position needed
shift = n - x.adjusted() - 1

quantize_value = Decimal("1e" + str(-shift))

result = x.quantize(quantize_value, rounding=ROUND_HALF_EVEN)

print("Result:", result)

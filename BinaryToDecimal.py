binary = input("Enter your Binary: ")

decimal = 0
power = len(binary) - 1

for digit in binary:
    decimal = decimal + int(digit) * (2 ** power)
    power = power - 1

print("Decimal :", decimal)

def powerof8(n):
    if n > 0 and (n & (n - 1)) == 0:
        count = 0
        while n > 1:
            n >>= 1
            count += 1
        return count % 3 == 0
    return False

num = int(input("Enter your number: "))
if powerof8(num):
    print(f"Yes, {num} is the power of 8")
else:
    print(f"No, {num} is not the power of 8")

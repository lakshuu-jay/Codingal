def firstSetBit(n):
    count = 1
    while(n):
        if (n & 1 == 1):
            print("Position of the first set bit:", count)
            return
        count += 1
        n >>= 1

number = int(input("Enter a number: "))
firstSetBit(number)
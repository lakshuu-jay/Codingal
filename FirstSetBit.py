def firstSetBit(n):
    count = 1
    while (n):
        if n &1 ==1:
           break
    count +=1
    n = n >>1
    print("Position of the first set bit:",count)

number = int(input("Enter a number:"))

firstSetBit(number)
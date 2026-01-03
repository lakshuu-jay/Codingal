def isEvenOdd(n):
    if (n^1 == n+1):
        return True
    else:
        return False

number = int(input("Enter A Number:"))

if isEvenOdd(number):
    print(number,"is Even")
else:
    print(number,"is Odd")
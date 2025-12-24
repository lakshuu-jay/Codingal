number=int(input("Input your number:"))
digits=len(str(number))

resultNumber=0
temp=number
while temp>0:
    digit=temp % 10
    resultNumber += digit ** digits
    temp //= 10

if number == resultNumber:
    print(number,"is Armstrong number")
else:
    print(number,"is not Armstrong number")
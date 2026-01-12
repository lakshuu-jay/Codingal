def printTwoOdd(arr,size):
    xorof2 = arr[0]
    x=0
    y=0

    for i in range(1,size):
        xorof2 = xorof2 ^ arr[i]
    
    setbit = xorof2 & ~(xorof2 - 1)

    for i in range(size):
        if arr[i]& setbit:
            x^=arr[i]
        else:
            y^=arr[i]
    
    print("The two ODD elements are",x,"&",y)

num=[2,2,3,4,5,5]
size=6
printTwoOdd(num,size)
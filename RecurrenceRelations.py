def myfunction1(n):
    if n <= 1:
        return
    for i in range(n + 1):
        print("coding1")
    myfunction1(n // 2)
    myfunction1(n // 3)
def myfunction2(n):
    if n <= 1:
        return
    print("coding1")
    myfunction2(n - 1)


print("T(n) = T(n/2) + T(n/3) + O(n)")
print("T(n) = T(n-1) + O(1)")
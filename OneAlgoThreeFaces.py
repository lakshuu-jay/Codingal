#O(1)-constant time best
def fun1(n):
    return n*(n+1)/2

#O(n)-linear time
def fun2(n):
    sum=0
    for i in range(1,n+1):
        sum += 1
    return sum

#O(n^2)-Quadratic time
def fun3(n):
    sum=0
    for i in range(1,n+1):
        for j in range(1,i+1):
            sum += 1
    return sum
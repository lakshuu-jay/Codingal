numberLargest= int(input("Enter Largest number:"))
numberSmallest=int(input("Enter Smallest number:"))

var1=numberLargest
var2=numberSmallest

while(numberSmallest):
    numberStore=numberSmallest
    numberSmallest=numberLargest%numberSmallest
    numberLargest=numberStore

lcm= (var1*var2)//numberLargest

print("LCM is:", lcm)
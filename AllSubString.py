string = input("Enter a string: ")
n = len(string)
for i in range(n):
    for j in range(i+1, n+1):
        print(string[i:j])

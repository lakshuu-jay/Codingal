def one_iteration(a, b):
    return a * b

def n_iteration(a, b):
    result = 0
    for i in range(b):
        result += a
    return result

a = int(input("Enter 'a' for a*b : "))
b = int(input("Enter 'b' for a*b : "))

one_iteration_result = one_iteration(a, b)
n_iteration_result = n_iteration(a, b)

print("1 iteration:", one_iteration_result)
print("N iteration:", n_iteration_result)

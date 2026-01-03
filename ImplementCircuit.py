A = int(input("Enter 1 or 0"))
B = int(input("Enter 1 or 0"))
C = int(input("Enter 1 or 0"))

Gate1 = A & B
Gate2 = B | C
Gate3 = B & C
Gate4 = Gate2 & Gate3
GateQ = Gate1 | Gate4

print("Output Q =", GateQ)
n = int(input("Enter your original number: "))

rev = 0
num_bits = n.bit_length() 

for i in range(num_bits):
    rev = (rev << 1) | (n & 1) 
    n >>= 1 

print("Reversed Number:", rev)

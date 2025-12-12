file = open("Text.txt","r")
print("First 12 Characters:")
print(file.read(12))
file.close()

file=open("Text.txt","r")
print("\nFirst Line of text:")
print(file.readline())
file.close()

file=open("Text.txt","r")
print("\nFirst 3 lines of Text:")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file=open("Text.txt","r")
print("\nAll Lines of Text:")
print(file.readlines())
file.close()

file=open("Text.txt","r")
print("\nAll Lines of Text using LOOP:")
for x in file:
    print(x)
file.close()
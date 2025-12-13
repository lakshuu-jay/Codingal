print("Using write along with with()function:")
with open("Document.txt","w")as f:
    f.write("Hello World!")

print("\nSplit() function in file handling:")
with open("Document2.txt","r")as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)

print("\nCreate a New file:")
file = open("NewDocument.txt","x")

print("\nChecking if a file exists or not:")
import os
if os.path.exists("spiderman.txt"):
    print("File Exists")
else:
    print("File does not exist")

print("\nCreate a new file if it does not exist:")
file = open("batman.txt","w")
file.write("I AM BATMAN!")
file.close()

print("\nDeleting a file:")
import os
os.remove("ironman.txt")

print("\nDelete the folder:")
import os
os.rmdir("spiderman")
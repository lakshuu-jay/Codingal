with open("Codingal.txt","w") as file:
    file.write("Hi!I am Penguin and I am 1yr old.")

with open("Codingal.txt","r") as file:
    data=file.readline()
    print("Words in this file are...")
    words = data.split()
    print(words)
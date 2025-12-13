import random

def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "!@#$%"

    all_characters = letters + numbers + symbols
    password = ""

    for i in range(6):
        password = password + random.choice(all_characters)

    return password

print("Your password is:", generate_password())
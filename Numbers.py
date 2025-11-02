import random

numbers = [5, 10, 15, 20, 25, 30]
original_number = random.choice(numbers)

guess = int(input("Guess the number: "))

while guess!=original_number:
    if guess == original_number:
        print("Correct! You guessed the right number!")
    elif guess > original_number:
        print("Your guess is higher than the actual number. Try again!")
    else:
        print("Your guess is lower than the actual number. Try again!")

print(f"(The correct number was {original_number})")
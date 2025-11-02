import random

num = random.randint[350,234,345,676,342]

guess = None

while guess != num:
    guess = input("Guess a number from the list: ")
    guess = int(guess)
    if guess == num:
        print("Congratulations! you won")
        break
    else:
          print("Try Again!")
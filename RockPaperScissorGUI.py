import tkinter as tk
import random

# Game logic functions
def rock():
    play("Rock")

def paper():
    play("Paper")

def scissors():
    play("Scissors")

def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You Win!"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Win!"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You Win!"
    else:
        result = "You Lose!"

    result_label.config(
        text="You: " + user_choice +
             "\nComputer: " + computer_choice +
             "\n" + result
    )

# Window setup
window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("300x250")

# Title
title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 14))
title.pack(pady=10)

# Buttons (NO lambda)
btn_rock = tk.Button(window, text="Rock", width=10, command=rock)
btn_rock.pack(pady=5)

btn_paper = tk.Button(window, text="Paper", width=10, command=paper)
btn_paper.pack(pady=5)

btn_scissors = tk.Button(window, text="Scissors", width=10, command=scissors)
btn_scissors.pack(pady=5)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 11))
result_label.pack(pady=10)

# Run app
window.mainloop()
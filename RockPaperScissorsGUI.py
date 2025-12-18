from tkinter import *
import random

def rock():
    game("Rock")

def paper():
    game("Paper")

def scissors():
    game("Scissors")

def game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "Tie"
    elif user_choice == "Rock" and computer_choice == "Scissors":
        result = "You Win"
    elif user_choice == "Paper" and computer_choice == "Rock":
        result = "You Win"
    elif user_choice == "Scissors" and computer_choice == "Paper":
        result = "You Win"
    else:
        result = "You Lose"
    
    Label(window, text="You: " + user_choice + "\nComputer: " + computer_choice + "\n" + result, font=("Arial", 11)).pack(pady=5)

window = Tk()
window.title("Rock Paper Scissors")
window.geometry("300x250")

title_label = Label(window, text="Rock Paper Scissors", font=("Arial", 14))
title_label.pack(pady=10)

rock_button = Button(window, text="Rock", width=10, command=rock)
rock_button.pack(pady=5)

paper_button = Button(window, text="Paper", width=10, command=paper)
paper_button.pack(pady=5)

scissors_button = Button(window, text="Scissors", width=10, command=scissors)
scissors_button.pack(pady=5)

result_label = Label(window, text="", font=("Arial", 11))
result_label.pack(pady=10)

window.mainloop()
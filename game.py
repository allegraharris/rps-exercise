# this is the "game.py" file...

import random
print(" ")
name = input("Welcome Player, please enter your name: ")

print("Welcome to my Rock, Paper, Scissors game, " + name + "!")
print(" ")
print("Rock, Paper, Scissors, Shoot!")
user_choice = input("What is your choice? ")

if user_choice == 'rock' or 'Rock': 
    print("You chose rock!")
elif user_choice == 'paper' or 'Paper':
    print("You chose paper!")
elif user_choice == 'scissors' or 'Scissors':
    print("You chose scissors!")
else: 
    print("Invalid user input. Please choose one of the listed options when you restart the game.")

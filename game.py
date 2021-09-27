# this is the "game.py" file...

import random
print(" ")
name = input("Welcome Player, please enter your name: ")

print("Welcome to my Rock, Paper, Scissors game, " + name + "!")
print(" ")
print("Rock, Paper, Scissors, Shoot!")
user_choice = input("What is your choice? ")
print(" ")

if user_choice == 'rock': 
    print("You chose rock!")
elif user_choice == 'paper':
    print("You chose paper!")
elif user_choice == 'scissors':
    print("You chose scissors!")
else: 
    print("Invalid user input. Please choose one of the listed options when you restart the game.")
    exit()

options = ["rock", "paper", "scissors"]

comp_choice = random.choice(options)
print("Computer chose " + comp_choice + "!")
print(" ")

if user_choice == comp_choice: #with help from code posted by Dominic Parente in slack
    print("You drew with the computer, play again!")
elif user_choice == 'rock' and comp_choice == 'paper' or user_choice == 'paper' and comp_choice == 'scissors' or user_choice == 'scissors' and comp_choice == 'rock':
    print("Oh no, you lost to the computer, play again!")
elif user_choice == 'rock' and comp_choice == 'scissors' or user_choice == 'paper' and comp_choice == 'rock' or user_choice == 'scissors' and comp_choice == 'paper':
    print("Congratulations! You beat the computer! Celebrate by playing again.")
print(" ")
exit()

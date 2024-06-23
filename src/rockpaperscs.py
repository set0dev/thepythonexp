import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = None


while player not in choices:
    player = input("rock, paper or scissors?: ").lower()

if player == computer:
    print("Computer: ", computer)
    print("Player: ", player)

elif player == "rock":
    if computer == "paper":
        print("you lose!")

    if computer == "scissors":
        print("you win!")

elif player == "paper":
    if computer == "scissors":
        print("you lose!")

    if computer == "rock":
        print("you win!")

elif player == "scissors":
    if computer == "rock":
        print("you lose!")

    if computer == "paper":
        print("you win!")


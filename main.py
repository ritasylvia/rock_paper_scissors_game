import random

t = ["Rock", "Paper", "Scissors"]
computer = random.choice(t)
player = 0

while player == 0:
    player = input("Select: Rock, Paper, Scissors ")
    if player == computer:
        print("It is a Tie!")
    elif player == "Rock":
        if computer == "Scissors":
            print("You win! " + player + " beats " + computer)
        else:
            print("You lose! " + computer + " beats " + player)
    elif player == "Paper":
        if computer == "Rock":
            print("You win! " + player + " beats " + computer)
        else:
            print("You lose! " + computer + " beats " + player)
    elif player == "Scissors":
        if computer == "Paper":
            print("You win! " + player + " beats " + computer)
        else:
            print("You lose! " + computer + " beats " + player)
    else:
        print("Incorrect input")
        
    player = 0
    computer = random.choice(t)

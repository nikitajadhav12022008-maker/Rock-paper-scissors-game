#Rock paper scissors game:
import random as rd
def game():
    print("-------Rock paper scissors game--------")
    print("Choices:rock,paper,scissors")

    user = input("enter your choice:").lower()
    choices = ["rock","paper","scissors"]
    computer = rd.choice(choices)

    print("you choice:",user)
    print("computer chose:",computer)

    if(user == computer):
        print("it's a tie!")
    elif(user == "rock"):
        if(computer == "scissors"):
            print("you win!")
        else:
            print("you lose")
    elif(user == "paper"):
        if(computer == "rock"):
            print("you won!")
        else:
            print("you lose")
    elif(user == "scissors"):
        if(computer == "paper"):
            print("you won!")
        else:
            print("you lose")
    else:
        print("invalid choice!")

game()



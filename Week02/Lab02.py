import random

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3!)")
else:
    computerChoice = random.randint(1,3)

    playerChoiceIndex = choices[playerChoice -1]
    computerChoiceIndex = choices[computerChoice -1]

    print("You choose: ", playerChoiceIndex)
    print("Computer choose: ", computerChoiceIndex)

    # Determine the winner using if/elif/else
    if playerChoiceIndex == computerChoiceIndex:
        print("It's a tie!")
    elif playerChoiceIndex == 0 and computerChoiceIndex == 2:
        print("Rock beats Scissors - You Win!")
    elif playerChoiceIndex == 1 and  computerChoiceIndex == 0:
        print("Paper beats Rock - You Win!")
    elif playerChoiceIndex == 2 and  computerChoiceIndex == 1:
        print("Scissors beats Paper - You Win!")
    else:
        print("You lose!")

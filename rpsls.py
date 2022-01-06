# Rock, Paper, Scissor, Lizard, Spock
# Lucas Simonis

import random

print("Welcome to Rock, Paper, Scissors, Lizard, Spock Game")
print("""
	Objective: A user will select Rock, Paper Scissors, Lizard, or Spock. The computer
	will then randomly make a selection from the same choices. The choices will be evaluated
	and a winner will be proclaimed.
	  """)

# counters for scores
user_score = 0
computer_score = 0

while True:
    # ask user for selection
    user_selection = input("Enter a choice (rock, paper, scissors, lizard, spock): ")
    user = user_selection.lower()
    choices = ["rock", "paper", "scissors", "lizard", "spock"]

    # valid the user made a correct choice
    while user not in choices:
        print("INVALID CHOICE!")
        selection = input("Enter a choice (rock, paper, scissors, lizard, spock): ")
        user = selection.lower()

    # randomly select choice for computer
    computer = random.choice(choices)

    # print user and computer choices
    print(f"\nUser chose {user}, computer chose {computer}.\n")

    # check to see if user and computer selected same choice
    if user == computer:
        print(f"Both players selected {user}. No winner is declared.")

    # check possibilities for rock
    elif user == "rock":
        if computer == "scissors":
            user_score += 1
            print("Rock smashes scissors! You win!")
        elif computer == "lizard":
            user_score += 1
            print("Rock smashes lizard! You win!")
        elif computer == "spock":
            computer_score += 1
            print("Spock vaporizes rock! You lose.")
        else:
            computer_score += 1
            print("Paper covers rock! You lose.")

    # check possibilities for paper
    elif user == "paper":
        if computer == "rock":
            user_score += 1
            print("Paper covers rock! You win!")
        elif computer == "lizard":
            computer_score += 1
            print("Lizard eats paper! You lose.")
        elif computer == "spock":
            user_score += 1
            print("Paper disproves spock! You win!")
        else:
            computer_score += 1
            print("Scissors cuts paper! You lose.")

    # check possibilities for scissors
    elif user == "scissors":
        if computer == "paper":
            user_score += 1
            print("Scissors cuts paper! You win!")
        elif computer == "lizard":
            user_score += 1
            print("Scissors decapitates lizard! You win!")
        elif computer == "spock":
            computer_score += 1
            print("Spock smashes scissors! You lose.")
        else:
            computer_score += 1
            print("Rock smashes scissors! You lose.")

    # check possibilities for lizard
    elif user == "lizard":
        if computer == "paper":
            user_score += 1
            print("Lizard eats paper! You win!")
        elif computer == "rock":
            computer_score += 1
            print("Rock smashes lizard! You lose.")
        elif computer == "spock":
            user_score += 1
            print("Lizard poisons spock! You win!")
        else:
            computer_score += 1
            print("Scissors decapitates lizard! You lose.")

    # check possibilities for spock
    elif user == "spock":
        if computer == "paper":
            computer_score += 1
            print("Paper disproves spock. You lose.")
        elif computer == "rock":
            user_score += 1
            print("Spock vaporizes rock. You win!")
        elif computer == "lizard":
            computer_score += 1
            print("Lizard poisons spock. You lose.")
        else:
            user_score += 1
            print("Spock smashes scissors. You win!")

    # print current score
    print(f"\nSCORE- User: {user_score} Computer: {computer_score}")

    # ask user if they want to play again and validate response
    play_again = input("\nPlay again? (Type y for yes/Type n for no): ")
    while play_again.lower() not in ["y", "n"]:
        print("Invalid Entry")
        play_again = input("Play again? (Type y for yes/Type n for no): ")

    # this will break while loop
    if play_again.lower() != "y":
        break

# print the final score
print(f"\nFINAL SCORE- User: {user_score} Computer: {computer_score}")

# add message to user about performance
if user_score == computer_score:
    print("\nYou are equally talented as the computer!")
elif user_score > computer_score:
    print("\nYou defeated the computer!")
else:
    print("\nThe computer has defeated you!")
import random

# i want to create the rock paper scrissors game
# the rules are the following: Rock beats scissors, Scissors beat paper, Paper beats rock
# the computer will be my opponent and can randomly choose one of the elements
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ["yes", "no"]:
            return play_again == "yes"
        else:
            print("Invalid choice. Please try again.")


def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        if result == "win":
            user_score += 1
            print("You won this round!")
        elif result == "lose":
            computer_score += 1
            print("You lost this round.")
        else:
            print("It's a tie.")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print(f"Your final score is: {user_score}")
    print(f"Computer's final score is: {computer_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
import random

def welcome():
    """This function displays a welcome message"""
    print("Welcome to Shecktar Rock-Paper-Scissors Game")

def get_user_choice():
    """This function gets the user's choice"""
    print("\n1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def get_computer_choice():
    """This function gets the computer's choice"""
    return str(random.randint(1, 3))

def determine_winner(user, computer):
    """This function determines the winner"""
    if user == computer:
        return "It's a tie!"
    if (user == '1' and computer == '3') or (user == '2' and computer == '1') or (user == '3' and computer == '2'):
        return "You win!"
    else:
        return "You lose!"

def play_again():
    """This function asks the user if they want to play again"""
    return input("\nDo you want to play again? (yes/no): ").lower() == "yes"

def game():
    """This function plays the game"""
    user_score = 0
    computer_score = 0

    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"\nYou chose {user}, computer chose {computer}.")
        result = determine_winner(user, computer)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"\nScores:\nYou - {user_score}\nComputer - {computer_score}")

        if not play_again():
            break

def main():
    welcome()
    game()

# Call the main function
if __name__ == "__main__":
    main()

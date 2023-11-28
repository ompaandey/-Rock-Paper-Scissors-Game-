import random

def get_user_choice():
    print("Choose: 1 for Rock, 2 for Paper, 3 for Scissors")
    choice = input("Enter your choice (1/2/3): ")
    return choice

def get_computer_choice():
    return str(random.randint(1, 3))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "1" and computer_choice == "3") or
        (user_choice == "2" and computer_choice == "1") or
        (user_choice == "3" and computer_choice == "2")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    print("Welcome to Rock-Paper-Scissors Game!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

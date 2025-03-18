import random

def get_user_choice():
    while True:
        choice = input("Enter r for rock, p for paper, or s for scissors: ").lower()
        if choice in ['r', 'p', 's']:
            return choice
        print("Invalid choice, please try again.")

def get_computer_choice():
    return random.choice(['r', 'p', 's'])

def show_choice(choice):
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    print(choices.get(choice, "Invalid choice"))

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("You lose!")

def main():
    player = get_user_choice()
    print("You chose:", end=" ")
    show_choice(player)
    
    computer = get_computer_choice()
    print("Computer chose:", end=" ")
    show_choice(computer)
    
    determine_winner(player, computer)

if __name__ == "__main__":
    main()

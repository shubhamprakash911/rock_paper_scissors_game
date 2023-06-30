import random

user_score = 0
computer_score = 0
draws = 0

while True:
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: (rock, paper, scissors)")
    print("To quit the game, type 'quit'.")

    user_choice = input("Your choice: ").lower()

    if user_choice == "quit":
        break

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("Computer chooses:", computer_choice)

    if user_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("-------------------------------")
    print("Game results:")
    print("-------------------------------")
    print("Your score:", user_score)
    print("Computer score:", computer_score)
    print("Draws:", draws)
    print("-------------------------------")

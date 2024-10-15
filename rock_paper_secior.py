import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    computer = random.choice(options)  # Computer randomly selects

    while player not in options:
        player = input("Enter the choice (rock, paper, scissors): ").lower()  # Convert input to lowercase for uniformity

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    # Game logic
    if player == computer:
        print("It's a tie!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")
    elif player == "rock" and computer == "scissors":
        print("You win!")
    else:
        print("You lose!")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (yes or no): ").lower()
    if play_again == "no":  # Corrected condition
        running = False

print("Thank you for playing!")

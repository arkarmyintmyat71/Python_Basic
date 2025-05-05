import random

user_wins = 0
compute_wins = 0
draw_wins = 0
options = ["rock", "paper", "scissors"]
#rock: 0, paper: 1, scissors: 2
while True:
    user_input = input("Enter your choice (Rock (or) Paper (or) Scissors) or Q for quit: ").lower()

    if user_input == "q":
        break
    if user_input not in options:
        continue

    random_number = random.randrange(0, 3)
    computer_picked = options[random_number]
    print("Computer picked:", computer_picked, ".")

    if user_input == "rock" and computer_picked == "scissors":
        print("Congratulation, you won!")
        user_wins += 1
    elif user_input == "paper" and computer_picked == "rock":
        print("Congratulation, you won!")
        user_wins += 1
    elif user_input == "scissors" and computer_picked == "paper":
        print("Congratulation, you won!")
        user_wins += 1
    elif user_input == computer_picked:
        print("We choice the same one.")
        draw_wins += 1
    else:
        print("Sorry, you lose me!")
        compute_wins += 1

print("You won", user_wins, "times and computer won", compute_wins, "times.")
print("We draw", draw_wins, "times.")
print("Good Bye!")
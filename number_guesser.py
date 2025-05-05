import random

top_of_range = input("Please enter a number for random range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please enter a number larger than 0 next time.")
        quit()

else:
    print("Please enter a number next time.")
    quit()

random_number = random.randrange(top_of_range)
guess = 0

while True:
    guess += 1

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

        if user_guess <= 0:
            print("Please enter a number larger than 0 next time.")
            continue
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_number:
        print("Congratulation! You got it.")
        break
    elif user_guess < random_number:
        print("Your guess number is under the number.")
        continue
    elif user_guess > random_number:
        print("Your guess number is above the number.")
        continue

print("You got it in", guess , "guesses.")
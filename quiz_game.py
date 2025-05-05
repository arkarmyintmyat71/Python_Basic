print("#########Welcome to my quiz game############")

playing = input("Do you want to play the game? (yes/no): ")
if str.title(playing) == "Yes":
    print("You are playing the game")
    score = 0
    answer_01 = input("What is CPU stand for? ")
    if str.lower(answer_01) != "central processing unit":
        print("Sorry, your answer is wrong.")

    else:
        print("Congratulation! your answer is right.")
        score += 1
    answer_02 = input("What is GPU stand for? ")
    if str.upper(answer_02) != "GRAPHICS PROCESSING UNIT":
        print("Sorry, your answer is wrong.")

    else:
        print("Congratulation! your answer is right.")
        score += 1
    answer_03 = input("What is RAM stand for? ")
    if str.capitalize(answer_03) != "Random access memory":
        print("Sorry, your answer is wrong.")

    else:
        print("Congratulation! your answer is right.")
        score += 1
        print("Your total score is : " + str((score/3)*100) + "%")
        if score != 3:
            print("You corrected " + str(score) + " answers.")
        else:
            print("Congratulation! You corrected all answers.")
else:
    print("You are not playing the game")
    quit()
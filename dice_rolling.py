from random import randint


print("Wellcome to 'Dice Rolling Simulator'!")
print("In order to win the game, your total points from three dices must be greater than 12. Good luck!") # You can set as many points as you want
key = input("Press 'S' to start: ").upper()
if key=='S':
    print("Rolling the dices....")
    game_over = False
    while not game_over:
        dice1 = randint(1, 6)
        dice2 = randint(1, 6)
        dice3 = randint(1, 6)
        total = dice1 + dice2 + dice3 
        print(f"First dice: {dice1}")
        print(f"Second dice: {dice2}")
        print(f"Third dice: {dice3}")
        print(f"Total points: {total}")
        if total>12:                        # According to what you have set above
            print("Hey, you won. Congratulation!")
        else:
            print("Sorry, you lost.")
        user_choice = input("If you want to roll the dices again, press 'Y', otherwise press 'N': ").upper()
        if user_choice=="Y":
            continue
        if user_choice=="N":
            print("Thanks for playing!")
            break
        else:
            print("Wrong keyword! Exit the game anyway :)")
            break
else:
    print("Wrong keyword! Exit the game :( ")

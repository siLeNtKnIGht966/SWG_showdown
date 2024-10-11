import random

choice_dict = {"s": 1, "w": -1, "g": 0}
print_dict = {1:"Snake",-1:"Water",0:"Gun"}
play_again = True
while (play_again):
    comp = random.randint(-1, 1)
    choice = input("Enter your choice (snake='s', water='w',gun='g'):  ").lower()
    you = choice_dict[choice]
    print(f"computer choose:{print_dict[comp]}")
    print(f"You choose: {print_dict[you]}")

    if (comp == -1 and you == 1):
        print("You win!!!")
    elif (comp == -1 and you == 0):
        print("computer win!!!")
    elif (comp == 1 and you == -1):
        print("Computer win!!!")
    elif (comp == 1 and you == 0):
        print("You win!!!")
    elif (comp == 0 and you == 1):
        print("computer win!!!")
    elif (comp == 0 and you == -1):
        print("You win!!!")
    else:
        print("game is draw")
    play_again_input = input("Do you want to play again?? (y/n)")
    if play_again_input != 'y':
        play_again = False
print("Thanks for playing!!!")


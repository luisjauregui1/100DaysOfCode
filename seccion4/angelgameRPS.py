import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock,paper,scissors]
user_chose = int(input("What do you choose? 0 = Rock, 1 = Paper , 2 = Scissors.\n"))
if user_chose >= 3 or user_chose < 0:
    print("You typed an ivalid number, you lose!")
else:
    print(game_images[user_chose])

    computer_choice = random.randint(0, 2)
    print("Computer chose")
    print(game_images[computer_choice])



    if user_chose == 0 and computer_choice == 2:
        print("User wins")
    elif computer_choice == 0 and user_chose == 2:
        print("You lose")
    elif computer_choice > user_chose:
        print("You lose")
    elif user_chose > computer_choice:
        print("You win")
    elif computer_choice == user_chose:
        print("It's a draw")

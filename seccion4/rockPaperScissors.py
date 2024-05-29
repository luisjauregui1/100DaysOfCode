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

# 0 = Rock 
# 1 = Paper
# 2 = Scissors

list_game = ["Rock", "Paper", "Scissors"]
pc_choose = random.choice(list_game)
pc_choose_index = list_game.index(pc_choose)

print("What do you choose ? Type 0 for Rock , 1 for paper or 2 for Scissors.")
user_input = int(input())


# Rock wins scissors
# Rock lost paper
# Rock draw Rock

# Paper lost Scissors
# paper draw paper

# Scissors draw Scissors
# Scissors wins paper 
# Scissors lost rock

if user_input == 0: # Rock
    print('El usuario selecciono Roca')
    if pc_choose_index == 0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("The game ended in a tie.")
    elif pc_choose_index == 1: # paper
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose")
    else:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win")
        
elif user_input == 1: # Paper
    print("El usuario selecciono Papel")
    if pc_choose_index == 0:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You won")
    elif pc_choose_index == 1: # paper
        print(paper)
        print("Computer chose:")
        print(paper)
        print("The game ended in a tie.")
    else:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose")
        
elif user_input == 2: # Scissors
    print("El usuario seleciono Tijeras!")
    if pc_choose_index == 0: # rock
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose")
    elif pc_choose_index == 1: # paper
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You won")
    else:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("The game ended in a tie.")
else:
    print("seleccionate un valor incorrecto Bye Bye, Take care!! 😎")



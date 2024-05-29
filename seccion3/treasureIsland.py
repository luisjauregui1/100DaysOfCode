art_tresure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
'''

print(art_tresure)
print("Welcome to Tresure Island.")
print("Your mision is to find the tresure")

input_user = input('You\'re at cross road. Where do you wanto to go? Type "left or "Right"\n').lower()

if input_user == "left":
    
    input_user = input(
        'You came to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swin across.\n').lower()
    
    if input_user == 'wait':
        
        input_user = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n").lower()
        if input_user == 'yellow':
            print("You Win!")
        elif input_user == 'red':
            print("Burned by fire Game Over!")
        elif input_user == 'blue':
            print("Eaten bu beasts. Game Over!")
        else:
            print("You chose a door that does't exist. Game Over!")

    else:
        print("Game over!")
else:
    print('You Fell into a hole. Game Over!')





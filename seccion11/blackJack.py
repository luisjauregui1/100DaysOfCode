import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def pc_choise():
    jugada = []
    for _ in range(2):
        seleccion = random.choice(cards)
        jugada.append(seleccion)
        
    

    
    return f"Suma de lista jugada = {jugada} es: {sum(jugada)}"

def run_game():
    pass

print(pc_choise())


# user_input = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")



    
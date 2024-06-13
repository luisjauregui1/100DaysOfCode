from data import data
from art import logo, vs
import random
import os


def indices_de_juego():
    indices_index = [] # indices nuevos para el seleccionado de opciones

    for i in range(0, 50):
        indices_index.append(i)

    random.shuffle(indices_index)
    
    return indices_index


def juego(): 
    
    index_game = indices_de_juego()
    
    for i in range(0,49):
        os.system('cls')
        print(logo)
        print(f'Compate: A: {data[index_game[i]]["name"]}, a {data[index_game[i]]["description"]}, from {data[index_game[i]]["country"]}.')
        print(vs)
        print(f'Compate: B: {data[index_game[i+1]]["name"]}, a {data[index_game[i+1]]["description"]}, from {data[index_game[i+1]]["country"]}.')
        
        valor_a = data[index_game[i]]['follower_count']
        valor_b = data[index_game[i+1]]['follower_count']
        

        user_input = input('Quien tiene mas seguidores? A o B: ').lower()
        


        if user_input == "a":
            # comparamos con b
            if valor_a > valor_b:
                continue
            else:
                return False
                
        elif user_input == 'b':
            # comparmos con a
            if valor_b > valor_a:
                continue
            else:
                return False
            
    
juego1 = juego()

if juego1 == False:
    os.system('cls')
    print('Perdiste')
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
        print(f'Lista de indices={index_game}')
        print(f'Compate: A: {data[index_game[i]]["name"]}, a {data[index_game[i]]["description"]}, from {data[index_game[i]]["country"]}.')
        print(vs)
        print(f'Compate: B: {data[index_game[i+1]]["name"]}, a {data[index_game[i+1]]["description"]}, from {data[index_game[i+1]]["country"]}.')
        
        valor_a = data[index_game[i]]['follower_count']
        valor_b = data[index_game[i+1]]['follower_count']
        print(f'Valor A={valor_a}, B={valor_b}')

        user_input = input('Quien tine mas seguidores? A o B: ').lower()
        


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
            
    
juego()
# comparar el resulatdo con los valores 
# en este caso son seguidores y que deberia pasar 
# A ó B son las opciones


"""
En que consiste el juego en seleccionar una opcion de la lista de data, son 50 opciones en total

tenemos que imprimir el logo

despues la primer opcion
    plantilla de impresion
    
    compare: A: Shakira, a Musican, from Colombia.
    data:      name        description    country

imprir el vs

imprimir la segunad opcion

    compare: A: Zendaya, a Actress and Musican, from Usa.
    data:      name            description       Country

el input donde selecciona mayor o menor ? 

si esta bien continuar, 
si es incorrecto 
    imprimir el score y terminar el juego

"""
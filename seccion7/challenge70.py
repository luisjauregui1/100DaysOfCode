import random
import os

word_list = ["ardvark", "baboon", "camel"]

# Esta funcion recibe palabra y el caracter para retornarnos los indices de la letra a buscar. si no existe retorna un None


def indices_letra(palabra, caracter):
    indices = []
    for index in range(len(palabra)):
        if chose_word[index] == caracter:
            indices.append(index)

    if len(indices) == 0:
        print("La letra no existe")
    else:
        return indices

# Esta funcion toma la palabra y la remplaza por guiones ['_']


def mostrar_guiones(chose_word):
    display = []

    for _ in chose_word:
        display += "_"

    return display

# Esta funcion es para actualizar la lista ▲ ya creada
# recibe los indices a remplazr y la lista


def actualizar_guiones(indices, display):

    print('Actualizar_guiones')

    if indices == None:

        print("Esa letra no existe")
    else:
        for _ in indices:
            display[_] = guess

    return display


# Monito
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# Seleccionamos la palabra al azar
chose_word = random.choice(word_list)
palabra_comparar = list(chose_word)

# vidas totales del juego
lifes = 7
# Empezamos el Juego
print('Comenzamos')
# Creamos la lista de guiones
guiones_lista = mostrar_guiones(chose_word)
guiones_actualizar = guiones_lista[:]
print(f"Plabra: {guiones_lista} ")

while lifes > 0:
    
    # Pedimos la letra del usuario!
    guess = input("Dame tu letra:").lower()  #
    os.system('cls')
    # Crear Indices
    indices_de_lista = indices_letra(
        chose_word, guess)  # Recibe Palabra Y caracter

    # si la letra no existe en la palabra restamos una vida y salimos a la siguente iteracion
    if indices_de_lista == None:
        lifes -= 1
        print(f"Ohh no:\n {stages[lifes]}")
    # si la letra si existe actualizamos la lista con la letra
    elif indices_de_lista:   # Actualizar Lista
        # Actualizar lista con letra
        guiones_actualizar = actualizar_guiones(indices_de_lista, guiones_lista)
        print(' '.join(guiones_actualizar))

    
    if lifes == 0:
        print('Perdiste no tienes mas vidas ):')
        break
    elif palabra_comparar == guiones_actualizar:
        print("Ganaste!!!")
        print(f'La Plabara es: {''.join(guiones_actualizar)}')
        break
    
    
    input("Presiona Enter para continuar...")

    # Imprimir Lista!

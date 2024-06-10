import random
import os

def juego(vidas, numero_pc):

    while vidas > 0:

        print(f'------Tienes {vidas} vidas-----')
        entrada_user = int(input('Dame tu numero:'))

        if entrada_user == numero_pc:
            os.system('cls')
            print(f'El numero es: {numero_pc}')
            return True

        elif numero_pc > entrada_user:
            print("El numero es mayor")
            vidas -= 1
        elif numero_pc < entrada_user:
            print("El numero es menor")
            vidas -= 1

        if vidas == 0:
            os.system('cls')
            print(f'El numero era: {numero_pc}')
            return False


# numero seleccionado para juego
numero_seleccionado = random.randint(1,100)
facil = 10
dificil = 5

entrada_user = input("Que difucultad.(Facil=F,Dificil=D)? ").lower()

if entrada_user == 'f':
    juego_f = juego(facil, numero_seleccionado)
    if juego_f == True:
        print('haz ganado')
    else:
        print('Haz perdido')
elif entrada_user == 'd':
    juego_d = juego(dificil, numero_seleccionado)
    if juego_d == True:
        print('haz ganado')
    else:
        print('Haz perdido')
else:
    print('NO es valido')


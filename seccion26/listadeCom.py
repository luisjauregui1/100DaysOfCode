# # listas de comprension

# # Ejemplo 
# numbers = [1,2,3,4,5]
# new_list = []
# for n in numbers:
#     add_1 = n + 1
#     new_list.append(add_1)    

# print(new_list)

# # Como es en forma de lista de compresion
# nueva_lista = [i + 1 for i in numbers ]
# print(nueva_lista)

# # test
# name = "Angela"
# new_letters = [letter for letter in name]
# print(new_letters)

# # por 2
# por_2_lista =[n * 2 for n in range(1,5)]
# print(por_2_lista)

# # if test
# names = ["Luis", "Fer", "Lola", "Dave", "Valeria", "Chango"]

# short_names = [name for name in names if len(name) < 5]
# upper_names = [name.upper() for name in names if len(name) > 5]
# print(short_names)
# print(upper_names)

list_of_strings = ['1', ' 1', ' 2', ' 3', ' 5', ' 8', ' 13', ' 21', ' 34', ' 55']

enteros = [int(numero) for numero in list_of_strings]
resultado = [numero for numero in enteros if numero % 2 == 0]

print(enteros)
print(resultado)
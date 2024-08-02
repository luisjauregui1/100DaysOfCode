# leer los documentos y crear las listas

# Rutas
txt1_ruta = 'C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion26/ejercicios/txt1.txt'
txt2_ruta = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion26/ejercicios/txt2.txt"


with open(txt1_ruta) as file1:
  list1 = file1.readlines()

with open(txt2_ruta) as file2:
  list2 = file2.readlines()

result = [int(num) for num in list1 if num in list2]

# Write your code above 👆
print(result)
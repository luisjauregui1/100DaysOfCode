with open("C:\\Users\\Gustavo\\Documents\\Programacion\\100DaysOfCode\\seccion24\\my_file.txt") as file:    
    contents = file.read()
    print(contents)
    file.close()


def funcion_numero():
    with open('C:\\Users\\Gustavo\\Documents\\Programacion\\100DaysOfCode\\seccion20\\data.txt', mode='r') as file:
        contenido = file.read()    
    return contenido


numero =funcion_numero()

print(numero)
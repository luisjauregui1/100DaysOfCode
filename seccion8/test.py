# Lista de ejemplo
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Número de posiciones a desplazar
desplazamiento = 10

# Elemento inicial
elemento = 'd'

# Obtener la posición del elemento en la lista
posicion_inicial = lista.index(elemento)

# Calcular la nueva posición usando el operador módulo
nueva_posicion = (posicion_inicial + desplazamiento) % len(lista)

# Obtener el nuevo elemento en la lista
nuevo_elemento = lista[nueva_posicion]

# Mostrar resultados
print("Posición inicial:", posicion_inicial)  # Resultado: 3
print("Nueva posición:", nueva_posicion)      # Resultado: 5
print("Nuevo elemento:", nuevo_elemento)      # Resultado: f

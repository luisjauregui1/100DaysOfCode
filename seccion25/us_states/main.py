import turtle
import pandas

# Configuracion de patalla
screen = turtle.Screen()
screen.title('U.S. States Game')

# Rutas, imagen y archivo csv
image = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion25/us_states/blank_states_img.gif"
ruta = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion25/us_states/50_states.csv"

# leer los datos del archivo csv
estados = pandas.read_csv(ruta)

# Configurar la imgaen como fondo
screen.addshape(image)
turtle.shape(image)

# Crear un objeto de turtle para escribir
escritor = turtle.Turtle()
escritor.penup()
escritor.hideturtle()


# Normaliza los nombre de los estados en el csv
estados['state'] = estados['state'].str.strip().str.lower()

# crear un conjunto para almacer n los estasdo ingresados
estados_correctos = set()

while True:
    
    if len(estados_correctos) == 50:
        print("bien hecho, todos los estados terminados")
        escritor.goto(-44,250)
        escritor.write("Bien Hecho... Terminaste", align="center", font=("Arial",16, "normal"))
    
    entrada_estado = screen.textinput(title=f"Estados correctos {len(estados_correctos)}/50", prompt="Ingresa tu estado?")
    
    if entrada_estado is None or entrada_estado == "Exit":
        break
    
    # Normalizo el estado ingresado
    entrada_estado = entrada_estado.strip().lower()
    
    # Verficar si el estado es valido y no ha sido ingresado anteriormente
    if entrada_estado in estados['state'].values and entrada_estado not in estados_correctos:
        # Agregar el estado al conjunto de estados correctos
        estados_correctos.add(entrada_estado)
        
        # obten las coordenadas del estado
        estado_info = estados[estados['state'] == entrada_estado]
        # Use int(ser.iloc[0]) instead
        x = int(estado_info['x'].iloc[0])
        y = int(estado_info['y'].iloc[0])
            
        # Mover el esciroter a las coordenadas y escirbi el nombre del estado
        escritor.goto(x,y)
        escritor.write(entrada_estado.capitalize(), align="center", font=("Arial", 8, "normal"))


# salvar los estados faltantes.
lista_50_state = estados["state"].str.strip().to_list()
lista_paises_faltantes = []
list_estados_correctos = list(estados_correctos)  # Corrección aquí: no sobrescribas con una lista vacía

for state in lista_50_state:
    if state not in list_estados_correctos:
        lista_paises_faltantes.append(state)
    
        
# creamos el csv

nuevo_csv = pandas.DataFrame(lista_paises_faltantes)
nuevo_csv.to_csv("states_missing.csv")



# mi version 👆

# angela version 👇

# import turtle
# import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)

# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_states = []

# while len(guessed_states) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
#                                     prompt="What's another state's name?").title()
#     if answer_state == "Exit":
#         missing_states = []
#         for state in all_states:
#             if state not in guessed_states:
#                 missing_states.append(state)
#         new_data = pandas.DataFrame(missing_states)
#         new_data.to_csv("states_to_learn.csv")
#         break
#     if answer_state in all_states:
#         guessed_states.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(state_data.x.item(), state_data.y.item())
#         t.write(answer_state)


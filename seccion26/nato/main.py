import pandas

ruta_csv = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion26/nato/alphabet.csv"

pd = pandas.read_csv(ruta_csv)
data = pandas.read_csv(ruta_csv)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format: 
# {"A": "Alfa", "B": "Bravo"}
diccionario = pd.set_index('letter')["code"].to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_word = input("Enter a word: ")
letras = list(input_word.upper())


claves = diccionario.keys()
valores = []

for letra in letras:
    if letra in claves:
        valores.append(diccionario[letra])

print(valores)

# MI CODIGO 👆
# CODIGO MAESTER 👇

# TODO 1
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2
word = input("enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
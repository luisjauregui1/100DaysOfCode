import pandas

ruta_csv_nato = "C:\\Users\\Gustavo\\Documents\\codigo\\100DaysOfCode\\seccion26\\nato\\alphabet.csv"

data = pandas.read_csv(ruta_csv_nato)

# TODO 1.  Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
        

generate_phonetic()
    
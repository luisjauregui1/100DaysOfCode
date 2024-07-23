import pandas

ruta = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion25/central_park/central_park.csv"

datos = pandas.read_csv(ruta)

color_counts = datos["Primary Fur Color"].value_counts(dropna=False)

nuevo_csv = pandas.DataFrame(color_counts)

nuevo_csv.to_csv('color.csv')
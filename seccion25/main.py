# TODO: created a list with values of weather_data.csv
# import pandas
# ruta = "C:/Users/Gustavo/Documents/Programacion/100DaysOfCode/seccion25/weather_data.csv"

# lista = []

# with open(ruta) as data:
#     for line in data:
#         linea_sin_n = line.strip()
#         lista.append(linea_sin_n)

# print(lista)

# import csv

# with open(ruta) as data_file:
#     data = csv.reader(data_file)
#     temperatura = []
#     for row in data:
#         if row[1] != "temp":
#             temperatura.append(int(row[1]))
#     print(temperatura)


# data = pandas.read_csv(ruta)

# print(data['temp'].mean())
# maximo_valor = data["temp"].max()

# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "monday"])

# max_row = data[data["temp"] == data["temp"].max()]

# monday = data[data.day == "monday"]

# monday = data[data.day == 'monday']
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 + 32
# print(monday_temp_f)

# # create a dataframe from screatch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }

# datas_dict = pandas.DataFrame(data_dict)

# datas_dict.to_csv("new_data.csv")


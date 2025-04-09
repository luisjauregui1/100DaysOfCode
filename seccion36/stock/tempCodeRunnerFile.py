dato_temporal = newapi()

with open("data_api.txt" ,"w") as file:
    json.dump(dato_temporal, file, indent=4)

print("Json guardado correctamente en data.txt")
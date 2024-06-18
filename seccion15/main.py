MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

monedas = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01
}


resources = {
    "water": 50,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1 terminal preguntar que te gustaria ? (expresso/Latte/ Cappuccino):
def seleccion_opciones_cafe():
    "Preguntamos por el tipo de cafe y retornamos ese valor"
    entrada_cafe = input(
        'selecciona tu cafe (espresso/Latte/ Cappuccion): ').lower()
    return entrada_cafe


# TODO: 2 Apagar la maquina de caffe ingresado off

def apagar_maquina():
    "Apagar maquina, retorna valor_maquina = apagado"
    valor_maquina = "Apagado"
    return valor_maquina

# TODO: 3 print reporte => agua: 100ml , milk 50
#          cuando el usuario ingreser report en la terminal , generamos el reporte


def reporte_cantidades():
    for item in resources:
        print(f'{item}: {resources[item]}')

# TODO: 4 Checar si tenemos los recursos suficientes.


def recursos_para_hacer_cafe(cafe):
    "Comparara los ingredientes del cafe seleccionado con la receta"
    material = []
    cantidad = []
    disponibilidad = True
    for item in MENU[cafe]['ingredients']:
        if MENU[cafe]['ingredients'][item] <= resources[item]:
            # si alncanz para el valor de la iteracino
            print(f'if: Ingredientes para cafe:{MENU[cafe]['ingredients'][item]}, recursos de maquina: {resources[item]}')
        elif MENU[cafe]['ingredients'][item] > resources[item]:
            # no alcanza para completar la resta
            print(f'elfi: Ingredientes para cafe:{MENU[cafe]['ingredients'][item]}, recursos de maquina: {resources[item]}')
            material.append(item)
            cantidad.append(resources[item])
    
    if len(material) == 0:
        return material, disponibilidad
    else:  
        return material, cantidad
            

# print(f'valores que tengo en menu: {MENU["cappuccino"]['ingredients']['milk']}')
# print(f'mis recursos en maquina: {resources["milk"]}')

cafe_seleccionado = seleccion_opciones_cafe()

material, cantidad = recursos_para_hacer_cafe(cafe_seleccionado)

print(f'Falta material: {material} , cantidad en maquina: {cantidad}')

# TODO: 5 Proceso de mondeas
#          si hay suficientes recursos para hacer un vevida seleccionada , el progrmada deberia imprimr que inserte monedas
#          recordar los cuartos 0.25, dimes= 0.10, nickels = 0.05, pennies = 0.01
#          Calcular el valor monetario de las mondeas insertadas. ejemplo
#           E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO: 6 Check transaction successful?
# Checar que el usuario inserte el precio de la vedida, la cantidad correcta
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “​Sorry that's not enough money. Money refunded.​
#  ”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.

# TODO: 7 Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b.Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

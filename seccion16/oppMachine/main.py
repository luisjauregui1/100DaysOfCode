from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maquina_monedas = MoneyMachine()
crear_cafe = CoffeeMaker()
menu = Menu()
is_on = True


while is_on:
    opciones = menu.get_items()
    choice = input(f'What would you like? ({opciones}): ')
    if choice == "off":
        is_on = False
    elif choice == "report":
        maquina_monedas.report()
        crear_cafe.report()
    else:
        drink = menu.find_drink(choice)
        if crear_cafe.is_resource_sufficient(drink) and maquina_monedas.make_payment(drink.cost):
            crear_cafe.make_coffee(drink)

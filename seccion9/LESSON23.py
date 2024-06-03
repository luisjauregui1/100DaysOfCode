# Instructions
# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. Your job is to create a function that can add new countries to this list.

# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
# DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

# Example Input
# Brazil
# 5
# ["Sao Paulo", "Rio de Janeiro"]
# Example Output
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.
# Hint
# Look at the function call above to see what the name of the function should be.

# The inputs for the function are positional arguments. The order is very important.

# Feel free to choose your own parameter names.


country = input()  # Add country name
visits = int(input())  # Number of visits
list_of_cities = eval(input())  # create list from formatted string

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log.


def add_new_country(name, times_visited, cities_visited):
    dic_nuevo = {}
    dic_nuevo["country"] = name
    dic_nuevo["visits"] = times_visited
    dic_nuevo["cities"] = cities_visited
        
    travel_log.append(dic_nuevo)



# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {
    travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")



# nota personal
"""
Como tenemos el dicionario o multiples diccionarios dentro de una lista solo tenemos que crear un diccionario
nuevo y este lo agregamos a la lista

    ejemplo : 
        Brazil
        5
        ["Sao Paulo", "Rio de Janeiro"]
    estos son los valorres y las claves son las mismas     
    
    
    "country":
    "visits": 
    "cities": esto es una lista
    
"""
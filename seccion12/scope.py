# Scope

# enemies = 1 

# def increase_enemies():
#     enemies = 2
#     print(f'enemies inside fuction: {enemies}')


# increase_enemies()
# print(f"enemies outside fuction: {enemies}")

# Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
# print(potion_strengh)

# Global Scope
# player_health = 10

# def drink_potion():
#     potion_strenght = 2
#     print(player_health)
    
# drink_potion()
# print(player_health)


# There is no Block Scope

# game_level = 3

# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Aline"]

#     if game_level < 5:
#         new_enemy = enemies[0]
    
#     print(new_enemy)



enemies = 1

def increase_enemies():
    enemies = "zombie"

    print(f"enemies inside fuction: {enemies}")
    
increase_enemies()
print(f'enemies outside fuction: {enemies}')


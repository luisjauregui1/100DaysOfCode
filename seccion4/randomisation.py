import random


random_integer = random.randint(1,10)

# 0.000000 - 0.999999999
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")



options = random.randint(1,2)    

if options == 1:
    print('Heads')
elif options == 2:
    print('Tails')


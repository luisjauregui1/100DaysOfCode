from data import data
from art import logo, vs
import random


indices_index = []

for i in range(0, 50):
    indices_index.append(i)


random.shuffle(indices_index)

valor = []

for i in range(0, 50):
    valor.append(data[i]['follower_count'])
            

print(valor)

gemelos = 0

for i in range(len(valor)-1):
    if valor[i] == valor[i+1]:
        print('Son gemelos')
        gemelos += 1
        
print(gemelos)
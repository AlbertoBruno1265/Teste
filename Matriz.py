#Este programa gera uma matriz com valores aleatórios
from random import randint
matriz = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
        matriz[i][j] = randint(1, 9)

for i in range(len(matriz[0])):
    print(matriz[i])

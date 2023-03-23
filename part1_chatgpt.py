import random
import time
import os

# matriz 10x10
matriz = [[0 for x in range(10)] for y in range(10)]

# preenche a matriz com números de 1 a 100 sem repetir
numeros = list(range(1, 101))
random.shuffle(numeros)
for i in range(10):
    for j in range(10):
        matriz[i][j] = numeros.pop()

# verifica se tem números repetidos
for i in range(10):
    for j in range(10):
        if matriz.count(matriz[i][j]) > 1:
            print(f"Número repetido {matriz[i][j]} na posição {i},{j}")

# próxima matriz
matriz_vazia = [[0 for x in range(10)] for y in range(10)]

num = 1
tentativas = 50
chance = 1
while num <= 100 and tentativas > 0:
    chance_de_acerto = chance / 100 * 100
    caixax, caixay = random.sample(range(10), 2)

    if matriz_vazia[caixax][caixay] == 0:
        matriz_vazia[caixax][caixay] = matriz[caixax][caixay]
        os.system("cls")
        print(f"Preso {num}\n")
        for i in range(10):
            for j in range(10):
                print(matriz_vazia[i][j], end="    ")
            print()

        print(f"Tentativa {101 - num}")
        print("Chance de acerto {:.2f}%".format(chance_de_acerto))

        if matriz_vazia[caixax][caixay] == num:
            num += 1
            matriz_vazia = [[0 for x in range(10)] for y in range(10)]
            chance = 1
        else:
            chance += 1

        time.sleep(2)
        tentativas -= 1

if num > 100:
    print("Ganhou!")
else:
    print("Perdeu!")

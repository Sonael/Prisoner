import random
import time
import os

#matriz 10x10
matriz = [[0 for x in range(10)] for y in range(10)]

#preenche a matriz com numeros de 1 a 100 sem repetir
lista = []
for i in range(10):
    for j in range(10):
        num = random.randint(1,100)
        while num in lista:
            num = random.randint(1,100)
        lista.append(num)
        matriz[i][j] = num

        



#verificar se tem numeros repetidos
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if matriz[i][j] == matriz[k][l] and i != k and j != l:
                    print(f"repetido na posicao {i},{j} e {k},{l}")


#proxima matriz
matriz_vazia = [[0 for x in range(10)] for y in range(10)]


cont = 1
partida = False
num = 1
chance = 1
while(num != 100):
    chance_de_acerto = (chance/100)*100
    caixax, caixay = random.randint(0,9), random.randint(0,9)
    while(matriz_vazia[caixax][caixay] != 0):
        caixax, caixay = random.randint(0,9), random.randint(0,9)

    matriz_vazia[caixax][caixay] = matriz[caixax][caixay]
    print(f"Preso {num} \n")
    for i in range(10):
        for j in range(10):
            print(matriz_vazia[i][j], end="    ")
        print()

    print(f"tentativa {cont}")
    print("chance de acerto {:.2f}%".format(chance_de_acerto))
    if(matriz_vazia[caixax][caixay] == num):
        partida = True
        num += 1
        matriz_vazia = [[0 for x in range(10)] for y in range(10)]
        cont = 0
        chance = 1
    elif(cont>=50):
        partida = False
        break

    
    time.sleep(0.5)
    os.system("cls")
    cont+=1
    chance+=1



if(partida):
    print("ganhou")
else:
    print("perdeu")
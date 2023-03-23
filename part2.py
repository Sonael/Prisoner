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
x = num
while(num != 100):
    chance_de_acerto = (chance/100)*100
    y = int(x/10)
    w = (x%10)

    if w == 0:
        w = 10
    else:
        w-=1
    if y == 0:
        y = 1

    for i in range(y):
        for j in range(w):
            if(w == 1):
                w = 0
            if(y == 1):
                y = 0
            caixa = matriz[i][j]



    matriz_vazia[y][w] = caixa
    x = caixa
    print(f"Preso {num} \n")
    for i in range(10):
        for j in range(10):
            print(matriz_vazia[i][j], end="    ")
        print()

    print(f"tentativa {cont}")
    print("chance de acerto {:.2f}%".format(chance_de_acerto))
    
    print(x)
    print(f"posicao {y},{w}")
    time.sleep(5)
    os.system("cls")
    cont+=1
    chance+=1
    
    
    
    if(matriz_vazia[y][w] == num):
        partida = True
        num += 1
        matriz_vazia = [[0 for x in range(10)] for y in range(10)]
        cont = 0
        chance = 1
        x = num
    elif(cont>=50):
        partida = False
        break

    




if(partida):
    print("ganhou")
else:
    print("perdeu")
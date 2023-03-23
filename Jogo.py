import random
import PySimpleGUI as sg
from time import sleep


sg.theme('DarkGreen3')



numero = 1

#popup input num_max e attempts
sg.popup('O objetivo do jogo é descobrir a posição de cada número de 1 a 100 na matriz. Cada vez que você acertar um número, ele será revelado e você poderá continuar tentando adivinhar a posição do próximo. Você pode definir o número de tentativas para cada número e também até que número você ira jogar. Boa sorte!')

layout = [
    [sg.Text('Número Máximo:'), sg.InputText()],
    [sg.Text('Tentativas:'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')]
    ]

window = sg.Window('Input', layout)
event, values = window.read()

while True:

    #parar o programa se o usuário clicar em 'Cancel' ou fechar a janela
    if event == 'Cancel' or event == sg.WIN_CLOSED:
        window.close()
        exit()

    try:
        num_max = int(values[0])
        attempts = int(values[1])
        if attempts > 100:
            sg.popup('O número de tentativas não pode ser maior que 100.')
            event, values = window.read()
            continue
        elif num_max > 100:
            sg.popup('O número máximo não pode ser maior que 100.')
            event, values = window.read()
            continue
        break
    except (ValueError, TypeError):
        sg.popup('Por favor, digite um número válido.')
        event, values = window.read()

window.close()


# matriz 10x10
matrix = [[0 for x in range(10)] for y in range(10)]

# função preenche a matriz com números de 1 a 100 sem repetir
def fill_matrix():
    numeros = list(range(1, 101))
    random.shuffle(numeros)
    for i in range(10):
        for j in range(10):
            matrix[i][j] = numeros.pop()


fill_matrix()

# Define o tema da interface gráfica


# Cria a lista de botões


# Cria o layout da janela
layout = [[sg.Text('Jogo de Descoberta', font=('Helvetica', 20), justification='center', size=(50, 1))],
          [sg.Text('Tentativas Restantes: {}'.format(attempts), font=('Helvetica', 14), justification='center', key='tentativas', size=(70,1)),],       
          [sg.Text('Número Atual: 1', font=('Helvetica', 14), justification='center', key='current_number', size=(70,1))],
          [sg.Text('Selecione uma célula para revelar o número:', font=('Helvetica', 14), justification='center', size=(70,1))]]

def create_buttons():
    buttons = [[sg.Button('', size=(7,2), key=(i,j), pad=(1,1), button_color='grey') for j in range(10)] for i in range(10)]
    for row in buttons:
        layout.append(row)

create_buttons()

#reset button
def reset_buttons():
    for i in range(10):
        for j in range(10):
            window[(i,j)].update(button_color=('white', 'grey'))
            window[(i,j)].update('')


buttons_row = [sg.Button('Desistir', font=('Helvetica', 14), key='giveup', size=(15,2)),    sg.Button('Próximo', font=('Helvetica', 14), key='next', visible=False,size=(15,2))]

layout.append(buttons_row)


# Cria a janela
window = sg.Window('Jogo de Descoberta', layout, size=(800, 800), resizable=True, finalize=True)

# Armazena as coordenadas do número na matriz
def find_num_coords():
    num_coords = None
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == numero:
                num_coords = (i,j)
                break
        if num_coords:
            break
    return num_coords


def update_num(value):
    window[event].update(value)
    window[event].update(button_color=('white', 'red'))

def highlight_num():
    for i in range(10):
        for j in range(10):
            if (i,j) == num_coords:
                window[(i,j)].update(button_color=('white', 'green'))
            else:
                value = matrix[i][j]
                window[(i,j)].update(value)
                window[(i,j)].update(button_color=('white', 'red'))

num_coords = find_num_coords()
print(num_coords[0]+1, num_coords[1]+1)

# Loop principal do jogo
win = False
clicked = set()  # set of clicked button keys
tentativas = attempts

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        win = 'Fechar'
        break
    elif event == 'giveup':
        value = matrix[num_coords[0]][ num_coords[1]]
        window[num_coords].update(value)
        highlight_num()
        break
    elif event == 'next':
            window['next'].update(visible=False)
            fill_matrix()
            create_buttons()
            numero += 1
            window['current_number'].update('Número Atual: {}'.format(numero))
            num_coords = find_num_coords()
            print(num_coords[0]+1, num_coords[1]+1)
            tentativas = attempts
            window['tentativas'].update('Tentativas Restantes: {}'.format(tentativas))
            reset_buttons()
            clicked.clear()
    elif event != 'tentativas' and event not in clicked:  # check if button has been clicked before
        clicked.add(event)  # add button key to clicked set
        tentativas -= 1
        window['tentativas'].update('Tentativas Restantes: {}'.format(tentativas))
        i, j = event
        value = matrix[i][j]
        print(value)

        if value == numero:
            if numero == num_max:
                win = True
                window[num_coords].update(value)
                highlight_num()
                break
            window[num_coords].update(value)
            highlight_num()
            #adicionar botão "proximo"
            window['next'].update(visible=True)
        
        elif tentativas == 0:
            value = matrix[num_coords[0]][ num_coords[1]]
            window[num_coords].update(value)
            highlight_num()
            break
            
        else:
            window[event].update(value)
            window[event].update(button_color=('white', 'red'))
            
    

# Exibe a mensagem de vitória ou derrota com a posição do número 1
if win == 'Fechar':
    sg.popup('Obrigado por jogar!')
else:
    if win:
        sg.popup('Você ganhou!')
    else:
        sg.popup('Você perdeu! O número {} estava na posição ({}, {}).'.format(numero,num_coords[0]+1, num_coords[1]+1))

# Fecha
window.close()
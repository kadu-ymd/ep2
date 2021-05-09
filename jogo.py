from funcs import *
from colorama import Fore, Style

print(print_jogo())

verif_ind = True
verif_mov = True

naipes = ['♠', '♥', '♦', '♣']
cores = ['\33[91m', '\33[92m', '\33[93m', '\33[94m']
cartas = rand_lista(cria_baralho())
i = 1

baralho = []

for carta in cartas:
    if extrai_naipe(carta) == '♠':
        print('{0}. {1}'.format(i, (Fore.RED + carta + Style.RESET_ALL)))
        baralho.append(Fore.RED + carta + Style.RESET_ALL)
    if extrai_naipe(carta) == '♥':
        print('{0}. {1}'.format(i, (Fore.YELLOW + carta + Style.RESET_ALL)))
        baralho.append(Fore.YELLOW + carta + Style.RESET_ALL)
    if extrai_naipe(carta) == '♦':
        print('{0}. {1}'.format(i, (Fore.GREEN + carta + Style.RESET_ALL)))
        baralho.append(Fore.GREEN + carta + Style.RESET_ALL)
    if extrai_naipe(carta) == '♣':
        print('{0}. {1}'.format(i, (Fore.BLUE + carta + Style.RESET_ALL)))
        baralho.append(Fore.BLUE + carta + Style.RESET_ALL)
    i += 1

posicao = int(input('\nEscolha uma carta (digite um número entre 1 e 52): '))
while verif_ind:
    if not posicao in range(1, len(cartas) + 1):
        posicao = int(input('Posição inválida. Por favor, digite um número entre 1 e 52): '))  
    else:
        verif_ind = False    

# COMEÇO DO JOGO
while verif_mov:
    if lista_movimentos_possiveis(cartas, posicao - 1) == []:
        posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52: '.format(baralho[posicao - 1])))
    elif lista_movimentos_possiveis(cartas, posicao) == [1, 3]:
        indice = int(input('Sobre qual carta você quer empilhar o {0}?\n'.format(baralho[posicao - 1])))
        print('1. {0}'.format(baralho[posicao - 1 - 1]))
        print('2. {0}'.format(baralho[posicao - 1 - 3]))
    elif lista_movimentos_possiveis(cartas, posicao - 1) == [1]:
        empilha(baralho, posicao - 1, posicao - 1 - 1)
    elif lista_movimentos_possiveis(cartas, posicao - 1) == [3]:
        empilha(baralho, posicao - 1, posicao - 1 - 3)
    else:
        verif_mov = False
        if len(baralho) == 1:
            print('Vitória! Você é muito bom! :D')
        else:
            print('Derrota! Tente mais uma vez! D:')

# cond = True
# while verif_mov:
#     if (condição):
#         baralho = empilha(baralho, origem, destino)
#     else:
#         cond = False

# while verif_mov:
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == []:
#         posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52: '.format(baralho[posicao - 1])))
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [1]:
#         funcs.empilha(baralho, posicao - 1, posicao - 2)
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [3]:
#         funcs.empilha(baralho, posicao - 1, posicao - 4)
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [1, 3]:
#         indice = int(input('Sobre qual carta você quer empilhar o {0}?'.format(baralho[posicao - 1])))

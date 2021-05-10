from funcs import *
from colorama import Fore, Style

print(print_jogo())

quer_jogar = True

baralho = []

# COMEÇO DO JOGO
while quer_jogar:
    cartas = rand_lista(cria_baralho())
    for carta in cartas:
        baralho.append(carta)
    while possui_movimentos_possiveis(baralho) == True:
        posicao_ = True
        print_cor(baralho, 1)
        posicao = int(input('\nEscolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho))))
        print()

        while posicao_:
            if not posicao in range(1, len(cartas) + 1):
                posicao = int(input('Posição inválida. Por favor, digite um número entre 1 e {0}): '.format(len(baralho))))
                print()
            else:
                posicao_ = False
                
        while lista_movimentos_possiveis(baralho, posicao - 1) == []: 
            posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}: '.format(cor_carta(baralho[posicao - 1]), len(baralho))))
            print()
            if not posicao in range(1, len(cartas) + 1):
                posicao = int(input('Posição inválida. Por favor, digite um número entre 1 e {0}): '.format(len(baralho))))
                print()
            else:
                posicao_ = False

        if lista_movimentos_possiveis(baralho, posicao - 1) == [1, 3]:
            print('Sobre qual carta você quer empilhar o {0}? '.format(cor_carta(baralho[posicao - 1])))
            print('1. {0}'.format(cor_carta(baralho[posicao - 2])))
            print('2. {0}'.format(cor_carta(baralho[posicao - 4])))
            qual = int(input('Digite aqui a posição: \n'))

            if qual == 1:
                baralho = empilha(baralho, posicao - 1, posicao - 2)
            elif qual == 2:
                baralho = empilha(baralho, posicao - 1, posicao - 4)
            else:
                while qual not in range(1, 3):
                    qual = int(input('Posição inválida. Por favor, digite 1 ou 2: '))
        
        elif lista_movimentos_possiveis(baralho, posicao - 1) == [1]:
            baralho = empilha(baralho, posicao - 1, posicao - 2)

        elif lista_movimentos_possiveis(baralho, posicao - 1) == [3]:
            baralho = empilha(baralho, posicao - 1, posicao - 4)
        
        if possui_movimentos_possiveis(baralho) == False:
            print('Você perdeu! :( \n')
            break

        if len(baralho) == 1:
            print('Você ganhou! :D \n')
            break

    resposta = input('Deseja jogar novamente? Digite "n" para "não" e qualquer outra coisa para "sim". ')
    if resposta == 'n':
        break

print('Obrigado por jogar! :D')
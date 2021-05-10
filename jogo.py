from funcs import *
from colorama import Fore, Style

print(print_jogo())

# CONDIÇÕES
posicao_ = True
quer_jogar = True
t1 = True
t2 = True
t3 = True
t4 = True
t5 = True

baralho = []

# COMEÇO DO JOGO
while quer_jogar:
    cartas = rand_lista(cria_baralho())
    for carta in cartas:
        baralho.append(carta)
    while possui_movimentos_possiveis(baralho) == True:
        print_cor(baralho, 1)
        while t1:
            try:
                posicao = int(input('\nEscolha uma carta (digite um número entre 1 e {0}): '.format(len(baralho))))
                t1 = False
            except ValueError:
                pass
        print()

        while posicao_:
            if not posicao in range(1, len(cartas) + 1):
                while t2:
                    try:
                        posicao = int(input('Posição inválida. Por favor, digite um número entre 1 e {0}): '.format(len(baralho))))
                        t2 = False
                    except ValueError:
                        pass
            else:
                posicao_ = False
                
        while lista_movimentos_possiveis(baralho, posicao - 1) == []: 
            while t3:
                try:
                    posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e {1}: '.format(cor_carta(baralho[posicao - 1]), len(baralho))))
                    t3 = False
                except ValueError:
                    pass
            print()

        if lista_movimentos_possiveis(baralho, posicao - 1) == [1, 3]:
            print('Sobre qual carta você quer empilhar o {0}? '.format(cor_carta(baralho[posicao - 1])))
            print('1. {0}'.format(cor_carta(baralho[posicao - 2])))
            print('2. {0}'.format(cor_carta(baralho[posicao - 4])))
            while t4:
                try:
                    qual = int(input('Digite aqui a posição: \n'))
                    t4 = False
                except ValueError:
                    pass
            if qual == 1:
                baralho = empilha(baralho, posicao - 1, posicao - 2)
            elif qual == 2:
                baralho = empilha(baralho, posicao - 1, posicao - 4)
            else:
                while qual not in range(1, 3):
                    while t5:
                        try:
                            qual = int(input('Posição inválida. Por favor, digite 1 ou 2: '))
                            t5 = False
                        except ValueError:
                            pass
        
        elif lista_movimentos_possiveis(baralho, posicao - 1) == [1]:
            baralho = empilha(baralho, posicao - 1, posicao - 2)
        
        elif lista_movimentos_possiveis(baralho, posicao - 1) == [3]:
            baralho = empilha(baralho, posicao - 1, posicao - 4)
        
        if possui_movimentos_possiveis(baralho) == False:
            print('Você perdeu! :( \n')
        
        if len(baralho) == 1:
            print('Você ganhou! :D \n')
    resposta = input('Deseja jogar novamente? Digite "n" para "não" e qualquer outra coisa para "sim". ')
    if resposta == 'n':
        break

print('Obrigado por jogar! :D')
from funcs import *

print('Paciência Acordeão')
print('==================\n')
print('Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha.\n')
print('{0}{1}{2}\n'.format('\033[1m', 'Regras do Jogo', '\033[0m'))
print('Existem apenas dois movimentos possíveis:\n')
print('1. Empilhar uma carta sobre a carta imediatamente anterior;')
print('2. Empilhar uma carta sobre a terceira carta anterior.\n')
print('Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida:\n')
print("1. As duas cartas possuem o mesmo valor ou")
print("2. As duas cartas possuem o mesmo naipe.\n")
print("Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada.\n")
print(input('Aperte [Enter] para continuar...'))

verif_ind = True

naipes = ['♠', '♥', '♦', '♣']
cores = ['\33[91m', '\33[92m', '\33[93m', '\33[94m']
baralho = rand_lista(cria_baralho())
i = 1

for carta in baralho:
    if extrai_naipe(carta) == '♠':
        print('{0}. {1}{2}{3}'.format(i, '\33[91m', carta, '\33[0m'))
    if extrai_naipe(carta) == '♥':
        print('{0}. {1}{2}{3}'.format(i, '\33[92m', carta, '\33[0m'))
    if extrai_naipe(carta) == '♦':
        print('{0}. {1}{2}{3}'.format(i, '\33[93m', carta, '\33[0m'))
    if extrai_naipe(carta) == '♣':
        print('{0}. {1}{2}{3}'.format(i, '\33[94m', carta, '\33[0m'))
    i += 1

indice = int(input('Escolha uma carta (digite um número entre 1 e 52): '))
while verif_ind:
    if not indice in range(1, 53):
        indice = int(input('Posição inválida. Por favor, digite um número entre 1 e 52): '))
    else:
        verif_ind = False

# if lista_movimentos_possiveis(baralho, indice) == []:
#     print('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52): '.format(carta))

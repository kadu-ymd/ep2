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

jogando = True

baralho = rand_lista(cria_baralho())
i = 1
for carta in baralho:
    print('{0}. {1}'.format(i, carta))
    i += 1

indice = int(input('Escolha uma carta (digite um número entre 1 e 52): '))
while jogando:
    if not (indice in range(1, 52)):
        indice = int(input('Posição inválida. Por favor, digite um número entre 1 e 52): '))
    else:
        jogando = False



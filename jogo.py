import funcs
import colorama

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
verif_mov = True

naipes = ['♠', '♥', '♦', '♣']
cores = ['\33[91m', '\33[92m', '\33[93m', '\33[94m']
cartas = funcs.rand_lista(funcs.cria_baralho())
i = 1

baralho = []

for carta in cartas:
    if funcs.extrai_naipe(carta) == '♠':
        print('{0}. {1}{2}{3}'.format(i, '\33[91m', carta, '\33[0m'))
        baralho.append('\33[91m' + carta + '\33[0m')
    if funcs.extrai_naipe(carta) == '♥':
        print('{0}. {1}{2}{3}'.format(i, '\33[92m', carta, '\33[0m'))
        baralho.append('\33[92m' + carta + '\33[0m')
    if funcs.extrai_naipe(carta) == '♦':
        print('{0}. {1}{2}{3}'.format(i, '\33[93m', carta, '\33[0m'))
        baralho.append('\33[93m' + carta + '\33[0m')
    if funcs.extrai_naipe(carta) == '♣':
        print('{0}. {1}{2}{3}'.format(i, '\33[94m', carta, '\33[0m'))
        baralho.append('\33[94m' + carta + '\33[0m')
    i += 1


posicao = int(input('Escolha uma carta (digite um número entre 1 e 52): '))
while verif_ind:
    if not posicao in range(1, len(cartas) + 1):
        posicao = int(input('Posição inválida. Por favor, digite um número entre 1 e 52): '))  
    else:
        verif_ind = False    

cartas_com_cor = []

# COMEÇO DO JOGO
while verif_mov:
    if funcs.lista_movimentos_possiveis(cartas, posicao) == []:
        posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52: '.format(baralho[posicao - 1])))
    elif funcs.lista_movimentos_possiveis(cartas, posicao) == [1]:
        funcs.empilha(baralho, posicao - 1, posicao - 2)
        
    elif funcs.lista_movimentos_possiveis(cartas, posicao) == [3]:
        funcs.empilha(baralho, posicao - 1, posicao - 4)
    else: 
        # funcs.lista_movimentos_possiveis(cartas, posicao) == [1, 3]:
        indice = int(input('Sobre qual carta você quer empilhar o {0}?'.format(baralho[posicao - 1])))
        print(Fore.YELLOW + '1. {0}{1}{2}'.format( baralho[posicao - 2]))
        print(Fore.RED + '1. {0}{1}{2}'.format( baralho[posicao - 2]))
        # print('2. {0}{1}{2}'.format('\33[93m', baralho[posicao - 4], '\33[0m'))
        # print(Fore.RED + 'some red text')

# while verif_mov:
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == []:
#         posicao = int(input('A carta {0} não pode ser movida. Por favor, digite um número entre 1 e 52: '.format(baralho[posicao - 1])))
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [1]:
#         funcs.empilha(baralho, posicao - 1, posicao - 2)
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [3]:
#         funcs.empilha(baralho, posicao - 1, posicao - 4)
#     if funcs.lista_movimentos_possiveis(cartas, posicao) == [1, 3]:
#         indice = int(input('Sobre qual carta você quer empilhar o {0}?'.format(baralho[posicao - 1])))

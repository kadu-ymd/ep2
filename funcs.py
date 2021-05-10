from colorama import Fore, Style
def cria_baralho():
    baralho = ['2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'A♠', 'J♠', 'Q♠', 'K♠', '2♥', '3♥', 
    '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'A♥', 'J♥', 'Q♥', 'K♥', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'A♦', 'J♦', 'Q♦', 'K♦', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'A♣', 'J♣', 'Q♣', 'K♣']
    return baralho
    
def extrai_naipe(carta):
    naipe = carta[1]
    if len(carta) == 3:
        naipe = carta[2]
    return naipe

def extrai_valor(carta):
    valor = carta[0]
    if len(carta) == 3:
        valor = '10'
    return valor

def lista_movimentos_possiveis(bar, ind):
    naipe = []
    valor = []

    for e in bar: 
        if len(e) == 3:
            valor.append(e[0] + e[1])
        else:
            valor.append(e[0])

    for e in bar:
        if len(e) == 3:
            naipe.append(e[2])
        else:
            naipe.append(e[1])

    if ind == 0:
        return []

    if ind > 0:
        if ind == 1 or ind == 2:
            if valor[ind] == valor[ind - 1] or naipe[ind] == naipe[ind - 1]:
                return [1]
            else:
                return []
        if ind >= 3:
            if (valor[ind] == valor[ind - 1] or naipe[ind] == naipe[ind - 1]) and (valor[ind] == valor[ind - 3] or naipe[ind] == naipe[ind - 3]):
                return [1, 3]
            elif valor[ind] == valor[ind - 1] or naipe[ind] == naipe[ind - 1]:
                return [1]
            elif valor[ind] == valor[ind - 3] or naipe[ind] == naipe[ind - 3]:
                return [3]
            else:
                return []

def empilha(cartas, origem, destino):
    cartas[destino] = cartas[origem]
    del cartas[origem]
    return cartas

def possui_movimentos_possiveis(cartas):
    valor = []
    naipe = []

    for e in cartas: 
        if len(e) == 3:
            valor.append(e[0] + e[1])
        else:
            valor.append(e[0])
    for e in cartas:
        if len(e) == 3:
            naipe.append(e[2])
        else:
            naipe.append(e[1])

    for i in range(1, len(valor)):
        if (valor[i] == valor[i - 1]) or (valor[i] == valor[i - 3]) or (naipe[i] == naipe[i - 1]) or (naipe[i] == naipe[i - 3]):
            return True
    return False

def rand_lista(lista):
    import random
    random.shuffle(lista)
    return lista

def print_jogo():
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
    return ''

def cor_carta(carta):
    if extrai_naipe(carta) == '♠':
        return Fore.RED + carta + Style.RESET_ALL
    if extrai_naipe(carta) == '♥':
        return Fore.YELLOW + carta + Style.RESET_ALL
    if extrai_naipe(carta) == '♦':
        return Fore.GREEN + carta + Style.RESET_ALL
    if extrai_naipe(carta) == '♣':
        return Fore.BLUE + carta + Style.RESET_ALL

def print_cor(baralho, i):
    for carta in baralho:
        if extrai_naipe(carta) == '♠':
            print('{0}. {1}'.format(i, cor_carta(carta)))
        if extrai_naipe(carta) == '♥':
            print('{0}. {1}'.format(i, cor_carta(carta)))
        if extrai_naipe(carta) == '♦':
            print('{0}. {1}'.format(i, cor_carta(carta)))
        if extrai_naipe(carta) == '♣':
            print('{0}. {1}'.format(i, cor_carta(carta)))
        i += 1






















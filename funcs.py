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
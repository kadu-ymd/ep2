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
from funcs import *
# cond = True
while cond:
    try:
        int(input('INT '))
        cond = False
    except ValueError:
        pass

# quer_jogar = True
# while quer_jogar:
    
#     resposta = input('Deseja jogar novamente? Digite "n" para "não" e qualquer outra coisa para "sim". ')
#     if resposta == 'n':
#         break

# print('Obrigado por jogar!')

print(print_jogo())
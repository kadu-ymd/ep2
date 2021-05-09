import funcs
# import colorama

# def cores_naipe(cartas):
cartas = funcs.rand_lista(funcs.cria_baralho())
cartas_cores = []
for carta in cartas:
    if funcs.extrai_naipe(carta) == '♠':
        espadas = ('\33[31m' + carta + '\33[0m')
        cartas_cores.append(espadas)
    elif funcs.extrai_naipe(carta) == '♥':
        copas = ('\33[32m' + carta + '\33[0m')
        cartas_cores.append(copas)
    elif funcs.extrai_naipe(carta) == '♦':
        ouros = ('\33[33m' + carta + '\33[0m')
        cartas_cores.append(ouros)
    elif funcs.extrai_naipe(carta) == '♣':
        paus = ('\33[34m' + carta + '\33[0m')
        cartas_cores.append(paus)
print(cartas_cores)

    # return cartas_cores

# print(funcs.cores_naipe([funcs.rand_lista(funcs.cria_baralho())]))

# instalar
anaconda = 'conda install -c anaconda colorama'
vscode = 'pip install colorama'

from colorama import Fore, Back, Style

print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
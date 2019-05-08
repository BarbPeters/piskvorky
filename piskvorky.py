from util import tah
from ai import tah_pocitace

def vyhodnot(pole):
    if 'xxx' in pole:
        return('x')
    elif 'ooo' in pole:
        return('o')
    elif '-' not in pole:
        return('!')
    else:
        return('-')

def tah_hrace(pole):
    while True:
        cislo_policka = int(input('Zadejte pozici symbolu od 0 do 19:'))
        if cislo_policka >= 0 and cislo_policka <= 19 and pole[cislo_policka] == '-':
            return tah(pole, cislo_policka, 'x')
        else:
            print('Špatná pozice, zadejte znovu.')

def piskvorky():
    pole = '-' *20
    while True:
        print(pole)
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != '-':
            break
        pole = tah_pocitace(pole)
        if vyhodnot(pole) != '-':
            break

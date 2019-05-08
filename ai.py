from util import tah

from random import randrange

def tah_pocitace(pole):
    while True:
        cislo_policka = randrange(19)
        if pole[cislo_policka] == "-":
            return tah(pole, cislo_policka, "o")

import pytest

from piskvorky import vyhodnot
from util import tah
from ai import tah_pocitace

def test_vyhodnot_vyhra_x():
    "Objeví se 3 x za sebou"
    assert vyhodnot('---xxx--------------') == 'x'
    assert vyhodnot('-----------------xxx') == 'x'

def test_vyhodnot_vyhra_o():
    "Objeví se 3 o za sebou"
    assert vyhodnot('---ooo--------------') == 'o'
    assert vyhodnot('-----------------ooo') == 'o'

def test_vyhodnot_remiza():
    "V poli neni znak -"
    assert vyhodnot('xoxoxoxoxoxoxoxoxoxx') == '!'
    assert vyhodnot('xxooxxooxxooxxooxxoo') == '!'

def test_tah_x():
    "Tah x"
    assert tah("--------------------", 2, "x") == "--x-----------------"
    assert tah("--------------------", 19, "x") == "-------------------x"


def test_tah_o():
    "Tah o"
    assert tah("--------------------", 2, "o") == "--o-----------------"
    assert tah("--------------------", 19, "o") == "-------------------o"

def test_tah_pocitace_na_prazdne_pole():
    "Tah pocitace na prazdne pole "
    pole = "--------------------"
    result = tah_pocitace(pole)
    assert result.count("-") == 19
    assert result.count("o") == 1

def test_tah_pocitace_na_pole_3_kolo():
    "Tah pocitace na pole po třetím kole "
    pole = "--oxxo---x----------"
    result = tah_pocitace(pole)
    assert result.count("x") == 3
    assert result.count("o") == 3
    assert result.count("-") == 14

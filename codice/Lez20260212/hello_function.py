""" In questo modulo introduciamo le funzioni in python """

import random as rnd

# print(help(rnd))

def mia_funzione():
    """ Ho definito (def) la funzione"""
    
    saluti = ['buongiorno', 'ciao', 'buonasera', 'hello']

    print(rnd.choice(saluti))

def addizione(a: int, b: int = 0):
    """
    Docstring for addizione
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    """
    return a + b

def sottrazione(a, b):
    return a - b


numero1 = 86
numero2 = 16


# mia_funzione()
print(addizione(addendo2 = numero1,addendo1 = numero2))
print(sottrazione(addizione(7,5),sottrazione(9,6)))
print(addizione(3))

print(numero1, numero2)

# mia_funzione()
# mia_funzione()
# mia_funzione()

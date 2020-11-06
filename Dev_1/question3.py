'''
Petit Diviseur
'''

import math

def petDiv(n):
    '''
    :param n: positif integer
    :return: plus petit diviseur d'un nombre entier
    no need to continue after racine de n because
    after that there will be no diviseur other than the number itself
    '''
    assert n > 0, "Numero doit etre positive"
    for i in range(2, n + 1):
        if i > math.sqrt(n):
            return n
        if n % i == 0:
            return i
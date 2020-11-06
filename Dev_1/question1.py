'''
Factorielle en forme iteratif et recursif
'''

def factIte(n):
    assert n > 0, "Numero doit etre positif"
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x

def factRecur(n):
    assert n >= 0, "Numero doit etre positif"
    if n <= 1:
        return 1
    return n * factRecur(n - 1)
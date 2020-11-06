def CalcPx(a, x):
    '''
    Calculer p(x)=a0+a1*x+..+ai*xi+...+an*xn
    :param a: liste de nombres
    :param x: constante
    :return:
    '''
    assert len(a) > 0
    y = 0
    i = 0
    while i <= len(a) - 1:
        y += (a[i] * (x ** i))
        i += 1
    return y

print(CalcPx([2,3,4], 2))
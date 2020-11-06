'''
Equation de Second Degree
'''
import math
from UTC503.premierDegre import controleEntreeEtSol
from UTC503.premierDegre import premDegre

def secDeg(a, b, c):
    assert a > 0
    delta = (b**2) - (4*a*c) #discriminant
    if delta == 0:
        # used controleEntreeEtSol because it will check for a and b != 0 and return -b/2a
        return controleEntreeEtSol(2*a, b)
    elif delta > 0:
        '''
        x1 = (-b -sqrt(delta)) / 2a
        x1 = (-b +sqrt(delta)) / 2a
        used premDegre because it returns -b / a
        '''
        x1 = premDegre(2*a, b) - premDegre(2*a, math.sqrt(delta))
        x2 = premDegre(2*a, b) + premDegre(2*a, math.sqrt(delta))
        # return x1 and x2 sous forme de dictionaire
        return {"x1": x1, "x2": x2}
    else:
        # delta < 0 donc pas de solution possible
        return


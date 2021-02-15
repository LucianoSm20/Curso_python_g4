import utils

d = utils.d
m = utils.m
ace = utils.ace
t = utils.t

def fuerza():

    result  = m*ace
    print ('fuerza =', result)
    return result

def trabajo():

    result = fuerza()* d
    print('trabajo =', result)
    return result


def potencia():

    result = trabajo()/t
    print('potencia =', result)
    return result

def velocidad():

    result = potencia() / fuerza()
    print('velocidad =', result)
    return result



print( velocidad())
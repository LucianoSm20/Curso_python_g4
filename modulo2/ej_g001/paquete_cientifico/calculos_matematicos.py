import utils

a = utils.a
b = utils.b

def dividir():
    result = a/b
    print('division=', result)
    return result

def suma():
    result = a+b
    print('suma=', result)
    return result

def resta():
    result = a-b
    print('resta=', result)
    return result

def multiplicar():
    result = a*b
    print('multiplicar=', result)
    return result

if __name__ == "__main__":
    dividir()
    suma()
    resta()
    multiplicar()
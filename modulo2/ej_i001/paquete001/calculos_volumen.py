import math

def volumen_cubo(LC):
    result = math.pow(LC, 3)
    print(result)
    return result

def volumen_piramide(AB, H):
    result = (AB*H)/3
    print(result)
    return result

def volumen_esfera(R):
    result = (R*3.14*4)/3
    print(result)
    return result

def volumen_cilindro(R, H):
    result = (3.14*math.pow(R,2)*H)
    print(result)
    return result


LC = int(input('ingrese el lado de un cubo:'))
volumen_cubo(LC)

AB = int(input('ingrese la base de la piramide:'))
H = int(input('ingrese la altura de la piramide:'))
volumen_piramide(AB, H)

R = int(input('ingrese el radio de la esfera:'))
volumen_esfera(R)

R = int(input('ingrese el randio del cilndro:'))
H = int(input('ingrese la altura del cilindro:'))
volumen_cilindro(R, H)


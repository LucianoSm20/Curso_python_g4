import utils
 
PI = utils.pi
R = utils.radio
B = utils.base
H = utils.altura
L1 = utils.lado_A
L2 = utils.lado_B



def area_perimetro_circ():

    area = ((R*R)* PI)
    perimetro= 2*PI*R
    print('circulo=', area, perimetro)
    return area, perimetro

def area_perimetro_tri():

    area = (B*H)/2
    perimetro = B*3
    print('triangulo=', area, perimetro)
    return area, perimetro

def area_perimetro_rec():

    area = L1*L2
    perimetro = (L1*2 + L2*2)
    print('rectangulo=', area, perimetro)
    return area, perimetro

def distancia_recorrida(T, V):

    dist = T*V



if __name__ == "__main__":
    area_perimetro_circ()
    area_perimetro_tri()
    area_perimetro_rec()



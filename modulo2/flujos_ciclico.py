def ingresar_numero(lista_de_numeros):   
    nuevo_numero = int(input('ingrese un numero:'))

    
    permiso = 0
    for num_actual in lista_de_numeros:
        if num_actual == nuevo_numero:
            permiso = 0
            print("error, ingrese un nuevo numero")
            break
        elif num_actual != nuevo_numero:
            permiso = 1
            continue

    if permiso == 1 and len(lista_de_numeros)<15:
        lista_de_numeros.append(nuevo_numero)
        ingresar_numero(lista_de_numeros)
    elif len(lista_de_numeros) == 15:
        print(lista_de_numeros)
    else:
        ingresar_numero(lista_de_numeros)

#lista_de_numeros = []
#nuevo_numero = int(input('ingrese un numero:'))
#lista_de_numeros.append(nuevo_numero)
#ingresar_numero(lista_de_numeros)

def generar_primos():

    lista_primos = [2]
    while(lista_primos[len(lista_primos)-1] < 30):
        lista_primos.append(lista_primos[len(lista_primos)-1] +1)

    for i in lista_primos:
        for j in range(2,11):
            print (j)
            if i == 2 or i == 3 or i == 5 or i == 7:
                continue
            elif i%j == 0:
                print("i:", i)
                lista_primos.remove(i)
                break
        
        

    for i in lista_primos:
            print(i, end=" ")

generar_primos()
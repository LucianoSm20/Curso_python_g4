def ingresar_numero():   
    nuevo_numero = int(input('ingrese un numero:'))

    lista_de_numeros = []
    permiso = 0
    for num_actual in lista_de_numeros:
        if num_actual != nuevo_numero:
            permiso = 1
            continue
        else:
            permiso = 0
            break

    if permiso == 1 and len(lista_de_numeros)<15:
        lista_de_numeros.append(nuevo_numero)
        ingresar_numero()
    elif len(lista_de_numeros) == 15:
        print(lista_de_numeros)
    else:
        ingresar_numero()

ingresar_numero()
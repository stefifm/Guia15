print("Altura de las personas")


def validar(inf):
    n = inf
    while n <= inf:
        n = int(input("Cargue el tamaño del vector: "))
        if n <= inf:
            print("Error. Ingrese un número que sea diferente a cero.")
    return n


def cargar_vector(v):
    n = len(v)
    for i in range(n):
        v[i] = float(input("Cargue las alturas de las personas: "))
    return v

def promedio(v):
    tam = len(v)
    suma = 0
    prom = 0
    for i in range(len(v)):
        suma += v[i]
    if tam != 0:
        prom = suma / tam
    return prom

# def v_contador(v):
#     n = len(v)
#     contadores = n * [0]
#     for i in range(n):
#         pos = v[i]
#         contadores[pos-1] += 1
#     return contadores

def menor_promedio(v, prom):
    cont = 0
    for i in range(len(v)):
        if v[i] <= prom:
            cont +=1
    return cont

def mayor_promedio(v, prom):
    cont_may = 0
    for i in range(len(v)):
        if v[i] >= prom:
            cont_may += 1
    return cont_may


#Función principal

def test():
    #Cargar el vector
    n = validar(0)
    v = n * [0]
    cargar_vector(v)
    print("Datos del vector:",v)
    #Cálculo del promedio
    prom = promedio(v)
    print("La media de alturas:",prom)
    #Contar altura menor
    cant_menor = menor_promedio(v, prom)
    print("La cantidad de alturas menor a la media:",cant_menor)
    #Contar la altura mayor
    cant_mayor = mayor_promedio(v, prom)
    print("La cantidad de alturas mayor a la media:",cant_mayor)




if __name__ == "__main__":
    test()
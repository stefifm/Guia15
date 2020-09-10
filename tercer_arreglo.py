print("Un arreglo a partir de 2")

import random

def validar(inf):
    n = inf
    while n <= inf:
        n = int(input("Cargue el tamaño del vector: "))
        if n <= inf:
            print("Error. Ingrese un número que sea diferente a cero.")
    return n

#Carga de vector para v1 y v2
def cargar_vector(v):
    n = len(v)
    for i in range(n):
        #v[i] = int(input("Cargue los elementos: "))
        v[i] = random.randint(1, 30)
    return v

def validar_arreglo(val1, v3):
    existe = False
    for k in range(len(v3)):
        if val1 == v3[k]:
            existe = True
            break
    return existe

def generar_arreglo(v1, v2):
    v3 = []
    #Recorrer el primer arreglo
    for i in range(len(v1)):
        #validar que el elemento a agregar en v3 no se encuentre
        #if v1[i] in v3 no se usa eso
        existe = validar_arreglo(v1[i], v3)
        #sino esta buscar en el v2 si se encuentra duplicado
        if not existe: #o existe == False
            for j in range(len(v2)):
                if v1[i] == v2[j]:
                    v3.append(v1[i]) #si está duplicado, grabarlo en el v3
                    break #Corta la búsqueda en v2
    return v3


def test():
    #Cargar el primer vector
    n = validar(0)
    v1 = n * [0]
    cargar_vector(v1)
    #Cargar el segundo vector
    m = validar(0)
    v2 = m * [0]
    cargar_vector(v2)
    #Generar el tercer arreglo
    v3 = generar_arreglo(v1, v2)
    #Resultados
    print("Primer vector:",v1)
    print("Segundo vector:",v2)
    print("Tercer vector generado de los 2 vectores originales:",v3)


if __name__ == "__main__":
    test()
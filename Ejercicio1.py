def ordenarlista(lista):
    """La funcion ordena una lista de numeros de mayor a menor
    y crea un fichero con estos
    Parametros:
    -Lista de numeros
    """
    listaordenada=lista.split(",")
    listaordenada.sort()
    listaordenada.reverse()
    file = open("ListaOrdenada.txt", "w")
    for i in listaordenada:
        file.write(i + " ")
    file.close()
def NumeroPar(fichero):
    """La funcion lee un fichero y
    crea otro fichero con los numeros pares
    Parametros:
    -Nombre de la direccion del fichero
    """
    file = open(fichero, "r")
    lineas = file.read()
    lineas = list(lineas.replace(" ", ""))
    lineas = list(map(int,lineas))
    pares = []
    for i in lineas:
        if i % 2 == 0:
            pares.append(i)
    file1 = open("ListaDePares.txt", "w")
    for i in pares:
        file1.write(str(i) + " ")
    file1.close()
ordenarlista(input("Dime una lista de numeros separados por comas: "))
NumeroPar(input("Dime la direccion del fichero que quieres leer: "))




diccionario = {}
while True: 
    menu = int(input("(1)Añadir alumno/a (2)Numero de aprobados (3)Mostrar todo el alumnado: "))
    if menu == 1:
        nombre = input("Nombre del alumno: ")
        aprobado = bool(int(input("aprobado(1)/Suspendido(0): ")))
        diccionario[nombre] = aprobado   
    elif menu == 2:
        aprobados = 0
        for i in diccionario.values():
            if i != 0:
                aprobados += 1
        print("El número de alumnos aprobados es: " + str(aprobados))
    elif menu == 3:
        print(diccionario.keys())
    else:
        print("Error")

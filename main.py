import os

from grafica import Grafica
i= 1

def pedirOpcion():
    correcto= False
    num= -1
    while(not correcto):
        try:
            num= int(input("Introduce tu opción: "))
            correcto= True
        except ValueError:
            print("Error: Introduce un número valido")
    return num


def menu(grafica, copia):
    opcion = -1
    sub_opcion = -1

    while (opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("\n-------------------------- MENÚ --------------------------")
        print("1) Agregar")
        print("2) Eliminar")
        print("3) Buscar")
        print("4) Grado de un Nodo")
        print("5) Número total")
        print("6) Vaciar")
        print("7) Copiar")
        print("8) Cargar copia")
        print("9) Bipartida")
        print("10) Buscar paseo de Euler (algoritmo de Fleury)")
        print("0) Salir")
        print("-------------------------- GRAFICA --------------------------")

        for v in grafica:
            if v:
                print(v)

        print("-------------------------- COPIA GRAFICA --------------------------")
        for v in copia:
            if v:
                print(v)

        while opcion not in range(11):
            opcion= pedirOpcion()
            if (opcion not in range(11)):
                print("Selecciona una opción válida")

        if opcion == 1:
            menu_agregar(grafica)
            opcion = -1
        elif opcion == 2:
            menu_eliminar(grafica)
            opcion = -1
        elif opcion == 3:
            menu_buscar(grafica)
            opcion = -1
        elif opcion == 4:
            menu_grado(grafica)
            opcion = -1
        elif opcion == 5:
            menu_total(grafica)
            opcion = -1
        elif opcion == 6:
            menu_vaciar(grafica)
            opcion = -1
        elif opcion == 7:
            copia= copiar_grafica(grafica)
            opcion = -1
        elif opcion == 8:
            grafica= copiar_grafica(copia)
            opcion = -1
        elif opcion == 9:
            if grafica.esBipartita():
                input("Presione una tecla para continuar...")
            else:
                print("La gráfica no es bipartita.")
                input("Presione una tecla para continuar...")
            opcion= -1
        elif opcion == 10:
            grafica.busquedas(0)
            input()
            opcion= -1

    return

def menu_agregar(grafica):
    global sub_opcion
    global i
    sub_opcion = -1

    while (sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("1) Agregar Nodo")
        print("2) Agregar Arista")
        print("0) Regresar")

        while sub_opcion not in range(3):
            sub_opcion= pedirOpcion()
            if (sub_opcion not in range(3)):
                print("Selecciona una opción válida")

        if sub_opcion == 1:
            # Función agregar Nodo (Pedir id)
            id= input("Introduce el identificador del nodo: ")
            if (grafica.agregarVertice(id)):
                print("Se agrego el nodo correctamente")
            else:
                print("Ya existe un nodo con ese identificador")
            input("Presione una tecla para continuar...")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función agregar Nodo (Pedir id)
            clave= 'e' + str(i)
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")
            if grafica.agregarArista(clave, inicio, destino):
                print("Se agrego la arista correctamente")
            else:
                print("No es posible agregar esa arista")
            input("Presione una tecla para continuar...")
            i= i+ 1
            sub_opcion = -1

    return

def menu_eliminar(grafica):
    global sub_opcion
    sub_opcion = -1

    while (sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("1) Eliminar Nodo")
        print("2) Eliminar Arista")
        print("0) Regresar")

        while sub_opcion not in range(3):
            sub_opcion= pedirOpcion()
            if (sub_opcion not in range(3)):
                print("Selecciona una opción válida")

        if sub_opcion == 1:
            # Función eliminar Nodo (Pedir id)
            id= input("Introduce el identificador del nodo que desea borrar: ")
            if grafica.eliminarVertice(id):
                print("El nodo se elimino correctamente")
                input("Presione una tecla para continuar...")
            else:
                print("No existe ese nodo en Ba Sing se")
                input("Presione una tecla para continuar...")
            print("Eliminar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función eliminar Nodo (Pedir id)
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")
            if grafica.eliminarArista(inicio, destino):
                print("Se elimino la arista correctamente")
                input("Presione una tecla para continuar...")
            else:
                print("No existe esa arista en Ba Sing se")
                input("Presione una tecla para continuar...")
            print("Eliminar arista")
            sub_opcion = -1

    return

def menu_buscar(grafica):
    global sub_opcion
    sub_opcion = -1

    while (sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("1) Buscar Nodo")
        print("2) Buscar Arista")
        print("0) Regresar")

        while sub_opcion not in range(3):
            sub_opcion= pedirOpcion()
            if (sub_opcion not in range(3)):
                print("Selecciona una opción válida")

        if sub_opcion == 1:
            # Función buscar Nodo (Pedir id)
            id= input("Introduce el id del nodo que busca: ")
            nodo= grafica.buscarVertice(id)
            if nodo:
                print(nodo.__str__())
                input("Presione una tecla para continuar...")
            else:
                print("No existe ese nodo en gráfica")
                input("Presione una tecla para continuar...")
            print("Buscar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función buscar Nodo (Pedir id)
            print("Buscar arista")
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")
            if grafica.buscarArista(inicio, destino):
                print ("Existe la arista entre %s y %s"%(inicio, destino))
                input("Presione una tecla para continuar...")
            else:
                print("No existe una conexión entre %s y %s"%(inicio, destino))
                input("Presione una tecla para continuar...")
            sub_opcion = -1

    return

def menu_grado(grafica):
    #os.system("clear") # LINUX
    os.system("cls") # WINDOWS

    # Función obtener grado de un Nodo
    id= input("Introduce el id del nodo: ")
    if grafica.gradoVertice(id) >= 0:
        print("El grado del nodo %s es: %s"%(id, grafica.gradoVertice(id)))
    else:
        print("No existe ese nodo en la gráfica")
    input("Presione una tecla para continuar...")

    return

def menu_total(grafica):
    global sub_opcion
    sub_opcion = -1

    while (sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("1) Total de Nodos")
        print("2) Total de Aristas")
        print("0) Regresar")

        while sub_opcion not in range(3):
            sub_opcion= pedirOpcion()
            if (sub_opcion not in range(3)):
                print("Selecciona una opción válida")

        if sub_opcion == 1:
            # Función total Nodo (Pedir id)
            print("El número total de nodos es: %s"%(grafica.numeroVertices()))
            input("Presione una tecla para continuar...")
            print("Total de nodos")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función total Nodo (Pedir id)
            print("El número total de aristas es: %s"%(grafica.numeroAristas()))
            input("Presione una tecla para continuar...")
            print("Total de aristas")
            sub_opcion = -1

    return

def menu_vaciar(grafica):
    global sub_opcion
    sub_opcion = -1
    warning_op = ''

    while (sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("1) Vaciar Nodo")
        print("2) Vaciar Grafica")
        print("0) Regresar")

        while sub_opcion not in range(3):
            sub_opcion= pedirOpcion()
            if (sub_opcion not in range(3)):
                print("Selecciona una opción válida")

        if sub_opcion == 1:
            # Función vaciar Nodo (Pedir id)
            id= input("Introduce el id del nodo: ")
            if grafica.vaciarVertice(id):
                print("El nodo se vacio correctamente")
                input("Presione una tecla para continuar...")
            else:
                print("Ese nodo no existe en Ba Sing Se")
                input("Presione una tecla para continuar...")
            print("Vaciar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            print("Seguro que quieres vaciar la grafica? (Empezar desde cero)")
            while(warning_op not in ['S','s','n','N']):
                warning_op = input("(S/N): ")

            if (warning_op in ['S','s']):
                # Función vaciar gráfica
                grafica.vaciarGrafica()
                print("La grafica se borro por completo")
                input("Presione una tecla para continuar...")
                return
            elif (warning_op in ['N','n']):
                sub_opcion = -1
                warning_op = ''

    return

def copiar_grafica(grafica):
    return grafica.copiar()


g= Grafica()
c= Grafica()
menu(g, c)

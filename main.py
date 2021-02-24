import os

from grafica import Grafica
i= 1

def pedirOpcion():
    correcto= False
    num= -1
    while(not correcto):
        try:
            num= int(input("\nIntroduce tu opción: "))
            correcto= True
        except ValueError:
            print("\nError: Introduce un número valido")
    return num


def menu(grafica, copia):
    opcion = -1
    sub_opcion = -1

    while (opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("-------------------------- MENÚ --------------------------")
        print("1) Agregar")
        print("2) Eliminar")
        print("3) Buscar")
        print("4) Grado de un Nodo")
        print("5) Número total")
        print("6) Vaciar")
        print("7) Copiar")
        print("8) Cargar copia")
        print("9) Tareas")

        print("0) Salir")
        if(len(grafica.lista_vertices) != 0): print("\n-------------------------- GRAFICA --------------------------")

        for v in grafica:
            if v:
                print(v)

        if(len(copia.lista_vertices) != 0): print("\n-------------------------- COPIA GRAFICA --------------------------")
        for v in copia:
            if v:
                print(v)

        while opcion not in range(10):
            opcion= pedirOpcion()
            if (opcion not in range(10)):
                print("\nSelecciona una opción válida")

        if opcion == 0: return
        elif opcion == 1: menu_agregar(grafica)
        elif opcion == 2: menu_eliminar(grafica)
        elif opcion == 3: menu_buscar(grafica)
        elif opcion == 4: menu_grado(grafica)
        elif opcion == 5: menu_total(grafica)
        elif opcion == 6: menu_vaciar(grafica)
        elif opcion == 7: copia= copiarGrafica(grafica)
        elif opcion == 8: grafica= copiarGrafica(copia)
        elif opcion == 9: menu_tareas(grafica)

        opcion = -1

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
                print("\nSelecciona una opción válida")

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            # Función agregar Nodo (Pedir id)
            id= input("Introduce el identificador del nodo: ")

            if (grafica.agregarVertice(id)):
                print("Se agrego el nodo correctamente")
            else:
                print("Ya existe un nodo con ese identificador")

        elif sub_opcion == 2:
            # Función agregar Nodo (Pedir id)
            clave= 'e' + str(i)
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")

            if grafica.agregarArista(clave, inicio, destino):
                print("Se agrego la arista correctamente")
            else:
                print("No es posible agregar esa arista")

            i= i+ 1

        input("\nPresione ENTER para continuar...")
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

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            # Función eliminar Nodo (Pedir id)
            id= input("Introduce el identificador del nodo que desea borrar: ")

            if grafica.eliminarVertice(id):
                print("El nodo se elimino correctamente")
            else:
                print("No existe ese nodo en la gráfica")

        elif sub_opcion == 2:
            # Función eliminar Nodo (Pedir id)
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")

            if grafica.eliminarArista(inicio, destino):
                print("Se elimino la arista correctamente")
            else:
                print("No existe esa arista en la gráfica")


        input("\nPresione ENTER para continuar...")
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

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            # Función buscar Nodo (Pedir id)
            id= input("Introduce el id del nodo que busca: ")
            nodo= grafica.buscarVertice(id)

            if nodo:
                print(nodo.__str__())
                input("Presione una tecla para continuar...")
            else:
                print("No existe ese nodo en gráfica")

        elif sub_opcion == 2:
            # Función buscar Nodo (Pedir id)
            inicio= input("Introduce el id del nodo de inicio: ")
            destino= input("Introduce el id del nodo del destino: ")

            if grafica.buscarArista(inicio, destino):
                print ("Existe la arista entre %s y %s"%(inicio, destino))
            else:
                print("No existe una conexión entre %s y %s"%(inicio, destino))

        input("\nPresione ENTER para continuar...")
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

    input("\nPresione ENTER para continuar...")

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

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            # Función total Nodo (Pedir id)
            print("\nEl número total de nodos es: %s"%(grafica.numeroVertices()))
        elif sub_opcion == 2:
            # Función total Nodo (Pedir id)
            print("\nEl número total de aristas es: %s"%(grafica.numeroAristas()))

        input("\nPresione ENTER para continuar...")
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

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            # Función vaciar Nodo (Pedir id)
            id= input("Introduce el id del nodo: ")

            if grafica.vaciarVertice(id): print("El nodo se vacio correctamente")
            else: print("Ese nodo no existe en la gráfica")

        elif sub_opcion == 2:
            print("Seguro que quieres vaciar la grafica? (Empezar desde cero)")

            while(warning_op not in ['S','s','n','N']):
                warning_op = input("(S/N): ")

            if (warning_op in ['S','s']):
                # Función vaciar gráfica
                grafica.vaciarGrafica()
                print("La gráfica se borro por completo")
                return

            elif (warning_op in ['N','n']):
                warning_op = ''

        input("\nPresione ENTER para continuar...")
        sub_opcion = -1

    return

def copiarGrafica(grafica):
    return grafica.copiar()

def subirGrafica(graph):
    lineas=[]
    archivo= open("grafica.txt")
    grafica= [linea[:-1] for linea in archivo]

    for linea in grafica:
        lineas.append(linea)

    for elementos in lineas:
        e= lineas[0]
        lineas= lineas[1:]
        if e == '$':
            break
        else:
            graph.agregarVertice(e)
    i= 0
    for elementos in lineas:
        if lineas:
            a= lineas[0]
            b= lineas[1]
            c= lineas[2]
            lineas= lineas[3:]
            graph.agregarArista("e"+str(i), a, b, int(c))
            i+= 1

    archivo.close()
    return graph

def menu_tareas(grafica):
    global sub_opcion
    sub_opcion = -1

    while(sub_opcion != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("-------------------------- TAREAS --------------------------")

        print("1) Verificar si grafica es bipartita")
        print("2) Buscar paseo de Euler (algoritmo de Fleury)")
        print("3) Buscar árbol de expansión")

        print("0) Regresar")

        while sub_opcion not in range(4):
            sub_opcion = pedirOpcion()
            if (sub_opcion not in range(4)):
                print("\nSelecciona una opción válida")

        if sub_opcion == 0: return
        elif sub_opcion == 1:
            if not grafica.esBipartita(): print("\nLa gráfica no es bipartita.")

        elif sub_opcion == 2:
            if not grafica.Fleury(): print("\nNo es posible encontrar un paseo de Euler.")

        elif sub_opcion == 3:
            menu_expansion(grafica)


        if sub_opcion != 3: input("\nPresione ENTER para continuar...")
        sub_opcion = -1

def menu_expansion(grafica):
    exp = -1

    while(exp != 0):
        #os.system("clear") # LINUX
        os.system("cls") # WINDOWS

        print("------------------ BÚSQUEDA DE ÁRBOLES DE EXPANSIÓN ------------------")
        print("1) Buscar árbol de expansión (busqueda a lo ancho)")
        print("2) Buscar árbol de expansión (busqueda a lo profundo)")
        print("3) Buscar árbol de expansión (Kruskal)")
        print("4) Buscar árbol de expansión (Prim)")

        print("0) Regresar")

        while exp not in range(5):
            exp = pedirOpcion()
            if (exp not in range(5)):
                print("\nSelecciona una opción válida")

        if exp == 0: return
        elif exp == 1:
            grafica.busquedas(1)

        elif exp == 2:
            grafica.busquedas(0)

        elif exp == 3:
            if not grafica.kruskal(): print("\nLa gráfica no es conexa")

        elif exp == 4:
            #if not grafica.prim(): print("\nLa gráfica no es conexa")
            print("Quién sos?")

        input("\nPresione ENTER para continuar...")
        exp = -1

g = Grafica()
c = Grafica()
g = subirGrafica(g)
menu(g, c)

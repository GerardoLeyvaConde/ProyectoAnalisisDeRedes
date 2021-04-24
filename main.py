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
        if(len(grafica.lista_vertices) != 0): print("9) Tareas")

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
        elif opcion == 9: grafica = menu_tareas(grafica)

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
    print(grafica.gradoVertice(id))
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
            graph.agregarArista("e"+str(i), a, b, int(c), True)
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
        print("4) Buscar arborescencia (Dijkstra)")

        print("0) Regresar")

        while sub_opcion not in range(6):
            sub_opcion = pedirOpcion()
            if (sub_opcion not in range(6)):
                print("\nSelecciona una opción válida")

        if sub_opcion == 0: return grafica
        elif sub_opcion == 1:
            lista_u, lista_v, bipartita = grafica.esBipartita()     #ruta: Paseo de euler.
                                                                    #cerrado: es 0 si es cerrado, varaible llamada impares en algoritmo.
                                                                    #paseo: booleano que indica si el paseo existe o no.
            if not bipartita:
                print("\nLa gráfica no es bipartita.")
            else:
                print("\nEs bipartita")                                   #Si el algorimo llego hasta aqui, significa que la grafica es bipartita
                print("V: %s"%(lista_v))                                #Imprime las listas u y v. Restablece los vertices y regresa True
                print("U: %s"%(lista_u))

        elif sub_opcion == 2:

            ruta, cerrado, paseo = grafica.Fleury()     #ruta: Paseo de euler.
                                                        #cerrado: es 0 si es cerrado, varaible llamada impares en algoritmo.
                                                        #paseo: booleano que indica si el paseo existe o no.

            if not paseo:
                print("\nNo es posible encontrar un paseo de Euler.")
            else:
                if cerrado == 0:
                    print("\nEl paseo de Euler es cerrado.")

                else:
                    print("\nEl paseo de Euler es abierto.")
                print(ruta)

        elif sub_opcion == 3:
            menu_expansion(grafica)

        elif sub_opcion == 4:
            inicio = input("Introduzca el vértice inicial: ")

            grafica, c, p = grafica.dijkstraGeneral(inicio)
            if(p < 0):
                print("\nExiste un ciclo negativo por lo que no se puede corregir")
                print("Ruta del ciclo:")
                print(c)
                print("Longitud: ", p)
            else: 
                print("\nArborescencia:")

                imprime_grafica(grafica, True)

                grafica.restablecerVertices()
        elif sub_opcion == 5:
            f, n, c = grafica.floyd()
            if(c):
                print("Hay un ciclo negativo")
                print("Ruta del ciclo: ")
                print(f)
                print("Longitud: ", n)
            else:
                j = 0
                for i in range(len(f)):
                    if(i == j * grafica.numero_vertices):
                        print("-----------------------RUTAS DE ", n[j], "-----------------------")
                    print("Ruta de ", n[j], " -> ", n[i-(j * grafica.numero_vertices)])
                    if(i >= (j + 1) * grafica.numero_vertices - 1):
                        j += 1
                    if(f[i][0]):
                        print(f[i][0])
                        print("Peso: ", f[i][1])
                    else:
                        print("No hay ruta")
                    print("")

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

        while exp not in range(6):
            exp = pedirOpcion()
            if (exp not in range(6)):
                print("\nSelecciona una opción válida")

        if exp == 0: return
        elif exp == 1:
            grafica, bosque = grafica.busquedas(1)  #busqueda a lo ancho (1)

            if bosque:
                print("\nEl bosque es:")
            else:
                print("\nEl árbol de expansión es:")

            imprime_grafica(grafica)

        elif exp == 2:
            grafica, bosque = grafica.busquedas(0)  #busqueda a lo profundo (0)

            if bosque:
                print("\nEl bosque es:")
            else:
                print("\nEl árbol de expansión es:")

            imprime_grafica(grafica)

        elif exp == 3:
            grafica, peso, bosque = grafica.kruskal()

            #Imprimimos el árbol o bosque
            if bosque:
                print("\nEl bosque es: ")
            else:
                print("\nEl árbol de mínima expansión es: ")

            imprime_grafica(grafica)

            # Imprimimos el peso total del arbol o bosque
            if bosque:
                print("\nPeso del bosque: ", peso)
            else:
                print("\nPeso del árbol: ", peso)

        elif exp == 4:
            grafica, peso, bosque = grafica.prim()

            #Imprimimos el árbol o bosque
            if bosque:
                print("\nEl bosque es: ")
            else:
                print("\nEl árbol de mínima expansión es: ")

            imprime_grafica(grafica)

            # Imprimimos el peso total del arbol o bosque
            if bosque:
                print("\nPeso del bosque: ", peso)
            else:
                print("\nPeso del árbol: ", peso)

        elif exp == 5:
            grafica= grafica.AlgoritmoFordFulkerson()
            for a in grafica.lista_aristas:
                print(grafica.lista_aristas[a])
            print("Flujo: ", grafica.peso_grafica)

        input("\nPresione ENTER para continuar...")
        exp = -1

def imprime_grafica(grafica, dirigida = False):
    if dirigida:
        for v in grafica.lista_vertices:

            if grafica.lista_vertices[v].lista_entrantes:
                arista = grafica.buscarArista(grafica.lista_vertices[v].lista_entrantes[0], v)
                print(grafica.lista_vertices[v].lista_entrantes[0], " -(", arista.peso,")->", v)

    else:
        for v in grafica:
            print(v)

def graficaArchivo(grafica):
    #Parametros:
    #d: dirigida
    #n: no dirigida
    #p: ponderada
    #f: flujo

    archivo= open("grafica.txt")

    lineas = archivo.readlines()
    lineas = [line[:-1] for line in lineas]

    parametros = lineas[0].split(',')
    nombres = lineas[1].split(',')
    lineas = [[num for num in line.split(',')] for line in lineas[2:]]

    archivo.close()

    if 'f' in parametros:
        for elementos in nombres:
            if elementos == '+':
                grafica.agregarVertice(nombres[nombres.index(elementos) - 1], elementos) 
                grafica.lista_vertices[nombres[nombres.index(elementos) - 1]].color = '+'
            elif elementos == '-':
                grafica.agregarVertice(nombres[nombres.index(elementos) - 1], elementos) 
                grafica.lista_vertices[nombres[nombres.index(elementos) - 1]].color = '-'
            else:
                grafica.agregarVertice(elementos)
    else:
        for elementos in nombres:
            grafica.agregarVertice(elementos)

    i= 0
    for arista in lineas: 
        if 'p' in parametros:
            if 'd' in parametros:
                grafica.agregarArista("e"+str(i), arista[0], arista[1], int(arista[2]))
            else:
                grafica.agregarArista("e"+str(i), arista[0], arista[1], int(arista[2]))
        else:
            if 'd' in parametros:
                grafica.agregarArista("e"+str(i), arista[0], arista[1], 0)
            else:
                grafica.agregarArista("e"+str(i), arista[0], arista[1])
        i+= 1

    grafica.lista_vertices["a"].color = '+'
    grafica.lista_vertices["e"].color = '-'

    a =grafica.buscarArista("c", "f")
    grafica.lista_aristas[a.id].peso_min = 5

    return grafica

g = Grafica(True)
#g = subirGrafica(g)
g = graficaArchivo(g)
c= Grafica(True)
menu(g, c)

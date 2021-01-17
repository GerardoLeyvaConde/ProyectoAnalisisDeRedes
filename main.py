import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import os

from clases import Grafica

g= Grafica()
for i in range(6):
    g.agregarVertice(i)

g.agregarArista(0,1,5)
g.agregarArista(0,5,2)
g.agregarArista(1,2,4)
g.agregarArista(2,3,9)
g.agregarArista(3,4,7)
g.agregarArista(3,5,3)
g.agregarArista(4,0,1)
g.agregarArista(5,4,8)
g.agregarArista(5,2,1)

de= []
a= []

for v in g:
    print(v.__str__())
    for w in v.obtenerConexiones():
        de.append(v.obtenerId())
        a.append(w.obtenerId())

print("nodo: %s"%(g.numeroNodos()))
print("aristas: %s"%(g.numeroAristas()))
print("\n-------------------------- MENÚ --------------------------")

#df= pd.DataFrame({"de": de, 'a': a})

#G= nx.from_pandas_edgelist(df, 'de', 'a')
#nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="o", alpha=0.5, linewidths=4, font_size=25, font_color="grey", font_weight="bold", width=2, edge_color="grey")
#plt.show()


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


def menu():
    opcion = -1
    sub_opcion = -1

    while (opcion != 0):
        print("1) Agregar")
        print("2) Eliminar")
        print("3) Buscar")
        print("4) Grado de un Nodo")
        print("5) Número total")
        print("6) Vaciar")
        print("0) Salir")

        while opcion not in range(7):
            opcion= pedirOpcion()
            if (opcion not in range(7)):
                print("Selecciona una opción válida")

        if opcion == 1:
            menu_agregar()
            opcion = -1
        elif opcion == 2:
            menu_eliminar()
            opcion = -1
        elif opcion == 3:
            menu_buscar()
            opcion = -1
        elif opcion == 4:
            menu_grado()
            opcion = -1
        elif opcion == 5:
            menu_total()
            opcion = -1
        elif opcion == 6:
            menu_vaciar()
            opcion = -1

    return

def menu_agregar():
    global sub_opcion
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
            print("Agregar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función agregar Nodo (Pedir id)
            print("Agregar arista")
            sub_opcion = -1

    return

def menu_eliminar():
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
            print("Eliminar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función eliminar Nodo (Pedir id)
            print("Eliminar arista")
            sub_opcion = -1

    return

def menu_buscar():
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
            print("Buscar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función buscar Nodo (Pedir id)
            print("Buscar arista")
            sub_opcion = -1

    return

def menu_grado():
    #os.system("clear") # LINUX
    os.system("cls") # WINDOWS

    # Función obtener grado de un Nodo
    print("Grado de un nodo")

    return

def menu_total():
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
            print("Total de nodos")
            sub_opcion = -1
        elif sub_opcion == 2:
            # Función total Nodo (Pedir id)
            print("Total de aristas")
            sub_opcion = -1

    return

def menu_vaciar():
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
            print("Vaciar nodo")
            sub_opcion = -1
        elif sub_opcion == 2:
            print("Seguro que quieres vaciar la grafica? (Empezar desde cero)")
            while(warning_op != 's' and warning_op != 'S' and warning_op != 'n' and warning_op != 'N'):
                warning_op = input("s/N: ")

            if (warning_op == 'S' or warning_op == 's'):
                # Función vaciar gráfica
                print("Vaciar gráfica")
                return
            elif (warning_op == 'N' or warning_op == 'n'):
                sub_opcion = -1

    return

menu()

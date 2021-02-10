import copy
class Vertice:
    def __init__(self, clave):
        self.id= clave              #Identificador del vertice
        self.grado= 0               #Grado del vertice
        self.lista_conectado= []    #Lista de los verices a los que esta conectado el vertice
        self.color= -1              #Variable utlizada para el algoritmo de Bipartita: Asiga un color al nodo
        self.bandera= 0             #Indica si el nodo fue visitado o no
    
    def __del__(self):              #Iniciador de la clase
        del self
    
    def __str__(self):              #Forma de imprimir un vertice
        return str(self.id) + ' conectado a: ' + str([id for id in self.lista_conectado])

    def conectar(self, destino):
        self.grado= self.grado+ 1
        self.lista_conectado.append(destino)

    def existeConexion(self, clave):
        if clave in self.lista_conectado:
            return True
        else:
            return False

    def eliminarConexion(self, clave):
        self.lista_conectado.remove(clave)
        self.grado= self.grado- 1

    def obtenerGrado(self):
        return self.grado

    def vaciar(self):
        self.grado= 0
        self.lista_conectado= []


class Arista:
    def __init__(self, clave, origen, destino, peso= 0):
        self.id= clave
        self.origen= origen
        self.destino= destino
        self.peso= peso
    
    def __str__(self):
        return str(self.id) + ' Origen: ' + str(self.origen) + ' Destino: ' + str(self.destino)

    def __del__(self):
        del self

class Grafica:
    def __init__(self):
        self.lista_vertices= {}
        self.lista_aristas= {}
        self.numero_aristas= 0
        self.numero_vertices= 0

    def __contains__(self, n):
        return n in self.lista_vertices

    def __iter__(self):
        return iter(self.lista_vertices.values())

    def __del__(self):
        del self

    def agregarVertice(self, clave):
        if clave not in self.lista_vertices:
            self.numero_vertices= self.numero_vertices+ 1
            nuevo_vertice= Vertice(clave) 
            self.lista_vertices[clave]= nuevo_vertice
            return True
        else:
            return False

    def agregarArista(self, clave, inicio, destino, peso= 0):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):
            nueva_arista= Arista(clave, inicio, destino, peso)
            self.numero_aristas= self.numero_aristas+ 1
            self.lista_aristas[clave]= nueva_arista
            if inicio == destino:
                self.lista_vertices[inicio].conectar(destino)
                self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado+ 1
            else:
                self.lista_vertices[inicio].conectar(destino)
                self.lista_vertices[destino].conectar(inicio)

            return True
        else:
            return False

    def buscarVertice(self, clave):
        if clave in self.lista_vertices:
            return self.lista_vertices[clave]
        else:
            return None

    def buscarArista(self, inicio, destino):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):
            for arista in self.lista_aristas:
                if (self.lista_aristas[arista].origen == inicio) and (self.lista_aristas[arista].destino == destino):
                    return self.lista_aristas[arista]
                elif (self.lista_aristas[arista].origen == destino) and (self.lista_aristas[arista].destino == inicio):
                    return self.lista_aristas[arista]
            return None
        else:
            return None

    def copiar(self):
        return copy.deepcopy(self)

    def eliminarVertice(self, clave):
        if clave in self.lista_vertices:
            for vertice in self.lista_vertices:
                if self.lista_vertices[vertice].existeConexion(clave):
                    self.lista_vertices[vertice].eliminarConexion(clave)
                    self.numero_aristas - 1
            self.numero_vertices= self.numero_vertices- 1
            del self.lista_vertices[clave]
            return True
        else:
            return False


    def eliminarArista(self, inicio, destino):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):
            if self.lista_vertices[inicio].existeConexion(destino):
                if inicio == destino:
                    self.lista_vertices[inicio].eliminarConexion(destino)
                    self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado- 1
                else:
                    self.lista_vertices[inicio].eliminarConexion(destino)
                    self.lista_vertices[destino].eliminarConexion(inicio)
            arista_existe= self.buscarArista(inicio, destino)
            if arista_existe != None:
                del self.lista_aristas[arista_existe.id]
            
            self.numero_aristas= self.numero_aristas - 1
            return True
        else:
            return False

    def existeArista(self, vertice):
        for arista in self.lista_aristas:
            if self.lista_aristas[arista].origen == vertice or self.lista_aristas[arista].destino == vertice:
                return True
        
        return False


    def gradoVertice(self, clave):
        if clave in self.lista_vertices:
            return self.lista_vertices[clave].obtenerGrado()
        else:
            return -1

    def numeroVertices(self):
        return self.numero_vertices

    def numeroAristas(self):
        return self.numero_aristas

    def vaciarVertice(self, clave):
        if clave in self.lista_vertices:
            existe_arista= True
            while existe_arista:
                for arista in self.lista_aristas:
                    if (self.lista_aristas[arista].origen == clave) or (self.lista_aristas[arista].destino == clave):
                        del self.lista_aristas[arista]
                    
                    self.numero_aristas= self.numero_aristas- 1
                    break
                if not self.existeArista(clave):
                    existe_arista= False

            for vertice in self.lista_vertices:
                if self.lista_vertices[vertice].existeConexion(clave):
                    while clave in self.lista_vertices[vertice].lista_conectado:
                        self.lista_vertices[vertice].eliminarConexion(clave)
                
            self.lista_vertices[clave].vaciar()
            return True
        else:
            return False

    def vaciarGrafica(self):
        self.lista_aristas.clear()
        self.lista_vertices.clear()
        self.numero_aristas= 0
        self.numero_vertices= 0
    
    def restablecerVertice(self):
        for vertice in self.lista_vertices:
            self.lista_vertices[vertice].color= -1
            self.lista_vertices[vertice].bandera= 0

    def bipartita(self, clave):
        cola= []
        cola.append(clave)

        while cola:
            u= cola.pop()
            if self.lista_vertices[u].existeConexion(u):
                return False

            for vertice in self.lista_vertices[u].lista_conectado:
                if self.lista_vertices[vertice].color== -1:
                    self.lista_vertices[vertice].color= 1- self.lista_vertices[u].color
                    cola.append(vertice)
                    self.lista_vertices[vertice].bandera= 1
                elif self.lista_vertices[vertice].color== self.lista_vertices[u].color:
                    return False
        return True

    def esBipartita(self):
        lista_v= []
        lista_u= []
        for vertice in self.lista_vertices:
            if self.lista_vertices[vertice].bandera== 0:
                self.lista_vertices[vertice].color= 1
                if not self.bipartita(vertice):
                    self.restablecerVertice()
                    return False
            if self.lista_vertices[vertice].color== 1:
                lista_v.append(self.lista_vertices[vertice].id)
            elif self.lista_vertices[vertice].color== 0:
                lista_u.append(self.lista_vertices[vertice].id)
            self.lista_vertices[vertice].bandera= 1

        print("Es bipartita")
        print("V: %s"%(lista_v))
        print("U: %s"%(lista_u))
        self.restablecerVertice()
        return True

    def conexa(self):
        cola= []
        cola.append(list(self.lista_vertices.keys())[0])
        self.lista_vertices[list(self.lista_vertices.keys())[0]].bandera= 1

        while cola:
            u= cola.pop(0)
            for vertice in self.lista_vertices[u].lista_conectado:
                if self.lista_vertices[vertice].bandera== 0:
                    cola.append(vertice)
                    self.lista_vertices[vertice].bandera= 1

        num_banderas= 0
        for nodo in self.lista_vertices:
            if self.lista_vertices[nodo].bandera== 1:
                num_banderas= num_banderas+ 1
                self.lista_vertices[nodo].bandera= 0

        if num_banderas == self.numero_vertices:
            return True
        else:
            return False
        
    def algoritmoFleury(self):
        impares= 0
        inicio= self.lista_vertices[list(self.lista_vertices.keys())[0]]
        copia = self.copiar()
        cola= []
        cola_vertices= []

        for vertice in self.lista_vertices:
            if (self.lista_vertices[vertice].grado % 2) != 0:
                impares= impares + 1
                inicio= self.lista_vertices[vertice]
 
        if impares != 0 and impares != 2:
            print("Erorr: La cantidad de nodos de grado impar no cumple.")
            return False

        if not self.conexa():
            print("Erorr: La grafica no es conexa.")
            return False

        while copia.numero_aristas != 0:
            for vecino in copia.lista_vertices[inicio.id].lista_conectado:
                destino= vecino
                arista= copia.buscarArista(inicio.id, vecino)
                cola.append(arista)
                cola_vertices.append(inicio)
                aux= copia.copiar()
                aux.eliminarArista(inicio.id, vecino)
                if len(copia.lista_vertices[inicio.id].lista_conectado) == 1:
                    copia.eliminarArista(inicio.id, vecino)
                    copia.eliminarVertice(inicio.id)
                    inicio= copia.buscarVertice(destino)
                    break
                elif aux.conexa():
                    copia.eliminarArista(inicio.id, vecino)
                    inicio= copia.buscarVertice(destino)
                    break
                else:
                    cola.pop(-1)
                    cola_vertices.pop(-1)
        if impares == 0:
            print("El paseo de Euler es cerrado.")
            
        else:
            print("El paseo de Euler es abierto.")
        cola_vertices.append(inicio)
        camino= []
        while cola_vertices:
            v= cola_vertices.pop()
            camino.append(v.id)
            if cola:
                a= cola.pop()
                camino.append(a.id)
        print(camino)
        del copia
        del aux
        return True

    def busquedas(self, tipo):
        grafiquita= Grafica()
        frontera= []
        frontera.append(self.lista_vertices[list(self.lista_vertices.keys())[0]]) #Agregamos el primer vertice de la grafica
        num_explorados= 0
        bosque= False
        i= 0 #Variable para los Id de las aristas

        while True:
            if num_explorados== self.numero_vertices: #Revisar ya se exploraron todos los vertices
                break
            elif len(frontera)== 0: #Si es True, es un bosque
                bosque= True
                for vertice in self.lista_vertices:
                    if self.lista_vertices[vertice].bandera== 0:
                        frontera.append(self.lista_vertices[vertice])
                        break

            if tipo== 0: #Busqueda a lo profundo (0)
                v= frontera.pop()
                num_explorados+= 1

            elif tipo== 1: #Busqueda a los ancho (1)
                v= frontera[0]
                frontera= frontera[1:]
                num_explorados+= 1

            v.bandera= 1
            grafiquita.agregarVertice(v.id)

            for vertice in self.lista_vertices[v.id].lista_conectado:
                if (vertice not in frontera) and (self.lista_vertices[vertice].bandera== 0):
                    frontera.append(self.lista_vertices[vertice])
                    grafiquita.agregarVertice(vertice)
                    grafiquita.agregarArista('e'+str(i),v.id, vertice)
                    i+= 1
                    print(frontera)
                    print(vertice)
                    input()
            
        
        if bosque:
            print("El bosque es:")
        else:
            print("El árbol de expansión es:")

        for v in grafiquita:
            print(v)
        print(grafiquita.numero_aristas)
        del grafiquita
        self.restablecerVertice()
        return

            

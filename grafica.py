import copy
class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.grado= 0
        self.lista_conectado= []
        self.color= -1
    
    def __del__(self):
        del self
    
    def __str__(self):
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
        return str(self.id) + 'Origen: ' + str(self.origen) + ' Destino: ' + str(destino)

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
    
    def restablecerColores(self):
        for vertice in self.lista_vertices:
            self.lista_vertices[vertice].color= -1

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
                elif self.lista_vertices[vertice].color== self.lista_vertices[u].color:
                    return False
        return True

    def esBipartita(self):
        lista_v= []
        lista_u= []
        for vertice in self.lista_vertices:
            if self.lista_vertices[vertice].color== -1:
                self.lista_vertices[list(self.lista_vertices.keys())[0]].color= 1
                if not self.bipartita(vertice):
                    self.restablecerColores()
                    return False
            if self.lista_vertices[vertice].color== 1:
                lista_v.append(self.lista_vertices[vertice].id)
            elif self.lista_vertices[vertice].color== 0:
                lista_u.append(self.lista_vertices[vertice].id)
        print("Es bipartita")
        print("V: %s"%(lista_v))
        print("U: %s"%(lista_u))
        self.restablecerColores()
        return True

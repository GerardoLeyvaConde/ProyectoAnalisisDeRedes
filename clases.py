from collections import defaultdict

class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.grado= 0
        self.conectadoA= {}
        self.listaVecinos= []
    
    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino]= ponderacion
        self.grado= self.grado+ 1
        self.listaVecinos.append(vecino.id)

    def __str__(self):
        return str(self.id) + ' conectado a: ' + str([x for x in self.listaVecinos])
    
    def obtenerGrado(self):
        return self.grado

    def obtenerVecino(self, clave):
        for n in self.conectadoA:  
            if n.id == clave:
                return True
        return False

    def obtenerConexiones(self):
        return self.conectadoA.keys()

    def obtenerId(self):
        return self.id

    def obtenerPonderacion(self, vecino):
        return self.conectadoA[vecino]

    def eliminarVecino(self, clave):
        self.listaVecinos.remove(clave)
        self.grado= self.grado- 1
        if clave in self.listaVecinos:
            return
        else:
            for n in self.conectadoA:
                if n.id == clave:
                    del self.conectadoA[n]
                    return

    def vaciar(self):
        self.conectadoA= {}
        self.listaVecinos= []
        self.grado= 0
        
class Grafica:
    def __init__(self):
        self.listaVertices= {}
        self.numVertices= 0
        self.numAristas= 0
    
    def agregarVertice(self, clave):
        if clave not in self.listaVertices:        
            self.numVertices= self.numVertices + 1
            nuevoVertice= Vertice(clave)
            self.listaVertices[clave]= nuevoVertice
            return nuevoVertice
        else:
            return None

    def agregarArista(self, de, a, costo= 0):
        self.numAristas= self.numAristas + 1
        if de not in self.listaVertices:
            nv= self.agregarVertice(de)
        if a not in self.listaVertices:
            nv= self.agregarVertice(a)
        if a == de:
            self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
            self.listaVertices[de].grado= self.listaVertices[de].grado + 1
        else:
            self.listaVertices[de].agregarVecino(self.listaVertices[a], costo)
            self.listaVertices[a].agregarVecino(self.listaVertices[de], costo)

    def gradoVertice(self, clave):
        if clave in self.listaVertices:
            return self.listaVertices[clave].obtenerGrado()
        else:
            return None

    def buscarVertice(self, n):
        if n in self.listaVertices:
            return self.listaVertices[n]
        else:
            return None

    def buscarArista(self, inicio, destino):
        if (inicio in self.listaVertices) and (destino in self.listaVertices):
            if self.listaVertices[inicio].obtenerVecino(destino):
                return True
            else:
                return False
        else:
            return False
    
    def obtenerVertices(self):
        return self.listaVertices.keys()

    def numeroNodos(self):
        return self.numVertices

    def numeroAristas(self):
        return self.numAristas


    def __contains__(self, n):
        return n in self.listaVertices

    def eliminarArista(self, inicio, destino):
        if (inicio in self.listaVertices) and (destino in self.listaVertices):
            if self.listaVertices[inicio].obtenerVecino(destino):
                self.numAristas= self.numAristas - 1
                if inicio == destino:
                    self.listaVertices[inicio].eliminarVecino(destino)
                    self.listaVertices[inicio].grado= self.listaVertices[inicio].grado - 1
                else: 
                    self.listaVertices[inicio].eliminarVecino(destino)
                    self.listaVertices[destino].eliminarVecino(inicio)
                return True
            else:
                return False
        else:
            return False

    def eliminarVertice(self, n):
        if n in self.listaVertices:
            self.numVertices= self.numVertices - 1
            del self.listaVertices[n]
            for v in self.listaVertices:
                if self.listaVertices[v].obtenerVecino(n):
                    self.listaVertices[v].eliminarVecino(n)
                    self.numAristas= self.numAristas - 1
            return True
        else:
            return False

        
    def vaciarVertice(self, n):
        if n in self.listaVertices:
            # aristas_v= len(self.listaVertices[n].listaVecinos)
            # self.numAristas= self.numAristas - aristas_v
            for v in self.listaVertices:
                if self.listaVertices[v].obtenerVecino(n):
                    while n in self.listaVertices[v].listaVecinos:
                        self.listaVertices[v].eliminarVecino(n)
                        self.numAristas= self.numAristas - 1

            self.listaVertices[n].vaciar()
            return True
        else:
            return False

    def vaciarGrafica(self):    
        self.listaVertices.clear()
        self.numAristas= 0
        self.numVertices= 0

    def __iter__(self):
        return iter(self.listaVertices.values())

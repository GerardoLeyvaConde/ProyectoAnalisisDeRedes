class Vertice:
    def __init__(self, clave):
        self.id= clave
        self.grado= 0
        self.conectadoA= {}
    
    def agregarVecino(self, vecino, ponderacion=0):
        self.conectadoA[vecino]= ponderacion
        self.grado= self.grado + 1

    def __str__(self):
        return str(self.id) + ' conectado a: ' + str([x.id for x in self.conectadoA])
    
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
        for n in self.conectadoA:
            if n.id == clave:
                del self.conectadoA[n]
                self.grado= self.grado - 1
                return

    def vaciar(self):
        self.conectadoA= {}
        
class Grafica:
    def __init__(self):
        self.listaVertices= {}
        self.numVertices= 0
        self.numAristas= 0
    
    def agregarVertice(self, clave):
        self.numVertices= self.numVertices + 1
        nuevoVertice= Vertice(clave)
        self.listaVertices[clave]= nuevoVertice
        return nuevoVertice

    def agregarArista(self, de, a, costo= 0):
        self.numAristas= self.numAristas + 1
        if de not in self.listaVertices:
            nv= self.agregarVertice(de)
        if a not in self.listaVertices:
            nv= self.agregarVertice(a)
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
                self.listaVertices[inicio].eliminarVecino(destino)
                self.listaVertices[destino].eliminarVecino(inicio)
                return True
            else:
                return False
        else:
            return False

    def eliminarVertice(self, n):
        self.numVertices= self.numVertices - 1
        del self.listaVertices[n]
        for v in self.listaVertices:
            if self.listaVertices[v].obtenerVecino(n):
                self.listaVertices[v].eliminarVecino(n)
                self.numAristas= self.numAristas - 1
        
    def vaciarVertice(self, n):
        if n in self.listaVertices:
            self.listaVertices[n].vaciar()
            for v in self.listaVertices:
                if self.listaVertices[v].obtenerVecino(n):
                    self.listaVertices[v].eliminarVecino(n)
                    self.numAristas= self.numAristas - 1
            return True
        else:
            return False

    def vacairGrafica(self):    
        self.listaVertices.clear()
        self.numAristas= 0
        self.numVertices= 0

    def __iter__(self):
        return iter(self.listaVertices.values())

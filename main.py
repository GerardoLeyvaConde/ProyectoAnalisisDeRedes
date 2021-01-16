import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt 

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

#df= pd.DataFrame({"de": de, 'a': a})

#G= nx.from_pandas_edgelist(df, 'de', 'a')
#nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="o", alpha=0.5, linewidths=4, font_size=25, font_color="grey", font_weight="bold", width=2, edge_color="grey")
#plt.show()

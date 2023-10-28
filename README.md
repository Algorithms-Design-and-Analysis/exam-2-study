# Analisys questions 

## 1. Explique cual es la complejidad temporal de los algoritmos vistos en clase: BFS, Dijkstra(Priority Queue), Bellman-Ford, kruskal y Floyd-Warshall.

- BFS: Para este algorimo la complejidad es de $O(V+E)$, esto es porque BFS recorre todos los vertices y arcos del grafo.

- Dijkstra(Priority Queue): Para este algorimo la complejidad es de $O((V+E)logV)$, esto es porque por cada vertice se recorren todos sus adyacentes y dentro de este recorrido de haces operaciones de pop y push en una cola de prioridad lo que toma un tiempo de $O(logV)$.

- Bellman-Ford: Para este algorimo la complejidad es de $O(VE)$, estos es porque cada arco se recorre $V-1$ veces ya que para cualquier nodo el camino más corto tendrá en el peor de los casos $V-1$ arcos.

- Kruskal: Para este algorimo la complejidad es de $O(ElogE)$, esto es porque cada arco se recorre una vez, los arcos están contenidos en una priority queue y extraer siempre el arco mínimo toma una complejidad de $logE$.

- Floyd-Warshall: Para este algorimo la complejidad es de $O(V^3)$, estos es porque hay 3 fors anidados que recorren todos los arcos.

## 2. Explique por que el algoritmo de Dijkstra no funciona en un grafo que tiene arcos negativos, de ser necesario puede usar un ejemplo para ilustrar su explicación.

No funciona por su enfoque greedy y porque Dijkstra aplica relajamiento a todos los arcos solo por una vez ya que espera que despues del primera relajamiento ya se tenga la distance más corta al nodo final de ese arco, por lo que al tener pesos negativos con solo un relajamiento por arco no es seguro llega a la distancia minima. Por ejemplo:

![Alt text](image.png)

Se parte desde $A$, se marca como visitado y las distances minimas a $B$ y $C$ quedan como 5 y 6 respectivamente, se pasa a $B$ por ser el arco minimo pero no tiene adyacentes así que se marca como visitado y se pasa a $C$ en donde hay un arco que puede dar una distancia menor de $A$ a $C$, pero no sigue ese camino porque B ya se marcó anteriormente como visidado.

## 3. Un grafo bipartito, es un grafo tal que el conjunto de nodos se puede expresar como dos conjuntos disjuntos, de manera que no hay dos nodos del mismo conjunto que sean adyacentes. Diseñe un algoritmo que reciba un grafo, en su implantación indique si su grafo esta implementado como lista o matriz de adyacencia, y retorne $True$ si el grafo es bipartito y $False$ en otro caso. La complejidad no debe superar $O(VE)$, donde V es el conjunto de nodos y E el conjunto de arcos del grafo.

Algoritmo en is_bipartite.py. Recibe una lista de adyacencia.

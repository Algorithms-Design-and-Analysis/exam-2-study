# Analisys questions 

## 1. Explique cual es la complejidad temporal de los algoritmos vistos en clase: BFS, Dijkstra(Priority Queue), Bellman-Ford, kruskal y Floyd-Warshall.

- BFS: Para este algorimo la complejidad es de $O(V+E)$, estos es porque BFS recorre todos los vertices y arcos del grafo.

- Dijkstra(Priority Queue): Para este algorimo la complejidad es de $O((V+E)logV)$, estos es porque por cada vertice se recorren todos sus adyacentes y dentro de este recorrido de haces operaciones de pop y push en una cola de prioridad lo que toma un tiempo de $O(logV)$.

- Bellman-Ford: Para este algorimo la complejidad es de $O(VE)$, estos es porque cada arco se recorre $V-1$ veces ya que para cualquier nodo el camino más corto tendrá en el peor de los casos $V-1$ arcos.
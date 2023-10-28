"""
Esta solucion funciona siempre y cuando no hayan nodos que no estén conectados a ningun otro
https://leetcode.com/problems/is-graph-bipartite/
"""


def isBipartite(graph) -> bool:

        set_1 = []
        set_1_adjacents = []
        set_2 = []
        set_2_adjacents = []

        stack = []
        visited = [False] * len(graph)

        depth = 1
        node_depth = []
        for node in range(len(graph)):
            if len(graph[node]) > 0:
                stack.append(node)
                visited[node] = True
                node_depth.append((node,1))
                set_1.append((node,1))
                set_1_adjacents += graph[node]
                break

        while stack:
            vertex = stack.pop()
            vertex_adjacents = graph[vertex]
            depth += 1
            for adjacent in vertex_adjacents:
                if not visited[adjacent]:
                    stack.append(adjacent)
                    visited[adjacent] = True
                    node_depth.append((adjacent,depth))
                    if depth%2==0:
                         if adjacent in set_2_adjacents:
                              return False
                         set_2_adjacents += graph[adjacent]
                         set_2.append((adjacent,depth))
                    else:
                        if adjacent in set_1_adjacents:
                              return False
                        set_1_adjacents += graph[adjacent]
                        set_1.append((adjacent,depth))

        return True
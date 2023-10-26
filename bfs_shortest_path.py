"""
https://www.hackerrank.com/challenges/bfsshortreach/problem"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    
    adjacency_matrix = [[float("inf") for _ in range(n)]for _ in range(n)]
    for edge in edges:
        vertex_1 = int(edge[0])
        vertex_2 = int(edge[1])
        adjacency_matrix[vertex_1-1][vertex_2-1] = 6
        adjacency_matrix[vertex_2-1][vertex_1-1] = 6
    
    visited = [False] * n
    queue = [(s-1, 0)]
    output = [float('inf')] * n
    output[s-1] = -1
    while len(queue) > 0:
        vertex_info = queue.pop(0)
        vertex = vertex_info[0]
        vertex_level = vertex_info[1]
        if vertex_level != 0:
            output[vertex] = vertex_level*6
        visited[vertex] = True
        for neighbor in range(len(adjacency_matrix[vertex])):
            
            if adjacency_matrix[vertex][neighbor] != float("inf") and not visited[neighbor]:
                queue.append((neighbor, vertex_level+1))
                
    output.remove(-1)

    for pos in range(len(output)):
        output[pos] = -1 if output[pos] == float('inf') else output[pos]
    
    return output

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        print(result)



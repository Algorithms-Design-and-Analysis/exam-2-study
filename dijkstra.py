#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'shortestReach' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER s
#

"""
https://www.hackerrank.com/challenges/dijkstrashortreach/
"""

def shortestReach(n, edges, s):
    
    adjacency_matrix = []
    for _ in range(n):
        row = [float('inf')] * n
        adjacency_matrix.append(row)
    
    for intial_vertex, final_vertex, weight in edges:
        adjacency_matrix[intial_vertex-1][final_vertex-1] = adjacency_matrix[final_vertex-1][intial_vertex-1] = weight
        
    visiteds = [False] * n
    distances = [float('inf')] * n
    distances[s-1] = 0
    priority_queue = []
    heapq.heappush(priority_queue, (0, s-1))
    while priority_queue:
        vertex = heapq.heappop(priority_queue)
        visiteds[vertex[1]] = True
        vertex_adjacents = adjacency_matrix[vertex[1]]
        for adjacent in range(len(vertex_adjacents)):
            if vertex_adjacents[adjacent] != float('inf') and not visiteds[adjacent] and (vertex[0]+vertex_adjacents[adjacent])<distances[adjacent]:
                distances[adjacent] = vertex[0]+vertex_adjacents[adjacent]
                heapq.heappush(priority_queue, (vertex[0]+vertex_adjacents[adjacent], adjacent))
    
    distances.pop(s-1)
    
    for pos in range(len(distances)):
        distances[pos] = -1 if distances[pos] == float('inf') else distances[pos]
            
    
    return distances

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = shortestReach(n, edges, s)
        print(result)

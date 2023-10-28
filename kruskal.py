#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#

"""
https://www.hackerrank.com/challenges/kruskalmstrsub/problem
"""

def kruskals(g_nodes, g_from, g_to, g_weight):
    
    edges = []
    for pos in range(len(g_from)):
        heapq.heappush(edges, (g_weight[pos], g_from[pos], g_to[pos]))
        
    vertexes_added = [False]*g_nodes
    total_weight = 0
    for _ in range(len(g_from)):
        edge_weight, initial_vertex, final_Vertex = heapq.heappop(edges)
        if not vertexes_added[final_Vertex-1]:
            vertexes_added[initial_vertex-1] = vertexes_added[final_Vertex-1] = True
            total_weight +=edge_weight
    return total_weight

if __name__ == '__main__':

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)
    print(res)
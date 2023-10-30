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
    
    # Create the min priority queue with the edges
    edges = []
    for pos in range(len(g_from)):
        heapq.heappush(edges, (g_weight[pos], g_from[pos], g_to[pos]))
        
    # Create the structures for disjoint-set operations, initial a vertex is its self parent with 1 children
    parents = [i for i in range(g_nodes)]
    childrens = [1 for _ in range(g_nodes)]
    total_weight = 0

    #Kruskal algorithm
    while len(edges) > 0:

        edge_weight, initial_vertex, final_vertex = heapq.heappop(edges)

        # Navigate in the set tree until reach the parent for each vertex
        initial_vertex_set = parents[initial_vertex-1] 
        while initial_vertex_set != initial_vertex-1: 
            initial_vertex = initial_vertex_set + 1
            initial_vertex_set = parents[initial_vertex_set]
        final_vertex_set = parents[final_vertex-1]
        while final_vertex_set != final_vertex-1:
            final_vertex = final_vertex_set + 1
            final_vertex_set = parents[final_vertex_set]

        # Normal continuation of algorithm
        if initial_vertex_set != final_vertex_set:
            total_weight +=edge_weight
            if childrens[initial_vertex_set] >= childrens[final_vertex_set]:
                final_vertex_childrens = childrens[final_vertex_set]
                parents[final_vertex_set] = parents[initial_vertex_set]
                childrens[parents[final_vertex_set]] += final_vertex_childrens
            else:
                initial_vertex_childrens = childrens[initial_vertex_set]
                parents[initial_vertex_set] = parents[final_vertex_set]
                childrens[parents[initial_vertex_set]] += initial_vertex_childrens
            
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
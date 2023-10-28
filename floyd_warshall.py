#!/bin/python3

import math
import os
import random
import re
import sys

"""
https://www.hackerrank.com/challenges/floyd-city-of-blinding-lights/problem
"""

def floyd_Warshall(initial_vertexes, final_vertexes, edges_weight):
    
    adjacency_matrix = [[0 if i==j else float('inf') for i in range(len(initial_vertexes))]for j in range(len(initial_vertexes))]
    for pos in range(len(initial_vertexes)):
        initial_vertex = initial_vertexes[pos]-1
        final_vertex = final_vertexes[pos]-1 
        edge_weight = edges_weight[pos] 
        adjacency_matrix[initial_vertex][final_vertex] = edge_weight
        
    for intermediate_vertex in range(len(adjacency_matrix)):
        for initial_vertex in range(len(adjacency_matrix)):
            for final_vertex in range(len(adjacency_matrix)):
                adjacency_matrix[initial_vertex][final_vertex] = adjacency_matrix[initial_vertex][intermediate_vertex] + adjacency_matrix[intermediate_vertex][final_vertex] if adjacency_matrix[initial_vertex][intermediate_vertex] + adjacency_matrix[intermediate_vertex][final_vertex] < adjacency_matrix[initial_vertex][final_vertex] else adjacency_matrix[initial_vertex][final_vertex]
                
    for initial_vertex in range(len(adjacency_matrix)):
        for final_vertex in range(len(adjacency_matrix)):
            adjacency_matrix[initial_vertex][final_vertex] = -1 if adjacency_matrix[initial_vertex][final_vertex] == float('inf') else adjacency_matrix[initial_vertex][final_vertex]
            
        
    return adjacency_matrix
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    road_nodes, road_edges = map(int, input().rstrip().split())

    road_from = [0] * road_edges
    road_to = [0] * road_edges
    road_weight = [0] * road_edges

    for i in range(road_edges):
        road_from[i], road_to[i], road_weight[i] = map(int, input().rstrip().split())

    q = int(input().strip())
    
    distances = floyd_Warshall(road_from, road_to, road_weight)

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        x = int(first_multiple_input[0])

        y = int(first_multiple_input[1])
        #!/bin/python3
        fptr.write(str(distances[x-1][y-1]))
        fptr.write("\n")
    
    fptr.close()


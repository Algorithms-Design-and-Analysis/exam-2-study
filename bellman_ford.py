#User function Template for python3

"""
https://practice.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1?utm_source=geeksforgeeks&utm_medium=ml_article_practice_tab&utm_campaign=article_practice_tab
"""

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        
        distances = [float('inf')] * V
        distances[S] = 0
        for _ in range(V-1):
            for initial_node, final_node, distance in edges:
                distances[final_node] = distances[initial_node] + distance if distances[initial_node] + distance < distances[final_node] else distances[final_node]  
        
        for initial_node, final_node, distance in edges:
            if distances[initial_node] + distance < distances[final_node]:
                return [-1]
                
        for pos in range(len(distances)):
            distances[pos] = 100000000 if distances[pos]==float('inf') else distances[pos]
        
        return distances
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends
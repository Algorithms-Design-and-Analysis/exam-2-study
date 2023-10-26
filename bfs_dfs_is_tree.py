"""
given a graph as a adjacency list, determine is the graph is a tree
"""

def dfs(adjacency_list):
    edges_count = 0
    stack = [0]
    visiteds = [False] * len(adjacency_list)
    while len(stack)>0:
        vertex = stack.pop()
        visiteds[vertex] = True
        neighbors = adjacency_list[vertex]
        for neighbor in neighbors:
            if not visiteds[neighbor]:
                edges_count += 1
                stack.append(neighbor)
                
            
    return edges_count == len(adjacency_list)-1

def bfs(adjacency_list):
    edges_count = 0
    queue = [0]
    visiteds = [False] * len(adjacency_list)
    while len(queue)>0:
        vertex = queue.pop(0)
        neighbors = adjacency_list[vertex]
        for neighbor in neighbors:
            if not visiteds[neighbor]:
                edges_count += 1
                queue.append(neighbor)
                visiteds[vertex] = True
                
            
    return edges_count == len(adjacency_list)-1
            

if __name__ == '__main__':
    cases_number = int(input())
    for _ in range(cases_number):
        print(bfs(eval(input())))
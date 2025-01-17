#!/usr/bin/env python3

def bfs_traversal(graph, initial_node):
    # your implementation here
    # your function will return a list!
    q = []
    visited = []
    #put node at end
    q.append(initial_node)
    while q:
        #get first = FIFO
        root = q.pop(0)
        if root in visited: #if in, skip
            continue
        visited.append(root)
        for c in graph[root]:
            q.append(c)
    
    return visited


def main():
    graph = {"+": ["*",3], "*":[2,7], 2:[],7:[],3:[]}
    initial_node = "+"
    visited = bfs_traversal(graph, initial_node)
    print(visited)
    
    print('\n')  

    graph =  {0: [1,3], 1:[2,3], 2:[3,1], 3:[0,1]}
    initial_node = 0
    visited = bfs_traversal(graph, initial_node)
    print(visited)


if __name__ == "__main__":
    main()
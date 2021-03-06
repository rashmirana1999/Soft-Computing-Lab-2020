"""
AIM:Write a program to implement bfs and dfs with the input of graph and the goal node to be searched, your output will show the path from the root node to goal node only

Solution:
"""
def bfs(graph,start,search):
    explored = []
    queue = [start]
    found = 1
    while found:
        node = queue.pop(0)
        if(node == search):
            found = 0
        if node not in explored:
            explored.append(node)
            neighbours = graph[node]
        for neighbour in neighbours:
            queue.append(neighbour)
    print(explored)

search = int(input("enter the number you want to search-"))
graph = {1: [2, 3, 5],
         2: [1,4, 5],
         3: [1, 6, 7],
         4: [2],
         5: [1, 2,4],
         6: [3],
         7: [3]}
bfs(graph,1,search)

"""
OUTPUT
enter the number you want to search-3
[1, 2, 3]
"""

from collections import defaultdict
from pprint import pprint

class Graph(object):
    def __init__(self, GraphInput):
        self.graph = defaultdict(set)
        # Sets the dictionary type to keys of sets
        self.add_GraphInput(GraphInput)

    def add_GraphInput(self, GraphInput):
    # Adds the connections to the graph
        for node1, node2 in GraphInput:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)

GraphInput = [('A', 'B'), ('A', 'S'), ('S', 'C'), ('S', 'G'), ('E', 'H'),
              ('C', 'D'), ('C', 'E'), ('C', 'F'), ('F', 'G'), ('G', 'H'),]
g = Graph(GraphInput)
pprint(dict(g.graph))

print("\n######################################################\nDFS search:\n")

def dfs(graph, start):
    visited = set()
    stack = [start]
    textfile = open("Week 7 - dfs.txt","w")
    while stack:
        if len(visited) == len(g.graph.keys()):
            return
        vertex = stack.pop()
        textfile.write(vertex)
        if vertex not in visited:
            print("Vertex:",vertex)
            # Printed after the if, to avoid multi-prints for nodes
            # with multiple connections.
            
            visited.add(vertex)
            print("Visited:",visited)
            # Add the current node to visited

            print("Vertex Edges:",graph[vertex])
            stack.extend(graph[vertex] - visited)
            # Extend the stack with the nodes connected to vertex (Vertex Edges),
            # minus the nodes already visited. This avoids backtracking.
            # Remembering that 'graph' is just the dictionary, it knows the connections.
            # And that extend vs append, the first seperates the elements, append doesn't.
            print("Stack:",stack)
            print("-------------------")
    textfile.close

dfs(g.graph, 'A')

print("\n######################################################\nBFS search:\n")

# Uses the same principle as dfs, but with a queue not a stack.
def bfs(graph, start):
    visited = set()
    queue = [start]
    textfile = open("Week 7 - bfs.txt","w")
    while queue:
        if len(visited) == len(g.graph.keys()):
            return
        vertex = queue.pop(0)
        textfile.write(vertex)
        if vertex not in visited:
            print("Vertex:",vertex)
            
            visited.add(vertex)
            print("Visited:",visited)

            print("Vertex Edges:",graph[vertex])
            queue.extend(graph[vertex] - visited)
            # Extend the queue to include the connections, minus any already visited.
            # Repeat for next element in queue. FIFO.

            print("Queue:",queue)
            print("-------------------")
    textfile.close

bfs(g.graph, 'A')

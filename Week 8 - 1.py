from collections import defaultdict
from pprint import pprint

class Graph(object):
    def __init__(self, GraphInput):
        self.graph = defaultdict(set)
        self.weights = defaultdict(set)
        self.nodes = set()
        self.add_GraphInput(GraphInput)
        
    def add_GraphInput(self, GraphInput):
        for node1, node2, node3 in GraphInput:
            self.graph[node1].add(node2)
            self.graph[node2].add(node1)
        for node1, node2, node3 in GraphInput:
            self.weights[(node1, node2)] = node3
    def add_node(self, value):
        self.nodes.add(value)
            
Vertexs = ['A','B','C','D','E','F']
GraphInput = [('A', 'B', 7), ('A', 'C', 9), ('A', 'F', 14),
              ('B', 'C', 10), ('B', 'D', 15), ('C', 'D', 11),
              ('C', 'F', 2), ('D', 'E', 6), ('F', 'E', 9)]
g = Graph(GraphInput)

for node in Vertexs:
    g.add_node(node)

pprint(g.nodes) 
print("-------")
pprint(dict(g.graph)) 
print("-------")
pprint(dict(g.weights)) 
print("-------")

def dijkstras(graph, initial):
    visited = {initial: 0}
    # Visted keeps a contant log of the lowest weight achieved to reach each node.
    path = {}

    nodes = set(g.nodes)

    while nodes:
        
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            # In a case where there is no new minimum value.
            break
        # Picks the lowest node/best path to remove from the list.
        
        nodes.remove(min_node)
        # Nodes stores all the unvisted nodes, removing each time.
        current_weight = visited[min_node]

        for edge in g.graph[min_node]:
            try:
                weight = current_weight + g.weights[(min_node, edge)]
            except:
                #print(edge,"already visted.")
                continue
            if edge not in visited or weight < visited[edge]:
                print(visited)
                
                visited[edge] = weight
                path[edge] = min_node
                # Assigns the weights and paths to each directory.
                
                print("From:",path[edge],"to",edge,"costs",weight)
                print("-------")
            
    return "Visted",visited, "Path directory",path

pprint(dijkstras(Graph, 'A'))

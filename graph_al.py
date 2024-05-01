class Graph_Node:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return self.data


class Graph_AL:
    def __init__(self):
        self.adjacencyList = {} 
        '''Each key in the dictionary is a node and 
        the values are lists holding sets of neghibours with their corresponding weights.'''


    def add_vertex(self, data):
        new_node = Graph_Node(data)
        if new_node not in self.adjacencyList:
            self.adjacencyList[new_node]=[] 
        
    def add_edge(self, start: Graph_Node, end: Graph_Node, weight = 1):
        if start in self.adjacencyList and end not in self.adjacencyList[start]:
            self.adjacencyList[start].append((end, weight))
    
    def remove_vertex(self, node: Graph_Node):
        for vertex in self.adjacencyList:
            if vertex == node:
                self.adjacencyList.pop(vertex)
            else:
                if node in vertex:
                    print(True)

    
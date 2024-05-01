class Graph_Node:
    def __init__(self, data):
        self.data = data

    # def __str__ (self):
    #     return self.data
    
    def __repr__(self):
        return str(self.data)


class Graph_AL:
    def __init__(self):
        self.adjacencyList = {} 
        '''Each key in the dictionary is a node and 
        the values are lists holding sets of neghibours with their corresponding weights.'''


    def add_vertex(self, data):
        if isinstance(data, Graph_Node):
            if data not in self.adjacencyList:
                self.adjacencyList[data]={}
        else:
            new_node = Graph_Node(data)
            if new_node not in self.adjacencyList:
                self.adjacencyList[new_node]={} 
        
    def add_edge(self, start: Graph_Node, end: Graph_Node, weight = 1):
        if start in self.adjacencyList and end not in self.adjacencyList[start]:
            self.adjacencyList[start][end]= (end, weight)
        else:
            self.adjacencyList[start] = {end: (end, weight)}
    
    def remove_vertex(self, node: Graph_Node):
        keys_to_rm = []
        for vertex in self.adjacencyList:
            if vertex == node:
                keys_to_rm.append(vertex)
            else:
                print(self.adjacencyList[vertex])
                if node in self.adjacencyList[vertex]:
                    self.adjacencyList[vertex].pop(node)
        for i in keys_to_rm:
            del self.adjacencyList[i]
    
    def remove_edge(self, node1: Graph_Node, node2: Graph_Node):
        if node1 in self.adjacencyList and node2 in self.adjacencyList[node1]:
            self.adjacencyList[node1].pop(node2)
        if node2 in self.adjacencyList and node1 in self.adjacencyList[node2]:
            self.adjacencyList[node1].pop(node1)

    def get_vertices(self):
        vertices_list = []
        for vertex in self.adjacencyList:
            if vertex not in vertices_list:
                vertices_list.append(vertex)
            for node in self.adjacencyList[vertex]:
                if node not in vertices_list:
                    vertices_list.append(node)
        return vertices_list
    
    def get_edges(self):
        edges_list = []
        for vertex in self.adjacencyList:
            for node in self.adjacencyList[vertex]:
                edges_list.append((vertex, node))
        
        return edges_list
    
    def get_neighbours(self, node):
        if node in self.adjacencyList:
            return self.adjacencyList[node].keys().tolist()



n1 = Graph_Node("betse")
n2 = Graph_Node("tame")
n3 = Graph_Node("teme")
n4 = Graph_Node("ella")
n5 = Graph_Node("sam")
n6 = Graph_Node("sami")


gra = Graph_AL()
gra.add_vertex(n1)
gra.add_vertex(n2)
gra.add_vertex(n3)
gra.add_vertex(n4)
gra.add_vertex(n5)

gra.add_edge(n1, n2)
gra.add_edge(n1, n3)
gra.add_edge(n2, n3)
gra.add_edge(n3, n6)

print(gra.get_edges())
print(gra.get_neighbours(n1))
# print(gra.get_vertices())
# print(gra.adjacencyList.keys())
# # print(gra.adjacencyList)

# gra.remove_vertex(n3)
# print(gra.adjacencyList)
# print(gra.adjacencyList)

# gra.remove_edge(n1, n3)
# print(gra.adjacencyList)



    
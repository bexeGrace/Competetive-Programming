from collections import deque


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
            return list(self.adjacencyList[node].keys())
        
    def get_edge_weight(self, start: Graph_Node, end: Graph_Node):
        if start in self.adjacencyList:
            if end in self.adjacencyList[start]:
                return self.adjacencyList[start][end][1]

    def BFS(self, start: Graph_Node, end: Graph_Node):
        frontier = deque([start])
        reached = {start: None}

        if start == end:
            return start
        

        while len(frontier) > 0:
            node = frontier.popleft()
            for child in self.adjacencyList[node]:
                if child == end:
                    reached[child] = node
                    solution = deque([child])
                    parent = reached[child]
                    while parent is not None:
                        solution.appendleft(parent)
                        parent = reached[parent]
                    return list(solution)
                if child not in reached:
                    # print(child, node, reached)
                    reached[child] = node
                    frontier.append(child)
            
        return None
    
    def DFS(self, start: Graph_Node, end: Graph_Node):
        reached = {start: None} 

        def dfs_recursive(node):
            for child in self.adjacencyList[node]:
                if child not in reached:
                    if child == end:
                        reached[child] = node
                        print(reached)
                        solution = deque([child])
                        parent = reached[child]
                        while parent is not None:
                            solution.appendleft(parent)
                            parent = reached[parent]
                        return list(solution)
                    reached[child] = node
                    return dfs_recursive(child)

        return dfs_recursive(start)       
        

       


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

# print(gra.get_edges())
# print(gra.get_neighbours(n1))
# print(gra.get_edge_weight(n1, n2))

print(gra.DFS(n1, n6))
# print(gra.get_vertices())
# print(gra.adjacencyList.keys())
print(gra.adjacencyList)

# gra.remove_vertex(n3)
# print(gra.adjacencyList)
# print(gra.adjacencyList)

# gra.remove_edge(n1, n3)
# print(gra.adjacencyList)



    
class Graph_Node:
    def __init__(self, data):
        self.data = data


class Graph_AL:
    def __init__(self):
        self.adjacencyList = {} #Each key in the dictionary is a node and the values are lists holding sets of neghibours with their corresponding weights.

    
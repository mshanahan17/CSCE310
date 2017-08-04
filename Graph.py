# Simple graph class to use for CSCE 310
class Graph:
    def __init__(self, name=""):
        self.name = name
        self.list_neighbor = {}
        self.list_node = {}

    def add_node(self, node):
        self.list_node[node] = True

    def add_edge(self, node, nodebis):
        try:
            self.list_neighbor[node].append(nodebis)
        except:
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)

    def neighbors(self, node):
        try:
            return self.list_neighbor[node]
        except:
            return []

    def nodes(self):
        return self.list_node.keys()


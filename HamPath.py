import sys

import Graph

g = Graph.Graph()

# Reads the input file and builds a graph
with open(sys.argv[1]) as input1:
    num_a = input1.readline()
    for line in input1:
        str1 = line.strip()
        if str1 != "":
            str2 = str1.split(" ")
            g.add_node(str2[0])
            for v in str2:
                if v != str2[0]:
                    g.add_edge(str2[0], v)


# Function that traverses the graph trying to find a path that works
def find_path(graph, vertex, path=[]):
    path = path + [vertex]
    # If the path length is the same as total nodes you found a path
    if len(path) == len(g.nodes()):
        print("Hamiltonian Path: " + "%s" % (' '.join(path)))
        return True
    # Walks through the vertex neighbors and adds it to path if new edge
    for node in iter(graph.neighbors(vertex)):
        if node not in path:
            paths = find_path(graph, node, path)
            # returns true if path found so program can end
            if paths:
                return paths
    return None

# Goes through list of all vertices till path is found or not
for key in iter(g.nodes()):
    if find_path(g, key):
        break
    elif key == list(g.nodes())[-1]:
        print("No Hamiltonian Path")


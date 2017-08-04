import networkx as nx
import sys

# creates graph from input file
G = nx.Graph()
with open(sys.argv[1]) as input1:
    num = int(input1.readline().strip())
    for line in input1:
        vals = line.strip().split(" ")
        G.add_edge(int(vals[0]), int(vals[1]), weight=float(vals[2]))


# marks all vertices white initially
def reset(graph):
    for vertex in graph.nodes():
        graph.node[vertex]['color'] = 'white'
        graph.node[vertex]['dt'] = 0
        graph.node[vertex]['pt'] = 0
        graph.node[vertex]['parent'] = None


# Stack based implementation of DFS lexicographical ordering
def DFS(graph, start, count):
    # sets starting vertex
    graph.node[start]['dt'] = count
    graph.node[start]['color'] = 'grey'

    # adds to stack
    s = [start]

    while s:
        count += 1
        x = s[-1]
        y = None
        for v in sorted(graph[x]):
            if graph.node[v]['color'] is 'white':
                y = v
            if y is not None:
                break
        if y is None:
            s.pop()
            graph.node[x]['color'] = 'black'
            graph.node[x]['pt'] = count
        else:
            graph.node[y]['color'] = 'grey'
            graph.node[y]['dt'] = count
            s.append(y)
    return count


# Queue based BFS edge weight ordering
def BFS(graph, start, count):
    q = []
    graph.node[start]['dt'] = count
    graph.node[start]['color'] = 'grey'
    q.insert(0, start)

    while q:
        x = q.pop()
        for v in sorted(graph[x], key=lambda k: graph[x][k]['weight']):
            if graph.node[v]['color'] is 'white':
                count += 1
                graph.node[v]['dt'] = count
                graph.node[v]['color'] = 'grey'
                q.insert(0, v)
        count += 1
        graph.node[x]['pt'] = count
        graph.node[x]['color'] = 'black'
    return count


# sorts vertices by their marked discovery time
def sort_graph(graph, val):
    return sorted(graph.nodes(data=True), key=lambda k: k[1][val])


count = 1
reset(G)
for v in sorted(G.nodes()):
    if G.node[v]['color'] is 'white':
        count = DFS(G, v, count)
disc_time = sort_graph(G, 'dt')
# outputs vertices by discover time
print("Depth First Search Traversal")
print([x[0] for x in disc_time])

count = 1
reset(G)
for x in sorted(G.nodes()):
    if G.node[x]['color'] is 'white':
        count = BFS(G, x, count)
disc_time = sort_graph(G, 'dt')
# outputs vertices by discover time
print("\nBreadth First Search Traversal")
print([x[0] for x in disc_time])


# Stack based implementation of DFS modified to check for cycles
def DFS2(graph, start, count):
    # sets starting vertex
    graph.node[start]['dt'] = count
    graph.node[start]['color'] = 'grey'

    # adds to stack
    s = [start]

    while s:
        count += 1
        x = s[-1]
        y = None
        for v in graph[x]:
            if graph.node[v]['color'] is 'grey':
                if graph.node[x]['parent'] is not v:
                    return True
            if graph.node[v]['color'] is 'white':
                graph.node[v]['parent'] = x
                y = v
            if y is not None:
                break
        if y is None:
            s.pop()
            graph.node[x]['color'] = 'black'
            graph.node[x]['pt'] = count
        else:
            graph.node[y]['color'] = 'grey'
            graph.node[y]['dt'] = count
            s.append(y)
    return False


# Kruskal's minimum spanning tree algorithm
def kruskal(G):
    new_graph = nx.Graph()
    edges = sorted(G.edges(data=True), key=lambda t: t[2]['weight'])

    for edge in edges:
        u1 = edge[0]
        v1 = edge[1]
        weight1 = edge[2]['weight']
        new_graph.add_edge(u1, v1, weight=weight1)
        reset(new_graph)
        cycle2 = DFS2(new_graph, new_graph.edges()[0][0], 1)
        if cycle2:
            new_graph.remove_edge(u1, v1)
    print("\nMinimum Spanning Tree:")
    print("V = " + str(sorted(new_graph.nodes())))
    print("E = " + str(new_graph.edges()))
    print("Weights = [" + ', '.join('{}'.format(el[2]['weight'])
                                    for el in new_graph.edges(data=True)) + "]")
    weight = 0
    for edge in new_graph.edges(data=True):
        weight += edge[2]['weight']
    print("Total Weight: %.2f" % weight)


reset(G)
kruskal(G)


# Floyd-Warshall shortest paths algorithm
INF = 999999999

D = [[INF for i in range(len(G.nodes()))] for j in range(len(G.nodes()))]
S = [[-1 for i in range(len(G.nodes()))] for j in range(len(G.nodes()))]

for i in range(len(D) - 1, -1, -1):
    for j in range(len(D)):
        if i != j:
            S[i][j] = j
            if G.get_edge_data(G.nodes()[i], G.nodes()[j]) is None:
                D[i][j] = INF
            else:
                D[i][j] = G.get_edge_data(G.nodes()[i], G.nodes()[j])['weight']
        else:
            D[i][j] = 0

for k in range(len(D)):
    for i in range(len(D)):
        for j in range(len(D)):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[i][k] + D[k][j]
                S[i][j] = S[i][k]

print("\nShortest Paths:")
print("{0: <9}{1: <14}{2: <20}".format("Pair", "Path Weight", "Path"))
path = ""
for i in range(len(S)):
    for j in range(i, len(S)):
        if i != j:
            u = i
            if D[i][j] != INF:
                path = ("{0: <1} -> {1: <6}{2: <12}{3: <1}".format(G.nodes()[i]
                        , G.nodes()[j], round(D[i][j], 4), str(G.nodes()[i])))
                v = i
                while True:
                    u = S[u][j]
                    w = G.get_edge_data(G.nodes()[v], G.nodes()[u])['weight']
                    path += " -(" + str(w) + ")-> " + str(G.nodes()[u])
                    v = u
                    if u == j:
                        break
            else:
                path = ("{0: <1} -> {1: <6}{2: <12}{3: <1}".format(G.nodes()[u]
                        , G.nodes()[v], "Disconnected graph", "(No path)"))

            print(path)

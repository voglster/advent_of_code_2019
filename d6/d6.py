import networkx as nx

with open("input_p1") as f:
    data = f.read()

# data = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

data = data.splitlines()
data = [d.strip() for d in data]

g = nx.Graph()

for d in data:
    left, right = d.split(")")
    g.add_edge(right, left)

sink = "SAN"
source = "YOU"
# source_nodes = [node for node, indegree in g.in_degree(g.nodes()) if indegree == 0]
# print(source_nodes)
# from itertools import combinations


path_to_home = nx.shortest_path(g, source, sink)
print(path_to_home)


print(len(path_to_home) - 3)

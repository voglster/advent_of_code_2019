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
# K)L"""

data = data.splitlines()
data = [d.strip() for d in data]

g = nx.DiGraph()

for d in data:
    left, right = d.split(")")
    g.add_edge(right, left)

sink = "COM"
source_nodes = [node for node, indegree in g.in_degree(g.nodes()) if indegree == 0]
print(source_nodes)
from itertools import combinations

orbits = set()

for node in source_nodes:
    path_to_home = next(nx.all_simple_paths(g, node, "COM"))
    for c in combinations(path_to_home, 2):
        orbits.add(c)


print(len(orbits))

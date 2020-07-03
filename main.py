import random, time
from prettytable import PrettyTable
import networkx as nx
import prim, kruskal
import dijkstra, bf

graph_sizes = [(10, 15),
               (50, 75),
               (100, 150),
               (500, 750),
               (1000, 1500)]

result_table = {size: dict() for size in graph_sizes}

for size in result_table.keys():
  G = nx.gnm_random_graph(size[0], size[1])

  for n in G.nodes():
    for e in G[n]:
      G[n][e]['weight'] = 0
      
  for n in G.nodes():
    for e in G[n]:
      if G[n][e]['weight'] == 0:
        G[n][e]['weight'] = random.randint(1, 20)

  org_node = random.randint(0, max(G.nodes()))

  start_time = time.time_ns()
  k = kruskal.get_mst(G)
  result_table[size]['Kruskal'] = time.time_ns() - start_time

  start_time = time.time_ns()
  p = prim.get_mst(G, org_node)
  result_table[size]['Prim'] = time.time_ns() - start_time

  start_time = time.time_ns()
  d = dijkstra.get_table(G, org_node)
  result_table[size]['Dijkstra'] = time.time_ns() - start_time

  start_time = time.time_ns()
  b = bf.get_table(G, org_node)
  result_table[size]['Bellman-Ford'] = time.time_ns() - start_time


t = PrettyTable(["Tamanho", "Prim", "Kruskal", "Dijkstra", "Bellman-Ford"])
for size in result_table.keys():
  t.add_row([size, result_table[size]['Prim'], result_table[size]['Kruskal'], result_table[size]['Dijkstra'], result_table[size]['Bellman-Ford']])

print(t)
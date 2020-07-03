import networkx as nx
import sys

def get_mst(graph, start_node):
  visited_nodes = [start_node]
  used_edges = []

  while len(visited_nodes) != len(graph.nodes):
    lowest_cost = sys.maxsize
    for n in visited_nodes:
      for e in graph[n]:
        if graph[n][e]['weight'] < lowest_cost and e not in visited_nodes:
          used_n = n
          used_e = e
          lowest_cost = graph[n][e]['weight']
    used_edges.append((used_n, used_e))
    visited_nodes.append(used_e)
  
  return used_edges
import networkx as nx
import sys

def get_table(graph, org_node):
  distance = {node: sys.maxsize for node in graph.nodes()}
  distance[org_node] = 0

  
  for i in range(graph.number_of_nodes() - 1):
    for n in graph.nodes():
      for e in graph[n]:
        if (distance[n] != sys.maxsize and 
            distance[n] + graph[n][e]['weight'] < distance[e]):
          distance[e] = distance[n] + graph[n][e]['weight']

  for n in graph.nodes():
    for e in graph[n]:
      if (distance[n] != sys.maxsize and
          distance[n] + graph[n][e]['weight'] < distance[e]):
        return "Sem solução devido ciclos negativos"

  return distance
import networkx as nx
import sys

def get_path(graph, org_node, dst_node):
  nodes = []
  for n in graph.nodes():
    nodes.append(n)
  costs = {node: sys.maxsize for node in nodes}
  costs[org_node] = 0
  parent_node = {node: None for node in nodes}

  neighbours = {node: set() for node in nodes}
  for n in nodes:
    for e in graph[n]:
      neighbours[n].add((e, graph[n][e]['weight']))

  while nodes:
    current_node = min(nodes, key = lambda node: costs[node])
    nodes.remove(current_node)

    if costs[current_node] == sys.maxsize:
      break
    for nbr, cost in neighbours[current_node]:
      new_cost = costs[current_node] + cost

      if new_cost < costs[nbr]:
        costs[nbr] = new_cost
        parent_node[nbr] = current_node

  path = []
  final_cost = costs[dst_node]
  while parent_node[dst_node] is not None:
    path.append(dst_node)
    dst_node = parent_node[dst_node]
  if path:
    path.append(dst_node)
  path.reverse()
  return path, final_cost

def get_table(graph, org_node):
  table = []

  for dst in graph.nodes():
    path, cost = get_path(graph, org_node, dst)
    if cost > 0:
      table.append((dst, cost, path[-2:]))
    else:
      table.append((org_node, cost, []))

  return table
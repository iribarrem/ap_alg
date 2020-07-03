import networkx as nx

def get_mst(graph):
  edges = []
  mst = []
  for n in graph.nodes():
    makeSet(n)
    for e in graph[n]:
      if not (e, n, graph[e][n]['weight']) in edges:
        edges.append((n, e, graph[n][e]['weight']))
  edges.sort(key = lambda edges: edges[2])

  for e in edges:
    if find(e[0]) != find(e[1]):
      union(e[0], e[1])
      mst.append(e)

  return sorted(mst, key = lambda mst: mst[2])

parent = dict()
rank = dict()

def makeSet(node):
  parent[node] = node
  rank[node] = 0

def find(node):
  if parent[node] != node:
    parent[node] = find(parent[node])
  return parent[node]

def union(node_a, node_b):
  root_a = find(node_a)
  root_b = find(node_b)

  if root_a != root_b:
    if rank[root_a] > rank[root_b]:
      parent[root_b] = root_a
    else:
      parent[root_a] = root_b
    if rank[root_a] == rank[root_b]:
      rank[root_b] += 1
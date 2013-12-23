import sys

import parse


def printMatrix(matrix, n, m):
    print '\n'.join([' '.join([str(matrix[i][j]) for j in xrange(m)]) for i in xrange(n)])


def add_node(nodes, n):
    if not n in nodes:
        nodes[n] = [0, [n]]


def traverse(graph, nodes, n):
    if not n in graph:
        return
    node = nodes[n]
    edges = graph[n]
    for e in edges:
        edge_finish = e[0]
        edge_weight = e[1]
        finish = nodes[edge_finish]
        if node[0] + edge_weight > finish[0]:
            finish[0] = node[0] + edge_weight
            finish[1] = node[1] + [edge_finish]
            traverse(graph, nodes, edge_finish)


sys.setrecursionlimit(100000)

start = int(raw_input())
finish = int(raw_input())
graph = {}
nodes = {}
while True:
    edge = raw_input()
    if not edge:
        break
    r = parse.parse("{s:d}->{f:d}:{w:d}", edge)
    if r['s'] in graph:
        graph[r['s']].append((r['f'], r['w']))
    else:
        graph[r['s']] = [(r['f'], r['w'])]
    add_node(nodes, r['s'])
    add_node(nodes, r['f'])

traverse(graph, nodes, start)
finish_node = nodes[finish]
print finish_node[0]
print '->'.join([str(x) for x in finish_node[1]])

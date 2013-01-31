import util

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.outbound = []
        self.inbound = []

    def __cmp__(self, other):
        return round(self.value - other.value, 5)


class GraphEdge:
    def __init__(self, node1, node2, value):
        self.value = value
        self.startNode = node1
        self.endNode = node2
        self.startNode.outbound.append(self)
        self.endNode.inbound.append(self)


def key(w):
    return int(round(w, 5) * 100000)


def traverseForward(node, path):
    global graph, n, prefixes

    if len(path) == n:
        prefixes.add(path)
        return
    for e in node.outbound:
        traverseForward(e.endNode, path + e.value)


def traverseBackward(node, path):
    global graph, n, suffixes

    if len(path) == n:
        suffixes.add(path)
        return
    for e in node.inbound:
        traverseBackward(e.startNode, path + e.value)

L = []
while True:
    s = input()
    if not s: break
    L.append(float(s))

P = L[0]
L = L[1:]
n = (len(L) >> 1) - 1

graph = {key(x): GraphNode(x) for x in L}
starts = set(graph.keys())
ends = set(graph.keys())
for i in range(0, len(L)):
    w1 = L[i]
    for j in range(0, len(L)):
        w2 = L[j]

        if w2 > w1:
            s = util.getSymbol(w2 - w1)
            if not s is None:
                key1 = key(w1)
                key2 = key(w2)
                GraphEdge(graph[key1], graph[key2], s)
                if key2 in starts: starts.remove(key2)
                if key1 in ends: ends.remove(key1)

prefixes = set()
suffixes = set()

for node in starts:
    traverseForward(graph[node], '')
for node in ends:
    traverseBackward(graph[node], '')

print('\n'.join(prefixes.intersection(suffixes)))

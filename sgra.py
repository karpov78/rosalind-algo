from util import getSymbol

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []

    def __hash__(self):
        return int(self.value * 100)

    def __cmp__(self, other):
        return round(self.value - other.value, 5)


class GraphEdge:
    def __init__(self, node1, node2, value):
        self.value = value
        self.startNode = node1
        self.endNode = node2
        self.startNode.edges.append(self)


class SpecterGraph:
    def __init__(self):
        self.roots = set()
        self.nodes = {}

    def addNode(self, w):
        node = GraphNode(w)
        self.nodes[w] = node
        self.roots.add(node)

    def buildEdges(self):
        for node2 in self.nodes.values():
            for node1 in self.nodes.values():
                s = getSymbol(node2.value - node1.value)
                if s:
                    GraphEdge(node1, node2, s)
                    if node2 in self.roots: self.roots.remove(node2)

    def getLongestPath(self):
        longest_path = []
        paths = {n: [] for n in self.roots}
        while len(paths) > 0:
            for k, v in paths.items():
                node = k
                path = v
                break
            if not node:
                break

            for e in node.edges:
                end_path = paths.get(e.endNode, [])
                if len(path) + 1 > len(end_path):
                    end_path = path + [e.value]
                paths[e.endNode] = end_path
                if len(end_path) > len(longest_path):
                    longest_path = end_path
            del paths[node]
        return longest_path

if __name__ == '__main__':
    g = SpecterGraph()
    while True:
        d = input()
        if not d: break
        g.addNode(float(d))
    g.buildEdges()
    print(''.join(g.getLongestPath()))


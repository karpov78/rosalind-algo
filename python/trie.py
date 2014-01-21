nodeIdx = 1

class GraphNode:
    def __init__(self):
        global nodeIdx
        self.value = nodeIdx
        nodeIdx += 1
        self.edges = [None] * 5
        self.bitmap = {'A': 0, 'C': 1, 'G': 2, 'T': 3, '$': 4}

    def add(self, value):
        idx = bitmap[value]
        res = self.edges[idx]
        if res: return res
        res = GraphNode()
        self.edges[idx] = res
        return res


def populateTrie(root, s):
    node = root
    for c in s:
        node = node.add(c)


def traverse(root):
    for k, n in root.edges.items():
        print("%d %d %s" % (root.value, n.value, k))
        traverse(n)


if __name__ == '__main__':
    root = GraphNode()
    while True:
        s = raw_input()
        if not s: break
        populateTrie(root, s)
    traverse(root)

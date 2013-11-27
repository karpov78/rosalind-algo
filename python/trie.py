__author__ = 'ekarpov'

nodeIdx = 1


class GraphNode:
    def __init__(self):
        global nodeIdx
        self.value = nodeIdx
        nodeIdx += 1
        self.edges = {}

    def add(self, value):
        res = self.edges.get(value)
        if res: return res
        res = GraphNode()
        self.edges[value] = res
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
        s = input()
        if not s: break
        populateTrie(root, s)
    traverse(root)

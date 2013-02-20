from python.util import reverseComplement

class Node:
    def __init__(self, value):
        self.value = value
        self.path = None
        self.edges = set()

    def __add__(self, other):
        self.edges.add(other)
        return self

    def __str__(self):
        return self.value

    def __eq__(self, y):
        return self.value == y.value

    def __hash__(self):
        return hash(self.value)


def build_deBruijin_graph(un, k):
    global data_len
    result = {}
    for r in un:
        for i in range(0, data_len - k):
            start = r[i:i + k]
            startNode = result.get(start)
            if not startNode:
                startNode = Node(start)
                result[start] = startNode

            end = r[i + 1:i + k + 1]
            endNode = result.get(end)
            if not endNode:
                endNode = Node(end)
                result[end] = endNode
            startNode += endNode
            result[start] = startNode
            result[end] = endNode
    return result


def first(l):
    for x in l:
        return x
    return None


def traverseGraph(start_node, edges, visited, k):
    global data_len
    node = edges[start_node]
    node.path = [node]
    visited.add(start_node)

    queue = [node]

    minPath = None
    while len(queue) > 0:
        node = queue.pop()
        for e in node.edges:
            if not e.path:
                visited.add(e.value)
                e.path = node.path + [e]
                queue.append(e)
            elif len(e.path) < len(node.path) + 1:
                e.path = node.path + [e]
            if e.value == start_node and len(node.path) >= data_len - k + 1:
                if not minPath or len(minPath) > len(node.path):
                    minPath = node.path
    return minPath

if __name__ == '__main__':
    s = []
    while True:
        l = input()
        if not l: break
        s.append(l)
    un = set(s).union({reverseComplement(x) for x in s})
    data_len = len(s[0])

    k = data_len - 1
    while k >= 1:
        edges = build_deBruijin_graph(un, k)
        g_visited_nodes = set()
        start_node = first(edges.keys())

        path = None
        while True:
            visited_nodes = set()
            path = traverseGraph(start_node, edges, visited_nodes, k)
            if path:
                break
            g_visited_nodes |= visited_nodes

            start_node = first(edges.keys() - g_visited_nodes)
            if not start_node:
                k -= 1
                break

        if path:
            string = None
            for c in path:
                if not string:
                    string = c.value
                else:
                    string += c.value[-1]

            i = 0
            max = 0
            while i < (len(string) / 2):
                if string[:i] == string[-i:]:
                    max = i
                i += 1
            print(string[:-max])
            break

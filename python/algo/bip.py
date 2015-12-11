from util import test_data, read_ugraph_to_map


def dfs_color(_graph, _node, _colors, color = 1):
    _colors[_node - 1] = color

    other_color = 2 if color == 1 else 1
    for e in _graph[_node]:
        if _colors[e - 1] == 0:
            if not dfs_color(_graph, e, _colors, other_color):
                return False
        elif _colors[e - 1] != other_color:
            return False
    return True


def is_bip(_graph):
    _colors = [0] * len(_graph)

    for _node in _graph.keys():
        if _colors[_node - 1] == 0:
            if not dfs_color(_graph, _node, _colors):
                return False
    return True

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        res = []
        for i in xrange(n):
            f.readline()
            g = read_ugraph_to_map(f)
            res.append(is_bip(g))
    print ' '.join(['1' if x else '-1' for x in res])

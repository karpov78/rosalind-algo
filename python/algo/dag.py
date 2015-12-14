from util import test_data, read_dgraph_to_map


def traverse(_graph, _node, _visited, _path=None):
    if not _path:
        _path = [_node]
    if _node not in _graph:
        return True
    for _x in _graph[_node]:
        if _x in _visited:
            return _x not in _path
        else:
            _visited.add(_x)
            if not traverse(_graph, _x, _visited, _path + [_x]):
                return False
    return True

def is_dag(_graph):
    _visited = set()

    for _node in _graph.keys():
        if _node in _visited:
            continue
        elif not traverse(_graph, _node, _visited):
            return False
    return True


if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        res = []
        for i in xrange(n):
            f.readline()
            g = read_dgraph_to_map(f)
            res.append(is_dag(g))
    print ' '.join(['1' if x else '-1' for x in res])

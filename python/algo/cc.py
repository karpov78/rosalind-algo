from util import test_data

def find_cc(_nodes, _edges, _visited, _parent=None):
    if not _parent:
        for _node in _nodes:
            if _node not in _visited:
                _parent = _node
                break
        if not _parent:
            return None

    _visited.add(_parent)
    if _parent in _edges:
        for _next in _edges[_parent]:
            if _next not in _visited:
                _visited.add(_next)
                find_cc(_nodes, _edges, _visited, _next)
    return _visited

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        u,v = (int(x) for x in f.readline().split())
        edges = {}
        for i in xrange(v):
            start, end = (int(x) for x in f.readline().split())
            if start in edges:
                edges[start].append(end)
            else:
                edges[start] = [end]
            if end in edges:
                edges[end].append(start)
            else:
                edges[end] = [start]

    nodes = range(1, u + 1)
    res = 0
    visited = set()
    while True:
        cc = find_cc(nodes, edges, visited)
        if not cc:
            break
        res += 1
    print res
from hea import MinHeap
from util import test_data

def dijsktra(_u, _graph):
    _not_found = _u + 1

    _paths = [_not_found] * (_u + 1)
    _heap = MinHeap(_u, key=lambda _x: _not_found if not _x else _paths[_x])

    _paths[1] = 0
    for _node in xrange(1, u + 1):
        _heap += _node

    _visited = set()
    while len(_visited) < u:
        _node = _heap.extract_min()
        if _node in _graph:
            _value = _paths[_node]
            for _end, _weight in _graph[_node]:
                if _paths[_end] > _value + _weight:
                    _paths[_end] = _value + _weight
                    _heap.update(key=lambda _x: _x == _end)
        _visited.add(_node)

    for _node in xrange(1, _u + 1):
        if _paths[_node] >= _not_found:
            _paths[_node] = -1
    return _paths[1:]

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        u, v = (int(x) for x in f.readline().split())
        graph = {}
        while True:
            s = f.readline()
            if not s:
                break
            start, end, weight = (int(x) for x in s.split())
            if start not in graph:
                graph[start] = [(end, weight)]
            else:
                graph[start] += [(end, weight)]

    paths = dijsktra(u, graph)
    print ' '.join([str(x) for x in paths])
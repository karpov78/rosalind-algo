import os.path


def test_data(module):
    name = os.path.splitext(os.path.basename(module))[0]
    return '/Users/evgeny/Downloads/rosalind_%s.txt' % name


def swap(arr, i, j):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t


def read_ugraph_to_list(_file):
    u, v = (int(x) for x in _file.readline().split())
    g = []
    for _i in xrange(v):
        g.append((int(x) for x in _file.readline().split()))
    return u, g


def read_ugraph_to_map(_file):
    _nodes, _edges = (int(x) for x in _file.readline().split())
    _map = dict()
    for _n in xrange(_nodes):
        _map[_n + 1] = []
    for _i in xrange(_edges):
        _start, _end = (int(x) for x in _file.readline().split())
        _map[_start].append(_end)
        _map[_end].append(_start)
    return _map


def read_dgraph_to_map(_file):
    _nodes, _edges = (int(x) for x in _file.readline().split())
    _map = dict()
    for _n in xrange(_nodes):
        _map[_n + 1] = []
    for _i in xrange(_edges):
        _start, _end = (int(x) for x in _file.readline().split())
        _map[_start].append(_end)
    return _map


def read_weighted_dgraph_to_map(_file):
    _nodes, _edges = (int(x) for x in _file.readline().split())
    _map = dict()
    for _n in xrange(_nodes):
        _map[_n + 1] = []
    for _i in xrange(_edges):
        _start, _end, _weight = (int(x) for x in _file.readline().split())
        _map[_start].append((_end, _weight))
    return _map

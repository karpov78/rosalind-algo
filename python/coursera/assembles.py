import random


class AdjacencyMatrix:
    def __init__(self, nodes, noEdge=0):
        self.len = len(nodes)
        self.nodes = list(nodes)
        self.node_index = {}
        self.noEdge = noEdge
        for i in xrange(self.len):
            self.node_index[self.nodes[i]] = i
        self.edges = np.empty((self.len, self.len), dtype=int)
        self.edges.fill(self.noEdge)

    def __setitem__(self, key, value):
        if not type(key) is tuple:
            raise Exception('Invalid matrix key')
        elif type(key[0]) is int:
            self.edges[key[0], key[1]] = value
        elif type(key[0]) is str:
            s = self.node_index[key[0]]
            e = self.node_index[key[1]]
            self.edges[s, e] = value

    def __getitem__(self, item):
        if not type(item) is tuple:
            raise Exception('Invalid matrix key')
        elif type(item[0]) is int:
            return self.edges[item[0] * self.len + item[1]]
        elif type(item[0]) is str:
            s = self.node_index[item[0]]
            e = self.node_index[item[1]]
            return self.edges[s * self.len + e]

    def __contains__(self, item):
        if type(item) is str:
            return item in self.node_index
        elif type(item) is int:
            return 0 <= item < self.len
        else:
            raise Exception('Invalid matrix key')

    def assertEquals(self, other):
        assert self.len == other.len
        for i in xrange(self.len * self.len):
            assert other.edges[i] == self.edges[i], 'Invalid entry: expected %s, but was %s' % (
                other.edgeString(i), self.edgeString(i))

    def edgeString(self, index):
        i = index / self.len
        j = index % self.len
        return '%s %s %s' % (self.nodes[i], '->' if self.edges[index] else '  ', self.nodes[j])

    def nodeString(self, i):
        index = i * self.len
        targetNodes = ','.join([self.nodes[j] for j in xrange(self.len) if self.edges[index + j] != self.noEdge])
        if targetNodes:
            return '%s %s %s' % (self.nodes[i], '->', targetNodes)
        else:
            return ''

    def gluedStart(self):
        return [self.nodeString(i) for i in xrange(self.len) if self.nodeString(i)]

    def __str__(self):
        return '\n'.join([self.edgeString(i) for i in xrange(self.len * self.len) if self.edges[i] != self.noEdge])


class AdjacencyList:
    def __init__(self):
        self.nodes = {}

    def __setitem__(self, key, value):
        if type(key) is str:
            if key in self.nodes:
                self.nodes[key].append(value)
            else:
                self.nodes[key] = [value]
            if not value in self.nodes:
                self.nodes[value] = []
        else:
            raise Exception("Invalid argument")

    def __getitem__(self, item):
        if type(item) is str:
            return self.nodes[item]
        else:
            raise Exception("Invalid argument")

    def __delitem__(self, item):
        if type(item) is tuple:
            if len(item) != 2 or type(item[0]) is not str:
                raise Exception("Invalid argument")
            k = item[0]
            x = item[1]
            end_nodes = self.nodes[k]
            end_nodes.remove(x)
            if len(end_nodes) == 0:
                del self.nodes[k]
        else:
            raise Exception("Invalid argument")

    def __contains__(self, item):
        if type(item) is str:
            return item in self.nodes
        else:
            raise Exception('Invalid matrix key')

    def assertEquals(self, other):
        assert self.len == other.len
        for s in self.nodes:
            assert other.nodes[s] == self.nodes[s], 'Invalid entry: expected %s, but was %s' % (
                other.nodeString(i), self.nodesString(i))

    def nodeString(self, node):
        targetNodes = ','.join(self.nodes[node])
        if targetNodes:
            return '%s %s %s' % (node, '->', targetNodes)
        else:
            return ''

    def str_edges(self):
        return [self.nodeString(n) for n, v in self.nodes.items() if len(v) > 0]

    def edges(self):
        res = []
        for n, v in self.nodes.items():
            if len(v) == 0:
                continue
            for x in v:
                res.append((n, x))
        return res

    def reverse(self):
        res = AdjacencyList()
        for s, a in self.nodes.items():
            for f in a:
                res[f] = s
        return res

    def __str__(self):
        return '\n'.join([self.nodeString(n) for n, v in self.nodes.items() if len(v) > 0])


def overlap(patterns, k=1):
    len_p = len(patterns)
    res = AdjacencyMatrix(patterns)
    for i in xrange(len_p):
        for j in xrange(len_p):
            if i == j:
                continue
            if patterns[i][k:] == patterns[j][:-k]:
                res[i, j] = 1
    return res


def composition(text, k):
    res = [text[i: i + k] for i in xrange(len(text) - k + 1)]
    res.sort()
    return res


def de_bruijn_from_text(text, k):
    return DeBruijn(composition(text, k))


def de_bruijn_from_kmers(kmers):
    res = AdjacencyList()
    for s in kmers:
        res[s[:-1]] = s[1:]
    return res


def form_cycle(graph, node, prev_cycle=None):
    if not prev_cycle:
        prev_cycle = []
    edges = set() if not prev_cycle else set(prev_cycle)
    edge = (node, next_node(graph, node, edges))
    path = prev_cycle + [edge]
    while True:
        edges.add(edge)
        node = edge[1]
        if node in graph:
            end = next_node(graph, node, edges)
            if end:
                edge = (node, end)
                path.append(edge)
                continue
        return path


def next_node(graph, node, cycle):
    ends = random.sample(graph[node], len(graph[node]))
    for end in ends:
        edge = (node, end)
        if not edge in cycle:
            return end
    return None


def find_eulerian_cycle(graph):
    edges = set()
    for n, e in graph.items():
        for x in e:
            edges.add((n, x))
    cycle = form_cycle(graph, random.choice(graph.keys()))
    while edges - set(cycle):
        newStart = None
        for i in xrange(len(cycle)):
            n = cycle[i]
            for e in graph[n[0]]:
                if not (n[0], e) in cycle:
                    newStart = n[0]
                    cycle = cycle[i:] + cycle[:i]
                    break
            if newStart:
                break
        if not newStart:
            raise Exception("Invalid graph")
        cycle = form_cycle(graph, newStart, cycle)
    return cycle


def find_start_finish(graph):
    plusMinus = {}
    for a, e in graph.items():
        if a in plusMinus:
            plusMinus[a] -= len(e)
        else:
            plusMinus[a] = -len(e)
        for x in e:
            if x in plusMinus:
                plusMinus[x] += 1
            else:
                plusMinus[x] = 1
    start = None
    finish = None
    for n, pm in plusMinus.items():
        if pm == -1:
            start = n
        if pm == 1:
            finish = n
    return start, finish


def find_eulerian_path(graph):
    start, finish = find_start_finish(graph)
    if not start or not finish:
        raise Exception("Invalid graph")
    if finish in graph:
        graph[finish].append(start)
    else:
        graph[finish] = [start]
    path = find_eulerian_cycle(graph)
    for i in xrange(len(path)):
        if path[i][0] == start:
            path = path[i:] + path[:i]
            break
    return [x[0] for x in path]


def read_graph_from_console():
    graph = {}
    while True:
        s = raw_input().strip()
        if not s:
            break
        a, b = s.split(' -> ')
        e = b.split(',')
        graph[a] = e
    return graph


def read_graph_from_file(f):
    graph = {}
    while True:
        s = f.readline().strip()
        if s == 'Output':
            break
        a, b = s.split(' -> ')
        e = b.split(',')
        graph[a] = e
    return graph


def join_path(path):
    res = ''
    for s in path:
        if not res:
            res = s
        else:
            res += s[-1]
    return res


def permutations(k, alphabet):
    if k == 1:
        return alphabet
    else:
        perm = permutations(k - 1, alphabet)
        res = []
        for c in alphabet:
            res += [c + x for x in perm]
        return res


def BuildKGraph(k):
    p = permutations(k - 1, ['0', '1'])
    graph = {}
    for x in p:
        start = x[:-1]
        end = x[1:]
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    return graph


def de_bruijn(n, k):
    """
    De Bruijn sequence for alphabet size k
    and subsequences of length n.
    """
    a = [0] * k * n
    sequence = []

    def db(t, p):
        if t > n:
            if n % p == 0:
                for j in range(1, p + 1):
                    sequence.append(a[j])
        else:
            a[t] = a[t - p]
            db(t + 1, p)
            for j in range(a[t - p] + 1, k):
                a[t] = j
                db(t + 1, t)

    db(1, 1)
    return sequence


def de_bruijn_composition(k, d, text):
    res = []
    for i in xrange(len(text) - 2 * k - d + 1):
        s = text[i:i + k]
        e = text[i + k + d:i + 2 * k + d]
        res.append((s, e))
    res.sort(key=lambda x: x[0])
    return res


def prefix(x):
    return x[0][:-1], x[1][:-1]


def suffix(x):
    return x[0][1:], x[1][1:]


def get_next_node(graph, result, valid, start_with=None):
    last = result[-1]
    if not last in graph:
        return None
    next_nodes = graph[last]
    start = start_with is None
    for n in next_nodes:
        if not start:
            start = start_with == n
            continue
        if valid(result, n):
            return n
    return None


def find_eulerian_path_stack(graph, valid):
    start, finish = find_start_finish(graph)
    edges = sum([len(x) for x in graph.values()])
    result = [start]
    while result[-1] != finish and len(result) < edges + 1:
        # print ' -> '.join(['|'.join(e) for e in result])
        n = get_next_node(graph, result, valid)
        if n != None:
            result.append(n)
            continue
        while True:
            x = result.pop()
            assert len(result) > 0
            n = get_next_node(graph, result, valid, x)
            if n != None:
                result.append(n)
                break
    assert len(result) == edges + 1, "Inconsistent path"
    return result


def restore_string_from_path(path, k, d):
    s = path[0][0]
    for i in xrange(1, len(path)):
        s += path[i][0][-1]
    for i in xrange(len(path) - k - d, len(path)):
        s += path[i][1][-1]
    return s


if __name__ == '__main__':
    random.seed()
    patterns = []
    while True:
        s = raw_input()
        if not s:
            break
        patterns.append(s)

    # with open('/Users/evgeny/Downloads/contig_generation_3.txt', 'r') as f:
    #     f.readline()
    #     while True:
    #         s = f.readline().strip()
    #         if s == 'Output:':
    #             break
    #         patterns.append(s)
    #     expected = []
    #     while True:
    #         s = f.readline().strip()
    #         if not s:
    #             break
    #         expected.append(s)
    #     expected.sort()

    graph = de_bruijn_from_kmers(patterns)
    rev_graph = graph.reverse()
    res = []
    for n in graph.nodes.keys():
        if len(rev_graph[n]) == 1 and len(graph[n]) == 1:
            continue
        for x in graph[n]:
            contig = [n, x]
            while len(rev_graph[x]) == 1 and len(graph[x]) == 1:
                x = graph[x][0]
                contig.append(x)
            res.append(join_path(contig))
    print ' '.join(res)
    # res.sort()
    # assert len(expected) == len(res), "Expected %d, but was %d" % (len(expected), len(res))
    # for i in xrange(len(expected)):
    #     assert expected[i] == res[i], "Diff on %d-th position: expected %s, but was %s" % (expected[i], res[i])
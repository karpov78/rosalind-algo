from pygraph.classes.graph import graph
from pygraph.algorithms.cycles import find_cycle


def build_bp_graph(ps):
    graph = {}
    startVal = None
    prevVal = None
    val = 0
    for c in ps:
        if c == '(':
            startNode = True
        elif c == '-':
            sign = -1
        elif c == '+':
            sign = 1
        elif c >= '0' and c <= '9':
            val = val * 10 + int(c)
        elif c == ' ':
            val = sign * val
            if startNode:
                startVal = val
                prevVal = val
                startNode = False
            else:
                graph[prevVal] = -val
                prevVal = val
            val = 0
        elif c == ')':
            val = sign * val
            graph[prevVal] = -val
            graph[val] = -startVal
            prevVal = None
            startVal = None
            val = 0
    return graph


def blocks(p, q):
    if len(p) != len(q):
        raise Exception("Inconsistent graphs")
    return len(p)


def reverse_graph(g):
    res = {}
    for k, v in g.items():
        res[v] = k
    return res


def cycle(p, q):
    # gr = graph()
    # for n in p.keys():
    #     gr.add_node(n)
    #     gr.add_node(-n)
    # print gr.nodes()
    # print p.items()
    # print q.items()
    # for k,v in p.items():
    #     if not gr.has_edge((k, v)): gr.add_edge((k, v))
    # for k,v in q.items():
    #     if not gr.has_edge((k, v)): gr.add_edge((k, v))
    # print gr.edges()
    # res = 0
    # while True:
    #     c = find_cycle(gr)
    #     print c
    #     if len(c) > 0:
    #         for n in c:
    #             gr.del_node(n)
    #         res += 1
    #     else:
    #         break
    # return res
    rp = reverse_graph(p)
    rq = reverse_graph(q)

    res = 0
    visited = set()
    while len(visited) < len(p.keys()) * 2:
        # print visited
        for k in p.keys():
            if k not in visited:
                start = k
                break
        node = start
        visited.add(node)
        cycle = [node]
        while True:
            qn = q[node] if node in q else rq[node]
            cycle.append(qn)
            visited.add(qn)
            node = p[qn] if qn in p else rp[qn]
            if node == start:
                break
            cycle.append(node)
            visited.add(node)
            # print cycle
        res += 1
    return res

# with open('/Users/evgeny/Downloads/2_break.txt', 'r') as f:
#     f.readline() # skip "Input:"
#     ps = f.readline().strip()
#     qs = f.readline().strip()
#     f.readline() # skip "Output:"
#     res = int(f.readline().strip())
ps = raw_input()
p = build_bp_graph(ps)
qs = raw_input()
q = build_bp_graph(qs)
# res = 3
c = cycle(p, q)
b = blocks(p, q)
print b - c
# assert res == (b - c), "Expected %d, but was %d" % (res, b - c)
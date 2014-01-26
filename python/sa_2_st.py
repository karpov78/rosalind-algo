s = raw_input()
sa = [int(x) for x in raw_input().split(', ')]
lcp = [int(x) for x in raw_input().split(', ')]

# with open('/Users/evgeny/Downloads/sa2st.txt', 'r') as f:
#     f.readline()
#     s = f.readline().strip()
#     sa = [int(x) for x in f.readline().strip().split(', ')]
#     lcp = [int(x) for x in f.readline().strip().split(', ')]
#     f.readline()
#     exp = []
#     while True:
#         l = f.readline().strip()
#         if not l: break
#         exp.append(l)
#     exp.sort()


def handle_subtree(subtree, sub_lcp):
    global s

    if len(subtree) == 0:
        return []

    if len(sub_lcp) == 0:
        return [s[x:] for x in subtree]

    m = min(sub_lcp)
    res = []
    if m > 0:
        res.append(s[subtree[0]:subtree[0] + m])
    res += traverse_sa([x + m for x in subtree], [0] + [y - m for y in sub_lcp])
    return res


def traverse_sa(sa, lcp):
    subtree = []
    sub_lcp = []
    res = []

    for i in xrange(len(sa)):
        if lcp[i] == 0:
            ss = handle_subtree(subtree, sub_lcp)
            res += ss
            subtree = [sa[i]]
            sub_lcp = []
        else:
            subtree.append(sa[i])
            sub_lcp.append(lcp[i])
    res += handle_subtree(subtree, sub_lcp)
    return res


st_edges = traverse_sa(sa, lcp)

with open('/Users/evgeny/Downloads/result.txt', 'w') as f:
    f.write('\n'.join(st_edges))
# print '\n'.join(st_edges)
# st_edges.sort()
# assert exp == st_edges, "Expected %d edges, but were %d" % (len(exp), len(st_edges))

from suff_tree import SuffixTree


def traverse(tree, node=None):
    n = node if node else tree.root
    m = ''
    for e in n.edges:
        if e.end.edges and len(e.end.edges) > 1:
            trav = traverse(tree, e.end)
            if len(m) < e.length + len(trav):
                m = e.getValue(tree) + trav
    return m


s = raw_input()
st = SuffixTree(s + '$')
print traverse(st)
from suff_tree import SuffixTree


def find_nonshared(tree, s, offset, l):
    res = 0
    node = tree.root
    while True:
        hit = False
        for e in node.edges:
            if tree.s[e.offset] == s[offset + res]:
                for i in xrange(e.length):
                    if tree.s[e.offset + i] != s[offset + res]:
                        return res + 1
                    res += 1
                    if l - offset == res:
                        return None
                node = e.end
                hit = True
                break
        if not hit:
            return res + 1


s = raw_input()
t = raw_input()

tree = SuffixTree(t)

len_s = len(s)
res = (0, len_s)
for i in xrange(1, len_s):
    ns = find_nonshared(tree, s, i, len_s)
    if ns and ns < res[1]:
        res = (i, ns)

result = s[res[0]:res[0] + res[1]]
print result
print tree.contains(result)

print len(t)
print len(result)
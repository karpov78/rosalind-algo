from suff_tree import SuffixTree


def hasWindow(positions, L, t, k):
    if len(positions) < t:
        return False
    if positions[-1] - positions[0] + k <= L:
        return True
    return hasWindow(positions[1:], L, t, k) or hasWindow(positions[0:-1], L, t, k)


def locateClump(node, s, L, t, k, prefix=''):
    x_len_s = len(s)
    result = []
    for e in node.edges:
        sub = s[e.offset:e.offset + e.length]
        if len(sub) >= k:
            end_positions = sorted([x_len_s - p - len(prefix) - k for p in e.end.positions()])
            if len(end_positions) >= t:
                end_positions = sorted([x_len_s - p - len(prefix) - k for p in e.end.positions()])
                if hasWindow(end_positions, L, t, len(prefix) + k):
                    result.append(prefix + sub[0:k])

        else:
            result += locateClump(e.end, s, L, t, k - len(sub), prefix + sub)
    return result


if __name__ == '__main__':
    s = raw_input() + '$'

    k, L, t = (int(x) for x in raw_input().split(' '))
    len_s = len(s)

    tree = SuffixTree(s)
    res = locateClump(tree.root, s, L, t, k)
    print ' '.join(res)
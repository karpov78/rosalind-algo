import python.ctbl


def depthFirst(node):
    if len(node.edges) == 0:
        return 1 if node.value == 'AA' else 0,\
               1 if node.value == 'Aa' else 0,\
               1 if node.value == 'aa' else 0
    aa = depthFirst(node.edges[0])
    bb = depthFirst(node.edges[1])

    res_1 = aa[0] * bb[0] + (aa[0] * bb[1] + aa[1] * bb[0]) / 2 + aa[1] * bb[1] / 4
    res_3 = aa[2] * bb[2] + (aa[2] * bb[1] + aa[1] * bb[2]) / 2 + aa[1] * bb[1] / 4
    return res_1, 1 - (res_1 + res_3), res_3


if __name__ == '__main__':
    s = input()
    tree = python.ctbl.parseTree(s)
    a = depthFirst(tree.root)
    print(' '.join([str(round(x, 3)) for x in a]))
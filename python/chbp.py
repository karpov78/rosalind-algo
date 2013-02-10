import python.tree
import python.ctbl


def diff(v1, v2):
    res = 0
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            res += 1
    return res


def union(v1, v2):
    res = []
    n = 0
    half_v_len = len(v1) >> 1
    for c in v1:
        if c == '1':
            n += 1
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            res.append('1' if n < half_v_len else '0')
        else:
            res.append(v1[i])
    return res


def buildTreeByCharacter(nodes, table):
    table_bin = []

    # transpose matrix
    for i in range(len(nodes)):
        p = ''
        for r in table:
            p += r[i]
        table_bin.append((nodes[i], p))

    # sort rows
    table_bin.sort(key=lambda x: x[1])
    i = 0
    while i < len(table_bin) and len(table_bin) > 3:
        j = i + 1
        while j < len(table_bin) and len(table_bin) > 3:
            current = table_bin[i][1]
            c_tree = table_bin[i][0]
            c_isTree = type(c_tree) is python.tree.Tree

            next = table_bin[j][1]
            next_tree = table_bin[j][0]
            n_isTree = type(next_tree) is python.tree.Tree

            d = diff(current, next)

            if d == 0:
                tree = python.tree.Tree(None)
                tree.add(c_tree)
                tree.add(next_tree)
                table_bin[i] = (tree, next)
                del table_bin[j]
                i = 0
                break
            elif d == 1 and (c_isTree or n_isTree):
                tree = python.tree.Tree(None)
                tree.add(c_tree)
                tree.add(next_tree)
                table_bin[i] = (tree, union(next, current))
                del table_bin[j]
                i = 0
                break
            elif d == 2 and c_isTree and n_isTree:
                tree = python.tree.Tree(None)
                tree.add(c_tree)
                tree.add(next_tree)
                table_bin[i] = (tree, union(next, current))
                del table_bin[j]
                i = 0
                break
            j += 1
        i += 1

    newRoot = python.tree.Tree(None)
    newRoot.add(table_bin[0][0])
    newRoot.add(table_bin[1][0])
    newRoot.add(table_bin[2][0])
    return newRoot


def rev(x):
    return ''.join(['1' if c == '0' else '0' for c in x])


if __name__ == '__main__':
    nodes = input().split()
    table = set()
    while True:
        s = input()
        if not s: break
        table.add(s)

    print("Nodes: %d, table size: %d" % (len(nodes), len(table)))

    resultTree = buildTreeByCharacter(nodes, table)
    newick = resultTree.toNewick()
    print(newick)
    print(resultTree.getSize())
    validateTree = python.ctbl.parseTree(newick)
    vCharTable = python.ctbl.createCharTable(validateTree)
    print("Char table size: %d" % len(vCharTable))
    for x in table:
        y = rev(x)
        if x in vCharTable:
            vCharTable.remove(x)
        elif y in vCharTable:
            vCharTable.remove(y)
    if len(vCharTable) > 0:
        print("Invalid result")
        print(vCharTable)

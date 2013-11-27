import python.tree


def diff(v1, v2):
    res = 0
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            res += 1
    return res


def neg(v):
    return ['0' if x == '1' else '1' for x in v]


def power(v):
    return sum([1 if x == '1' else 0 for x in v])


def sort_power(v):
    p = power(v)
    return min(p, len(v) - p)


def cleanupTable(table):
    i = 0
    while i < len(table[0][0]):
        v = table[0][0][i]
        allEqual = True
        for c in table:
            if c[0][i] != v:
                allEqual = False
                break
        if allEqual:
            for c in table:
                del c[0][i]
        else:
            i += 1


def findNodes(row):
    if len(row) < 3:
        raise Exception("Invalid row: %s" % row)
    x = y = -1
    for i in range(len(row)):
        if row[i] == '1':
            if x < 0:
                x = i
            else:
                y = i
    return x, y


def removeNode(nodes, table, i):
    del nodes[i]
    for c in table:
        del c[i]


def buildTreeByCharacter(nodes, table):
    c_nodes = list(nodes)
    c_table = list(table)

    c_table.sort(key=lambda x: sort_power(x))
    i = 0
    while len(c_table) > 0:
        if len(c_nodes) == 1:
            return python.tree.Tree(c_nodes[0])
        elif len(c_nodes) == 2:
            tree = python.tree.Tree(c_nodes[0])
            tree.add(c_nodes[1])
            return tree
        rPower = power(c_table[i])
        if rPower == 2:
            x, y = findNodes(c_table[i])
            newNode = python.tree.Tree(None)
            newNode.add(c_nodes[x])
            newNode.add(c_nodes[y])
            c_nodes[x] = newNode
            removeNode(c_nodes, c_table, y)
            del c_table[0]
        elif rPower == len(c_table[i]) - 2:
            x, y = findNodes(neg(c_table[i]))
            newNode = python.tree.Tree(None)
            newNode.add(c_nodes[x])
            newNode.add(c_nodes[y])
            c_nodes[x] = newNode
            removeNode(c_nodes, c_table, y)
            del c_table[0]
        else:
            raise Exception("invalid char table")
    if len(c_nodes) == 3:
        root = python.tree.Tree(None)
        root.add(c_nodes[0])
        root.add(c_nodes[1])
        root.add(c_nodes[2])
        return root
    elif len(c_nodes) == 1:
        return c_nodes[0]
    elif len(c_nodes) == 2:
        root = c_nodes[0]
        root.add(c_nodes[1])
        return root


def _validate(tree):
    valid = False
    if len(tree.children) == 3 and tree.parent is None:
        valid = True
    elif len(tree.children) == 2 and not tree.parent is None:
        valid = True
    elif len(tree.children) == 0 and not tree.parent is None:
        valid = True
    if not valid:
        raise Exception("invalid tree: %s" % tree.toNewick())
    for c in tree.children:
        _validate(c)


if __name__ == '__main__':
    nodes = input().split()
    table = []
    while True:
        s = input()
        if not s: break
        table.append([x for x in s])

    resultTree = buildTreeByCharacter(nodes, table)
    newick = resultTree.toNewick()
    print(newick)
    _validate(resultTree)

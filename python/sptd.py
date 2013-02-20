import python.ctbl

if __name__ == '__main__':
    nodes = input().split()
    t1 = input()
    t2 = input()

    tree1 = python.ctbl.parseTree(t1)
    ctbl1 = python.ctbl.createCharTable(tree1)

    tree2 = python.ctbl.parseTree(t2)
    ctbl2 = python.ctbl.createCharTable(tree2)

    common = len(ctbl1.intersection(ctbl2))
    print(2 * (len(nodes) - 3) - 2 * common)
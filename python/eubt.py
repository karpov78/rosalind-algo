import sys

from python.tree import Tree


def buildAllTrees(baseTree, nodes):
    if len(nodes) == 0:
        print(baseTree.toNewick())
        return

    node = nodes[0]
    stack = [baseTree]
    while len(stack) > 0:
        r = stack.pop()
        for i in range(len(r.children)):
            c = r.children[i]

            t1 = Tree(None) # new internal node
            t1.add(node)
            t1.add(c)
            r.replaceChild(i, t1)
            buildAllTrees(baseTree, nodes[1:])
            r.replaceChild(i, c)
            stack.append(c)


if __name__ == '__main__':
    nodes = input().split()
    baseTree = Tree(nodes[0])
    if len(nodes) == 1:
        print(baseTree.toNewick())
        sys.exit()

    baseTree.add(nodes[1])
    if len(nodes) == 2:
        print(baseTree.toNewick())
        sys.exit()

    buildAllTrees(baseTree, nodes[2:])

from sys import argv

from python.tree import Tree


END_MARKER = '$'

__author__ = 'ekarpov'


class Data:
    def __init__(self, name, location, length):
        self.name = name
        self.location = location
        self.length = length

    def __str__(self):
        global s
        substr = s[self.location - 1: self.location + self.length - 1]
        return substr if len(substr) == 0 or substr[-1] != END_MARKER else substr[:-1]


node_stack = []
occurrences = {}


def calcSuffix(node):
    global node_stack, occurrences, k

    while len(node_stack) > 0 and node_stack[-1] != node.getParent():
        node_stack.pop()
    node_stack.append(node)

    n_occ = len(node.getLeaves())
    if n_occ >= k:
        suffix = ''.join([str(x.data) for x in node_stack])
        occurrences[suffix] = n_occ


f = open(argv[1], 'r')


def readNext():
    return f.readline()

#def readNext():
#    return input()

s = readNext()
k = int(readNext())
tree = Tree(Data('node1', 0, 0), key=lambda x: x.name)

while True:
    l = readNext()
    if not l: break
    d = l.split(' ')
    tree[d[0]].add(Data(d[1], int(d[2]), int(d[3])))

f.close()

tree.traverse(calcSuffix)
#print(occurrences)
#print(sorted(occurrences.keys(), key=lambda x: -len(x)))
for x in sorted(occurrences.keys(), key=lambda x: -len(x)):
    if occurrences[x] >= k:
        print(x)
        break
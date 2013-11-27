from python.tree import Tree

__author__ = 'ekarpov'


def del_substr(str, i, j):
    return (str[:i] if i > 0 else '') + str[j + 1:]


def remove_pair_brackets(path):
    i = 0
    brackets = []
    while i < len(path):
        if path[i] == ')' and len(brackets) > 0:
            open_bracket = brackets.pop()
            path = del_substr(path, open_bracket, i)
            i = open_bracket
        elif path[i] == '(':
            brackets.append(i)
            i += 1
        else:
            i += 1
    return path


def clean_commas(path):
    idx = path.rfind(')')
    while idx >= 0:
        if path[idx] == ',':
            path = del_substr(path, idx, idx)
        idx -= 1

    idx = path.find('(')
    while 0 <= idx < len(path):
        if path[idx] == ',':
            path = del_substr(path, idx, idx)
        else:
            idx += 1

    idx = 0
    while idx < len(path) - 1:
        if path[idx] == path[idx + 1] == ',':
            path = del_substr(path, idx, idx)
        else:
            idx += 1
    return path


def distance(tree, nodes):
    path = None
    current_node = ''
    for c in tree:
        if c == ';': break
        if c == ',' or c == '(' or c == ')':
            if not path and current_node in nodes:
                path = c
            elif path and current_node in nodes:
                break
            elif path:
                path += c
            current_node = ''
        else:
            current_node += c

    path = remove_pair_brackets(path)
    path = clean_commas(path)
    d = 0
    for c in path:
        if c == ')': d += 1
        if c == ',': d += 2
        if c == '(': d += 1

    return d


def test_distance(nwck, nodes):
    tree = None
    rootStack = []
    current_node = '$'
    for c in reversed(nwck):
        if c == ';':
            continue
        if not c in (',', '(', ')'):
            current_node = c + current_node
        else:
            if c == ',':
                rootStack[-1].add(current_node)
            elif c == ')':
                if not tree:
                    tree = Tree(current_node)
                    rootStack.append(tree)
                else:
                    rootStack.append(rootStack[-1].add(current_node))
            elif c == '(':
                rootStack[-1].add(current_node)
                rootStack.pop()
            current_node = '$'

    n1 = None
    n2 = None
    for c in nodes:
        if n1 is None:
            n1 = tree.find(c + '$')
        else:
            n2 = tree.find(c + '$')

    p1 = n1.getPath()
    p2 = n2.getPath()

    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] == p2[i]:
            del p1[i]
            del p2[i]
        else:
            break
    d = distance(nwck, nodes)
    if len(p1) + len(p2) != d:
        print("ERROR: expected %d, but got %d" % (len(p1) + len(p2), d))
        print(' '.join([str(x.data) for x in p1]))
        print(' '.join([str(x.data) for x in p2]))
    return len(p1) + len(p2)


res = []

while True:
    tree = input()
    if not tree: break
    nodes = set(input().split(' '))
    #test_distance(tree, nodes)
    res.append(distance(tree, nodes))
    input() # read empty line
print(' '.join([str(x) for x in res]))
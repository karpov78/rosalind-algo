b = False


class Edge:
    def __init__(self, e, val):
        self.val = val
        self.end = e
        self.a = True
        self.b = False

    def split(self, position):
        if position < len(s):
            other_val = self.val[position:]
            self.val = self.val[:position]
            result = self.end.addMoveChildren(other_val)
            return result
        else:
            return self

    def printEdge(self, tree, indent=''):
        res = indent + self.val
        for c in self.end.edges:
            res += '\n' + c.printEdge(tree, '')#'\t' + indent#)
        return res

    def getValue(self, tree):
        return self.val

    def __str__(self):
        return self.val


class Node:
    def __init__(self):
        self.edges = []

    def add(self, s):
        for e in self.edges:
            if e.val[0] == s[0]:
                return e
        self.edges.append(Edge(Node(), s))
        return self.edges[-1]

    def addMoveChildren(self, val):
        newNode = Node()
        newNode.edges = self.edges
        self.edges = [Edge(newNode, val)]
        return self.edges[-1]

    def __str__(self):
        return ' '.join([str(x) for x in self.edges])


class SuffixTree:
    def __init__(self, s=None):
        self.root = Node()
        l = len(s)
        for k in xrange(1, l):
            self.append(s[-k:])
        self.append(s)

    def append(self, s, root=None):
        if not root: root = self.root
        for e in root.edges:
            if e.val[0] == s[0]:
                r = self.followEdge(e, s)
                if r:
                    self.append(s[len(e.val):], r)
                return
        root.add(s)

    def followEdge(self, e, s):
        global b
        if b: e.b = True

        for i in xrange(len(e.val)):
            if e.val[i] != s[i]:
                e.split(i)
                e.end.add(s[i:])
                return None
        return e.end

    def __str__(self):
        return '\n'.join([x.printEdge(self) for x in self.root.edges])


def traverse(tree, node):
    l = ''
    for e in node.edges:
        if e.a and e.b:
            el = e.getValue(tree) + traverse(tree, e.end)
            if len(l) < len(el):
                l = el
    return l


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    st = SuffixTree(s + '$')
    t += '$'
    b = True
    l = len(t)
    for k in xrange(1, l):
        st.append(t[-k:])
    st.append(t)
    print traverse(st, st.root)
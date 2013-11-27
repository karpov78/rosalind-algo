class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __hash__(self):
        return hash(self.a) + hash(self.b)

    def __eq__(self, y):
        return self.a == y.a and self.b == y.b or self.b == y.a and self.a == y.b


    def __str__(self):
        return '{' + self.a + ', ' + self.b + '}'


class ResPair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __hash__(self):
        return hash(self.a) + hash(self.b)

    def __eq__(self, y):
        return self.a == y.a and self.b == y.b or self.b == y.a and self.a == y.b


    def __str__(self):
        return str(self.a) + ' ' + str(self.b)


def perm(list):
    result = set()
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            result.add(Pair(list[i], list[j]))
    return result


def pairs(list, list1):
    result = set()
    for a in list:
        for b in list1:
            result.add(ResPair(a, b))
    return result


def extractQuartets(nodes, charTable):
    result = set()
    for r in charTable:
        ones = []
        zeroes = []
        for i in range(len(r)):
            if r[i] == '1':
                ones.append(nodes[i])
            elif r[i] == '0':
                zeroes.append(nodes[i])
        if len(ones) > 1 and len(zeroes) > 1:
            #print("%s - ones: %s, zeroes: %s" % (r, str(perm(ones)), str(perm(zeroes))))
            result = result.union(pairs(perm(ones), perm(zeroes)))
    return result


if __name__ == '__main__':
    nodes = input().split()
    charTable = []
    while True:
        s = input()
        if not s: break
        charTable.append(s)

    print('\n'.join([str(x) for x in extractQuartets(nodes, charTable)]))

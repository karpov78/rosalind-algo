def isIncluded(a, b):
    return a[0] < b[0] < a[1] and a[0] < a[1] < a[1]


def addSubGraph(i, j, s, subgraphs):
    included = False
    for edge in subgraphs.keys():
        if isIncluded(edge, (i, j)):
            included = True
            break
    if not included:
        subgraphs[i, j] = numOfBondingGraphs(s[i + 1: j])

pairs = {
    'A': {'U'},
    'G': {'C', 'U'},
    'C': {'G'},
    'U': {'A', 'G'}
}

cache = {}

def numOfBondingGraphs(s):
    if len(s) < 4:
        return 1

    if s in cache: return cache[s]

    permutations = 1
    for i in range(len(s) - 4):
        for j in range(len(s) - 1, i + 3, -1):
            if s[j] in pairs[s[i]]:
                includingLeft = numOfBondingGraphs(s[i: j]) # permutations including left border
                includingRight = numOfBondingGraphs(s[i + 1: j + 1]) # permutations including right border
                permutations += (includingLeft + includingRight - 1) * numOfBondingGraphs(s[j:])
    cache[s] = permutations
    return permutations

if __name__ == '__main__':
    s = input()
    print(numOfBondingGraphs(s))
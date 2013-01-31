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
    len_s = len(s)
    if len_s <= 4:
        return 1

    if (s) in cache: return cache[s]

    permutations = 1 # count empty permutation right away

    for i in range(len_s):
        for j in range(len_s - 1, i + 3, -1):
            if s[j] in pairs[s[i]]:
                internal_permutations = numOfBondingGraphs(s[i + 1: j])
                external_permutations = numOfBondingGraphs(s[j + 1:])

                permutations += internal_permutations * external_permutations

            #    result = (2 if countOuter and s[-1] in pairs[s[0]] else 1) * permutations
    cache[s] = permutations
    #    print("%s (%s) - %d" % (s, str(countOuter), permutations))
    return permutations

if __name__ == '__main__':
    s = input()
    print(numOfBondingGraphs(s))
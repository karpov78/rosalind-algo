import sys


def printMatrix(matrix, n, m):
    print '\n'.join([' '.join([str(matrix[i][j]) for j in xrange(m)]) for i in xrange(n)])


def lcs(s1, s2):
    s = [[0] * len(s2) for i in xrange(len(s1))]
    backtrack = [[None] * len(s2) for i in xrange(len(s1))]
    for i in xrange(1, len(s1)):
        for j in xrange(1, len(s2)):
            s[i][j] = max(s[i - 1][j],
                          s[i][j - 1],
                          s[i - 1][j - 1] + 1 if s1[i] == s2[j] else -1)
            backtrack[i][j] = 'D' if s[i][j] == s[i - 1][j] else 'L' if s[i][j] == s[i][j - 1] else 'T'
    return backtrack


def output_backtrack(backtrack, s1, i, j):
    if i == 0 or j == 0:
        return []
    if backtrack[i][j] == 'D':
        return output_backtrack(backtrack, s1, i - 1, j)
    elif backtrack[i][j] == 'L':
        return output_backtrack(backtrack, s1, i, j - 1)
    else:
        return output_backtrack(backtrack, s1, i - 1, j - 1) + [s1[i]]


sys.setrecursionlimit(100000)

s1 = raw_input()
s2 = raw_input()
backtrack = lcs(s1, s2)
#printMatrix(backtrack, len(s1), len(s2))
res = output_backtrack(backtrack, s1, len(s1) - 1, len(s2) - 1)
print ''.join(res)
import sys


def printMatrix(matrix, n, m):
    print '\n'.join([' '.join([str(matrix[i][j]) for j in xrange(m + 1)]) for i in xrange(n + 1)])


down = []
right = []

sys.setrecursionlimit(10000)
n = int(raw_input())
m = int(raw_input())

for i in xrange(n):
    down.append([int(x) for x in raw_input().split(' ')])
raw_input()
for j in xrange(n + 1):
    right.append([int(x) for x in raw_input().split(' ')])

scoreMatrix = [list([0] * (m + 1)) for i in xrange(n + 1)]
for i in xrange(n):
    scoreMatrix[i + 1][0] = down[i][0]
for i in xrange(m):
    scoreMatrix[0][i + 1] = right[0][i]
for i in xrange(1, n + 1):
    for j in xrange(1, m + 1):
        left_edge = right[i][j - 1]
        top_edge = down[i - 1][j]
        scoreMatrix[i][j] = max(scoreMatrix[i][j - 1] + left_edge, scoreMatrix[i - 1][j] + top_edge)
#printMatrix(scoreMatrix, n, m)
print scoreMatrix[n][m]
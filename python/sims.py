import sys

from python.lev_matrix import LevMatrix, GAP_SYMBOL


def weight(a, b):
    return 1 if a == b else -1


class FittingAlignmentMatrix(LevMatrix):
    def __init__(self, s, t):
        self.maxValue = None

        super().__init__(s, t, weight=weight, format="%-3d")

    def calculatePathFromTop(self, top, x, y):
        return self.cellFactory(x, y, (top - 1) if y >= 0 else 0)

    def calculatePathFromLeft(self, left, x, y):
        return self.cellFactory(x, y, left - 1)

    def buildCell(self, diag, top, left, x, y):
        if top is None and left is None:
            return self.cellFactory(x, y, 0)
        elif top is None:
            return self.calculatePathFromLeft(left, x, y)
        elif left is None:
            return self.calculatePathFromTop(top, x, y)
        else:
            pathFromTop = self.calculatePathFromTop(top, x, y)
            pathFromLeft = self.calculatePathFromLeft(left, x, y)
            diag = self.cellFactory(x, y, diag + self.weight(self.s[x], self.t[y]))
            return max(pathFromLeft, pathFromTop, diag)

    def createCell(self, x, y, weight, prevCell=None):
        if y == len(t) - 1 and (not self.maxValue or self.maxValue < weight):
            self.maxValue = weight
        return weight


def printAlignment(m, cell):
    s_prefix = ''
    t_prefix = ''
    while cell[1] >= 0:
        cellValue = m.matrix[cell[0] + 1, cell[1] + 1]
        diag = m.matrix[cell]
        top = m.matrix[cell[0], cell[1] + 1]
        left = m.matrix[cell[0] + 1, cell[1]]
        if diag + weight(s[cell[0]], t[cell[1]]) == cellValue:
            s_prefix = s[cell[0]] + s_prefix
            t_prefix = t[cell[1]] + t_prefix
            cell = (cell[0] - 1, cell[1] - 1)
        elif top - 1 == cellValue:
            s_prefix = s[cell[0]] + s_prefix
            t_prefix = GAP_SYMBOL + t_prefix
            cell = (cell[0] - 1, cell[1])
        elif left - 1 == cellValue:
            s_prefix = GAP_SYMBOL + s_prefix
            t_prefix = t[cell[1]] + t_prefix
            cell = (cell[0], cell[1] - 1)
        else:
            sys.exit(1)
            #raise Exception("Something wrong is happening")
    print(s_prefix)
    print(t_prefix)

    res = 0
    for i in range(len(s_prefix)):
        res += 1 if s_prefix[i] == t_prefix[i] else -1
    print(res)

if __name__ == '__main__':
    s = input()
    t = input()
    m = FittingAlignmentMatrix(s, t)
    #print(m)
    print(m.maxValue)

    y = len(t) - 1
    for x in range(-1, len(s)):
        cell = (x, y)
        w = m.matrix[x + 1, y + 1]
        if w == m.maxValue:
            printAlignment(m, cell)
            break

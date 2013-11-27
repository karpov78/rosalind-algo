import sys

from python.lev_matrix import LevMatrix


class AlignmentMatrix(LevMatrix):
    def __init__(self, s, t):
        super().__init__(s, t, format="%-3d", type='h')

    def calculatePathFromTop(self, top, x, y):
        return self.cellFactory((top + 1) if y >= 0 else 0)

    def calculatePathFromLeft(self, left, x, y):
        return self.cellFactory(left + 1)

    def buildCell(self, diag, top, left, x, y):
        if top is None and left is None:
            return self.cellFactory(0)
        elif top is None:
            return self.calculatePathFromLeft(left, x, y)
        elif left is None:
            return self.calculatePathFromTop(top, x, y)
        else:
            pathFromTop = self.calculatePathFromTop(top, x, y)
            pathFromLeft = self.calculatePathFromLeft(left, x, y)
            diag = self.cellFactory(diag + self.weight(self.s[x], self.t[y]))
            return min(pathFromLeft, pathFromTop, diag)


def findStart(m, cell):
    length = 0
    while cell[1] >= 0 and cell[0] >= 0:
        cellValue = m.matrix[cell[0] + 1, cell[1] + 1]
        diag = m.matrix[cell]
        top = m.matrix[cell[0], cell[1] + 1]
        left = m.matrix[cell[0] + 1, cell[1]]
        if diag + m.weight(m.s[cell[0]], m.t[cell[1]]) == cellValue:
            cell = (cell[0] - 1, cell[1] - 1)
            length += 1
        elif top + 1 == cellValue:
            cell = (cell[0] - 1, cell[1])
            length += 1
        elif left + 1 == cellValue:
            cell = (cell[0], cell[1] - 1)
        else:
            raise Exception("Something wrong is happening")
    return cell[0] + 2, length


if __name__ == '__main__':
    k = int(input())
    s = input()
    t = input()
    m = AlignmentMatrix(t, s)
    #print(m)

    y = len(s) - 1
    for x in range(-1, len(t)):
        cell = (x, y)
        w = m.matrix[x + 1, y + 1]
        if w <= k:
            print("%d %d" % findStart(m, cell))

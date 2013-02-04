from python.lev_matrix import *
from python.timer import Timer


class MaxGapMatrixCell(LevMatrixCell):
    def __init__(self, x, y, weight, s, t, prevCell):
        super().__init__(x, y, weight, s, t, prevCell, True) # suppress prefixes calculation
        if prevCell:
            self.gaps = prevCell.gaps + (1 if prevCell.isOnTopOf(self) or prevCell.isLeftTo(self) else 0)
        else:
            self.gaps = 0


class MaxGapLevMatrix(LevMatrix):
    def __init__(self, s, t):
        super().__init__(s, t, cellFactory=self.createCell,
            weight=lambda x, y: -1 if x == GAP_SYMBOL or y == GAP_SYMBOL else 1 if x == y else -10000, cleanup=True)

    def buildCell(self, diag, top, left, x, y):
        if top is None and left is None:
            return self.cellFactory(x, y, 0)
        elif top is None:
            return self.cellFactory(x, y, left.weight + self.weight(GAP_SYMBOL, None), left)
        elif left is None:
            return self.cellFactory(x, y, top.weight + self.weight(GAP_SYMBOL, None), top)
        else:
            topWeight = top.weight + self.weight(GAP_SYMBOL, None)
            leftWeight = left.weight + self.weight(GAP_SYMBOL, None)
            diagWeight = diag.weight + self.weight(self.s[x], self.t[y])

            if diagWeight > leftWeight and diagWeight > topWeight:
                return self.cellFactory(x, y, diagWeight, diag)
            elif leftWeight == topWeight:
                if left.gaps > top.gaps:
                    return self.cellFactory(x, y, leftWeight, left)
                else:
                    return self.cellFactory(x, y, topWeight, top)
            elif leftWeight > topWeight:
                return self.cellFactory(x, y, leftWeight, left)
            else:
                return self.cellFactory(x, y, topWeight, top)

    def createCell(self, x, y, weight, prevCell=None):
        return MaxGapMatrixCell(x, y, weight, self.s, self.t, prevCell)


if __name__ == '__main__':
    s = input()
    t = input()
    with Timer() as perf:
        matrix = MaxGapLevMatrix(s, t)
        print(matrix.getLastCell().gaps)
    print(perf)

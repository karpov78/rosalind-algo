from python.lev_matrix import *
from python.timer import Timer

GAP_EXTENSION_PENALTY = 1
GAP_OPEN_PENALTY = 11 + GAP_EXTENSION_PENALTY

def leftGapOpen(left):
    return max(left.weight - GAP_OPEN_PENALTY, left.gap_weight_left - GAP_EXTENSION_PENALTY)


def topGapOpen(top):
    return max(top.weight - GAP_OPEN_PENALTY, top.gap_weight_top - GAP_EXTENSION_PENALTY)


def _validate(d, s, t):
    if len(s) != len(t):
        raise Exception("Inconsistent lengths")
    count = 0
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1] == GAP_SYMBOL:
            count -= 1
            continue
        if i > 0 and t[i] == t[i - 1] == GAP_SYMBOL:
            count -= 1
            continue
        count += getBlosumWeight(s[i], t[i], gap_weight=-12)
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


class LaffMatrixCell:
    def __init__(self, weight, left=None, top=None, prevCell=None):
        self.weight = weight
        self.gap_weight_top = -GAP_OPEN_PENALTY if not top else topGapOpen(top)
        self.gap_weight_left = -GAP_OPEN_PENALTY if not left else leftGapOpen(left)
        self.prev = prevCell

    def cellSize(self):
        return 14

    def __str__(self):
        return "%3d (%3d, %3d)" % (self.weight, self.gap_weight_top, self.gap_weight_left)


class LaffMatrix(LevMatrix):
    def __init__(self, s, t):
        self.maxWeight = 0
        self.maxCell = (0, 0)
        super().__init__(s, t, self.createCell, weight=lambda a, b: getBlosumWeight(a, b))

    def buildCell(self, diag, top, left, x, y):
        if top is None and left is None:
            return self.cellFactory(x, y, 0)
        elif top is None:
            return self.cellFactory(x, y, leftGapOpen(left), (x, y - 1))
        elif left is None:
            return self.cellFactory(x, y, topGapOpen(top), (x - 1, y))
        else:
            max_weight = diag.weight + self.weight(self.s[x], self.t[y])
            cell = (x - 1, y - 1)

            top_weight = topGapOpen(top)
            if top_weight > max_weight:
                max_weight = top_weight
                cell = (x - 1, y)

            left_weight = leftGapOpen(left)
            if left_weight > max_weight:
                max_weight = left_weight
                cell = (x, y - 1)

            return self.cellFactory(x, y, max_weight, cell)

    def createCell(self, x, y, weight, prevCell=None):
        leftCell = None if y < 0 else self.matrix[x + 1, y]
        topCell = None if x < 0 else self.matrix[x, y + 1]

        if weight < 0:
            weight = 0
            prevCell = None

        cell = LaffMatrixCell(weight, leftCell, topCell, prevCell)
        if self.maxWeight < weight:
            self.maxCell = (x, y)
            self.maxWeight = weight
        return cell

    def restorePath(self):
        if not self.maxCell: return '', ''

        x, y = self.maxCell
        se = ''
        st = ''

        cell = self.matrix[x + 1, y + 1]
        while cell and cell.weight > 0:
            se = self.s[x] + se
            st = self.t[y] + st
            x, y = cell.prev
            cell = self.matrix[x + 1, y + 1]
        return se, st

if __name__ == '__main__':
    s = input()
    t = input()
    with Timer() as perf:
        matrix = LaffMatrix(s, t)
        print(matrix)
        print(matrix.maxWeight)
        se, st = matrix.restorePath()
        print(se)
        print(st)
    print("Time: " + perf)

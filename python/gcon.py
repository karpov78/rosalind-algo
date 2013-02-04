from python.lev_matrix import *
from python.timer import Timer

def _validate(d, s, t):
    if len(s) != len(t):
        raise Exception("Inconsistent lengths")
    count = 0
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1] == GAP_SYMBOL:
            continue
        if i > 0 and t[i] == t[i - 1] == GAP_SYMBOL:
            continue
        count += getWeight(s[i], t[i])
        #print("%s -> %s = %d (%d)" % (s[i], t[i], getWeight(s[i], t[i]), count))
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


class GconMatrixCell(LevMatrixCell):
    def __init__(self, x, y, weight, s, t, leftCell=None, topCell=None, prevCell=None):
        super(GconMatrixCell, self).__init__(x, y, weight, s, t, prevCell)
        self.left = leftCell
        self.top = topCell
        if not prevCell or prevCell.x == self.x - 1 and prevCell.y == self.y - 1:
            self.gap = 0 # no gap
        elif prevCell.x == self.x:
            self.gap = 1 # top
        else:
            self.gap = 2 # left


class GconMatrix(LevMatrix):
    def __init__(self, s, t):
        super(GconMatrix, self).__init__(s, t, self.createCell, weight=lambda a, b: getWeight(a, b))

    def calculatePathFromLeft(self, left, x, y):
        if y <= 0:
            return self.cellFactory(x, y, left.weight + self.weight(GAP_SYMBOL, None), left)

        left_cell = left
        newWeight = left.weight if left.gap == 1 else left.weight + self.weight(GAP_SYMBOL, None)
        ll = left_cell.left
        while not ll is None:
            w = ll.weight if ll.gap == 1 else ll.weight + self.weight(GAP_SYMBOL, None)
            if w > newWeight:
                newWeight = w
                left_cell = ll
            if ll.gap == 1: break
            ll = ll.left
        return self.cellFactory(x, y, newWeight, left_cell)

    def calculatePathFromTop(self, top, x, y):
        if x <= 0:
            return self.cellFactory(x, y, top.weight + self.weight(GAP_SYMBOL, None), top)

        top_cell = top
        newWeight = top.weight if top.gap == 2 else top.weight + self.weight(GAP_SYMBOL, None)
        tt = top_cell.top
        while not tt is None:
            w = tt.weight if tt.gap == 2 else tt.weight + self.weight(GAP_SYMBOL, None)
            if w > newWeight:
                newWeight = w
                top_cell = tt
            if tt.gap == 2: break
            tt = tt.top

        return self.cellFactory(x, y, newWeight, top_cell)

    def createCell(self, x, y, weight, prevCell=None):
        leftCell = None if y < 0 else self.matrix[x + 1, y]
        topCell = None if x < 0 else self.matrix[x, y + 1]
        return GconMatrixCell(x, y, weight, self.s, self.t, leftCell, topCell, prevCell)

if __name__ == "__main__":
    s = input()
    t = input()

    with Timer() as perf:
        matrix = GconMatrix(s, t)
        target_d = matrix.getDistance()
        #print(matrix)
        print(target_d)
        edited_s, edited_t = matrix.getAlignedStrings()
        print(edited_s)
        print(edited_t)
        _validate(target_d, edited_s, edited_t)
    print(perf)

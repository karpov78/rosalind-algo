from python.lev_matrix import *

def _validate(d, s, t):
    if len(s) != len(t):
        raise Exception("Inconsistent lengths")
    count = 0
    for i in range(len(s)):
        if i > 0 and s[i] == s[i - 1] == GAP_SYMBOL:
            count -= 1
            #print("%s -> %s = %d (%d)" % (s[i], t[i], -1, count))
            continue
        if i > 0 and t[i] == t[i - 1] == GAP_SYMBOL:
            count -= 1
            #print("%s -> %s = %d (%d)" % (s[i], t[i], -1, count))
            continue
        count += getBlosumWeight(s[i], t[i], gap_weight=-12)
        #print("%s -> %s = %d (%d)" % (s[i], t[i], getBlosumWeight(s[i], t[i], gap_weight=-12), count))
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


class GaffMatrixCell(LevMatrixCell):
    def __init__(self, x, y, weight, s, t, leftCell=None, topCell=None, prevCell=None):
        super().__init__(x, y, weight, s, t, prevCell)
        self.left = leftCell
        self.top = topCell
        if not prevCell or prevCell.x == self.x - 1 and prevCell.y == self.y - 1:
            self.gap = 0 # no gap
            self.gap_len = 0
        elif prevCell.x == self.x:
            self.gap = 1 # left
        else:
            self.gap = 2 # top


class GaffMatrix(LevMatrix):
    def __init__(self, s, t, gapOpening=11, gapExtension=1):
        self.gapOpening = gapOpening
        self.gapExtension = gapExtension
        super().__init__(s, t, self.createCell,
            weight=lambda a, b: getBlosumWeight(a, b, gap_weight=-gapOpening - gapExtension))

    def calculatePathFromLeft(self, left, x, y):
        calcWeight = lambda left:\
        left.weight - self.gapOpening - self.gapExtension * (y - left.y) if left.gap != 1\
        else left.weight - self.gapExtension * (y - left.y)

        if y <= 0:
            return self.cellFactory(x, y, calcWeight(left), left)

        left_cell = left
        newWeight = calcWeight(left)
        if left.gap != 1:
            ll = left_cell.left
            while not ll is None:
                w = calcWeight(ll)
                if w > newWeight:
                    newWeight = w
                    left_cell = ll
                if ll.gap == 1: break
                ll = ll.left
        return self.cellFactory(x, y, newWeight, left_cell)

    def calculatePathFromTop(self, top, x, y):
        calcWeight = lambda top:\
        top.weight - self.gapOpening - self.gapExtension * (x - top.x) if top.gap != 2\
        else top.weight - self.gapExtension * (x - top.x)

        if x <= 0:
            return self.cellFactory(x, y, calcWeight(top), top)

        top_cell = top
        newWeight = calcWeight(top)
        if top.gap != 2:
            tt = top_cell.top
            while not tt is None:
                w = calcWeight(tt)
                if w > newWeight:
                    newWeight = w
                    top_cell = tt
                if tt.gap == 2: break
                tt = tt.top

        return self.cellFactory(x, y, newWeight, top_cell)

    def createCell(self, x, y, weight, prevCell=None):
        leftCell = None if y < 0 else self.matrix[x + 1, y]
        topCell = None if x < 0 else self.matrix[x, y + 1]
        return GaffMatrixCell(x, y, weight, self.s, self.t, leftCell, topCell, prevCell)

if __name__ == '__main__':
    s = input()
    t = input()
    matrix = GaffMatrix(s, t)
    #print(matrix)
    d = matrix.getDistance()
    print(d)
    se, te = matrix.getAlignedStrings()
    _validate(d, se, te)

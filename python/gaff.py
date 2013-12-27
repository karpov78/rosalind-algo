from Bio import pairwise2
from Bio.SubsMat import MatrixInfo as matlist

from python.lev_matrix import *


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
        count += getBlosumWeight(s[i], t[i], gap_weight=-11)
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


class GaffCell:
    def __init__(self, score, dir, gap):
        self.score = score
        self.dir = dir
        self.gap = gap

    def __str__(self):
        return '%d %s' % (self.score, self.dir)


class GaffMatrix:
    def __init__(self, s, t, cellFactory=None, weight=getBlosumWeight, format='%-5s', type='i'):
        self.s = s
        self.t = t
        self.weight = weight
        self.gap_opening = 11
        self.gap_extension = 1

        self.len_s = len(self.s)
        self.len_t = len(self.t)
        self.matrix = Matrix(rows=self.len_s + 1, cols=self.len_t + 1, format=format, type=type, default=0)
        self._calculate_matrix()

    def createCell(self, x, y, weight, dir=None):
        if dir == 'D':
            return GaffCell(weight, dir, 0)
        elif dir == 'T':
            top = self.matrix[x - 1, y]
            return GaffCell(weight, dir, top.gap + 1 if top.dir == 'T' else 1)
        else:
            left = self.matrix[x, y - 1]
            return GaffCell(weight, dir, left.gap + 1 if left.dir == 'L' else 1)

    def calculatePathFromTop(self, top, x, y):
        calcScore = lambda top, tx: \
            top.score - (self.gap_opening - self.gap_extension if top.dir != 'T' else 0) - (x - tx) * self.gap_extension
        score = calcScore(top, x - 1)

        tx = x - 2
        while tx >= 0:
            tt = self.matrix[tx, y]
            new_score = calcScore(tt, tx)
            if new_score > score:
                score = new_score
            if tt.dir == 'T':
                break
            tx -= 1
        return score

    def calculatePathFromLeft(self, left, x, y):
        calcScore = lambda left, ly: \
            left.score - (self.gap_opening - self.gap_extension if left.dir != 'L' else 0) - (
            y - ly) * self.gap_extension
        score = calcScore(left, y - 1)

        ly = y - 2
        while ly >= 0:
            ll = self.matrix[x, ly]
            new_score = calcScore(ll, ly)
            if new_score > score:
                score = new_score
            if ll.dir == 'L':
                break
            ly -= 1
        return score

    def buildCell(self, diag, top, left, x, y):
        if top is None and left is None:
            return self.createCell(x, y, 0, 'D')
        elif top is None:
            return self.createCell(x, y, self.calculatePathFromLeft(left, x, y), 'L')
        elif left is None:
            return self.createCell(x, y, self.calculatePathFromTop(top, x, y), 'T')
        else:
            pathFromTop = self.calculatePathFromTop(top, x, y)
            pathFromLeft = self.calculatePathFromLeft(left, x, y)
            pathDiag = diag.score + self.weight(self.s[x - 1], self.t[y - 1])
            newScore = max(pathFromLeft, pathFromTop, pathDiag)
            return self.createCell(x, y, newScore,
                                   'D' if newScore == pathDiag else
                                   'T' if newScore == pathFromTop else
                                   'L')

    def _calculate_matrix(self):
        len_s = len(self.s)
        len_t = len(self.t)

        for i in xrange(0, len_s + 1):
            for j in xrange(0, len_t + 1):
                diag = self.matrix[i - 1, j - 1] if i > 0 and j > 0 else None
                top = self.matrix[i - 1, j] if i > 0 else None
                left = self.matrix[i, j - 1] if j > 0 else None
                self.matrix[i, j] = self.buildCell(diag, top, left, i, j)

    def getLastCell(self):
        return self.matrix[-1]

    def getDistance(self):
        return self.matrix[self.len_s, self.len_t].score

    def __str__(self):
        return str(self.matrix)

    def getAlignedStrings(self, cell=None):
        if cell is None:
            cell = (self.len_s, self.len_t)
        s_prefix = ''
        t_prefix = ''
        while cell[0] > 0 or cell[1] > 0:
            cell_value = self.matrix[cell]

            s_char = s[cell[0] - 1]
            t_char = t[cell[1] - 1]
            if cell_value.dir == 'D':
                s_prefix = s_char + s_prefix
                t_prefix = t_char + t_prefix
                cell = (cell[0] - 1, cell[1] - 1)
            elif cell_value.dir == 'T':
                s_prefix = s_char + s_prefix
                t_prefix = GAP_SYMBOL + t_prefix

                curr_score = cell_value.score + 11
                cell = (cell[0] - 1, cell[1])
                while curr_score != self.matrix[cell].score:
                    s_char = s[cell[0] - 1]
                    s_prefix = s_char + s_prefix
                    t_prefix = GAP_SYMBOL + t_prefix
                    cell = (cell[0] - 1, cell[1])
                    curr_score += 1
            else:
                s_prefix = GAP_SYMBOL + s_prefix
                t_prefix = t_char + t_prefix

                curr_score = cell_value.score + 11
                cell = (cell[0], cell[1] - 1)
                while curr_score != self.matrix[cell].score:
                    t_char = t[cell[1] - 1]
                    s_prefix = GAP_SYMBOL + s_prefix
                    t_prefix = t_char + t_prefix
                    cell = (cell[0], cell[1] - 1)
                    curr_score += 1
        return s_prefix, t_prefix


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    matrix = GaffMatrix(s, t)
    #print(matrix)
    d = matrix.getDistance()
    print(d)
    se, te = matrix.getAlignedStrings()
    print se
    print te

    valid = False
    matrix = matlist.blosum62
    alns = pairwise2.align.globalds(s, t, matrix, -11, -1)
    for a in alns:
        if d == int(a[2]) and se == a[0] and te == a[1]:
            valid = True
    if not valid:
        print "Invalid!!!"
    _validate(d, se, te)

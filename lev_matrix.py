from matrix import Matrix, parseIntMatrix

GAP_WEIGHT = -5

GAP_SYMBOL = '-'

SYMBOLS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

BLOSUM62 = parseIntMatrix(
    '4 0 -2 -1 -2 0 -2 -1 -1 -1 -1 -2 -1 -1 -1 1 0 0 -3 -2',
    '0 9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2',
    '-2 -3 6 2 -3 -1 -1 -3 -1 -4 -3 1 -1 0 -2 0 -1 -3 -4 -3',
    '-1 -4 2 5 -3 -2 0 -3 1 -3 -2 0 -1 2 0 0 -1 -2 -3 -2',
    '-2 -2 -3 -3 6 -3 -1 0 -3 0 0 -3 -4 -3 -3 -2 -2 -1 1 3',
    '0 -3 -1 -2 -3 6 -2 -4 -2 -4 -3 0 -2 -2 -2 0 -2 -3 -2 -3',
    '-2 -3 -1 0 -1 -2 8 -3 -1 -3 -2 1 -2 0 0 -1 -2 -3 -2 2',
    '-1 -1 -3 -3 0 -4 -3 4 -3 2 1 -3 -3 -3 -3 -2 -1 3 -3 -1',
    '-1 -3 -1 1 -3 -2 -1 -3 5 -2 -1 0 -1 1 2 0 -1 -2 -3 -2',
    '-1 -1 -4 -3 0 -4 -3 2 -2 4 2 -3 -3 -2 -2 -2 -1 1 -2 -1',
    '-1 -1 -3 -2 0 -3 -2 1 -1 2 5 -2 -2 0 -1 -1 -1 1 -1 -1',
    '-2 -3 1 0 -3 0 1 -3 0 -3 -2 6 -2 0 0 1 0 -3 -4 -2',
    '-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2 7 -1 -2 -1 -1 -2 -4 -3',
    '-1 -3 0 2 -3 -2 0 -3 1 -2 0 0 -1 5 1 0 -1 -2 -2 -1',
    '-1 -3 -2 0 -3 -2 0 -3 2 -2 -1 0 -2 1 5 -1 -1 -3 -3 -2',
    '1 -1 0 0 -2 0 -1 -2 0 -2 -1 1 -1 0 -1 4 1 -2 -3 -2',
    '0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1 0 -1 -1 -1 1 5 0 -2 -2',
    '0 -1 -3 -2 -1 -3 -3 3 -2 1 1 -3 -2 -2 -3 -2 0 4 -3 -1',
    '-3 -2 -4 -3 1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11 2',
    '-2 -2 -3 -2 3 -3 2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1 2 7')

def getWeight(a, b, gap_weight=GAP_WEIGHT):
    if a == GAP_SYMBOL or b == GAP_SYMBOL:
        return gap_weight
    else:
        return BLOSUM62[SYMBOLS.index(a), SYMBOLS.index(b)]


class LevMatrixCell:
    def __init__(self, x, y, weight, s, t, prevCell=None):
        self.x = x
        self.y = y
        self.weight = weight

        try:
            if not prevCell:
                self.s_prefix = ''
                self.t_prefix = ''
            elif prevCell.isOnTopOf(self):
                self.s_prefix = prevCell.s_prefix + s[prevCell.x + 1:self.x + 1]
                self.t_prefix = prevCell.t_prefix + GAP_SYMBOL * (self.x - prevCell.x)
            elif prevCell.isLeftTo(self):
                self.s_prefix = prevCell.s_prefix + GAP_SYMBOL * (self.y - prevCell.y)
                self.t_prefix = prevCell.t_prefix + t[prevCell.y + 1:self.y + 1]
            else:
                self.s_prefix = prevCell.s_prefix + s[self.x]
                self.t_prefix = prevCell.t_prefix + t[self.y]
        finally:
            if len(self.s_prefix) != len(self.t_prefix):
                raise Exception("Inconsistent length")

    def isOnTopOf(self, otherCell):
        return self.y == otherCell.y and self.x < otherCell.x

    def isLeftTo(self, otherCell):
        return self.x == otherCell.x and self.y < otherCell.y

    def cellSize(self):
        return 20

    def __str__(self):
        return "%3d (%s, %s)" % (self.weight, self.s_prefix, self.t_prefix)


class LevMatrix:
    def __init__(self, s, t, cellFactory=None, weight=lambda a, b: 0 if a == b else 1):
        self.s = s
        self.t = t
        self.weight = weight
        self.cellFactory = cellFactory if cellFactory else self.createCell

        len_s = len(self.s)
        len_t = len(self.t)
        self.matrix = Matrix(rows=len_s + 1, cols=len_t + 1, format='%%-%ds' % self.createCell(-1, -1, 0).cellSize())
        self._calculateMatrix()

    def createCell(self, x, y, weight, prevCell=None):
        return LevMatrixCell(x, y, weight, self.s, self.t, prevCell)

    def calculatePathFromTop(self, top, x, y):
        return self.cellFactory(x, y, top.weight + self.weight(GAP_SYMBOL, None), top)

    def calculatePathFromLeft(self, left, x, y):
        return self.cellFactory(x, y, left.weight + self.weight(GAP_SYMBOL, None), left)

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
            diagWeight = diag.weight + self.weight(self.s[x], self.t[y])

            if pathFromTop.weight >= pathFromLeft.weight and pathFromTop.weight >= diagWeight:
                return pathFromTop
            elif pathFromLeft.weight >= pathFromTop.weight and pathFromLeft.weight >= diagWeight:
                return pathFromLeft
            else:
                return self.cellFactory(x, y, diagWeight, diag)

    def _calculateMatrix(self):
        len_s = len(self.s)
        len_t = len(self.t)

        current_index = 0
        left_index = current_index - 1
        top_index = -len_t - 1
        diag_index = top_index - 1

        for i in range(-1, len_s):
            for j in range(-1, len_t):
                diag = self.matrix[diag_index] if i >= 0 and j >= 0 else None
                top = self.matrix[top_index] if i >= 0 else None
                left = self.matrix[left_index] if j >= 0 else None
                self.matrix[current_index] = self.buildCell(diag, top, left, i, j)

                current_index += 1
                top_index += 1
                left_index += 1
                diag_index += 1

    def getDistance(self):
        return self.matrix[-1].weight

    def getAlignedStrings(self):
    #        path = self.matrix[-1].path + [self.matrix[-1]]
    #        prev_step = path[0]
    #        edited_s = ''
    #        edited_t = ''
    #        for step in path[1:]:
    #            if prev_step.x + 1 == step.x and prev_step.y + 1 == step.y:
    #                edited_s += self.s[step.x]
    #                edited_t += self.t[step.y]
    #            elif prev_step.x == step.x and prev_step.y + 1 == step.y:
    #                edited_s += '-'
    #                edited_t += self.t[step.y]
    #            elif prev_step.x + 1 == step.x and prev_step.y == step.y:
    #                edited_s += self.s[step.x]
    #                edited_t += '-'
    #            prev_step = step
    #        return edited_s, edited_t
        return self.matrix[-1].s_prefix, self.matrix[-1].t_prefix

    def __str__(self):
        return str(self.matrix)

from python.lev_matrix import LevMatrix, GAP_SYMBOL


def weight(a, b):
    if a == GAP_SYMBOL or b == GAP_SYMBOL:
        return -1
    return 1 if a == b else -1


class FittingAlignmentMatrix(LevMatrix):
    def __init__(self, s, t):
        self.max_value = None
        LevMatrix.__init__(self, s, t, weight=weight)

    def calculatePathFromTop(self, top, x, y):
        return top - 1 if y > 0 else 0

    def createCell(self, x, y, weight, prevCell=None):
        if y == len(t) and (not self.max_value or self.matrix[self.max_value] < weight):
            self.max_value = (x, y)
        return weight


def printAlignment(m, cell):
    s_prefix = ''
    t_prefix = ''
    while cell[1] >= 1:
        cell_value = m.matrix[cell[0], cell[1]]
        diag = m.matrix[cell[0] - 1, cell[1] - 1]
        top = m.matrix[cell[0] - 1, cell[1]]
        left = m.matrix[cell[0], cell[1] - 1]

        s_char = s[cell[0] - 1]
        t_char = t[cell[1] - 1]
        if diag + weight(s_char, t_char) == cell_value:
            s_prefix = s_char + s_prefix
            t_prefix = t_char + t_prefix
            cell = (cell[0] - 1, cell[1] - 1)
        elif top - 1 == cell_value:
            s_prefix = s_char + s_prefix
            t_prefix = GAP_SYMBOL + t_prefix
            cell = (cell[0] - 1, cell[1])
        elif left - 1 == cell_value:
            s_prefix = GAP_SYMBOL + s_prefix
            t_prefix = t_char + t_prefix
            cell = (cell[0], cell[1] - 1)
        else:
            #sys.exit(1)
            raise Exception("Something wrong is happening")
    print(s_prefix)
    print(t_prefix)

    res = 0
    for i in range(len(s_prefix)):
        res += 1 if s_prefix[i] == t_prefix[i] else -1
    print(res)


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    m = FittingAlignmentMatrix(s, t)
    print(m)
    print(m.max_value)
    print(m.matrix[m.max_value])
    printAlignment(m, m.max_value)

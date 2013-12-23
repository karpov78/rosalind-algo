from python.lev_matrix import LevMatrix, LevMatrixCell, getPAMWeight


class LocalAlignmentMatrix(LevMatrix):
    def __init__(self, s, t):
        self.maxCell = LevMatrixCell(-1, -1, 0, None, None)
        LevMatrix.__init__(self, s, t, weight=lambda a, b: getPAMWeight(a, b))

    def buildCell(self, diag, top, left, x, y):
        none = self.cellFactory(x, y, 0, None)
        result = max(LevMatrix.buildCell(self, diag, top, left, x, y), none, key=lambda x: x.weight)
        if result.weight > self.maxCell.weight:
            self.maxCell = result
        return result


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    matrix = LocalAlignmentMatrix(s, t)
    mCell = matrix.maxCell
    print
    print(mCell.weight)
    print(mCell.s_prefix)
    print(mCell.t_prefix)

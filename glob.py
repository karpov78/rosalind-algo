from matrix import parseIntMatrix, Matrix

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

def getWeight(a, b):
    if a == GAP_SYMBOL or b == GAP_SYMBOL:
        return GAP_WEIGHT
    else:
        return BLOSUM62[SYMBOLS.index(a), SYMBOLS.index(b)]


def _validate(d, s, t):
    if len(s) != len(t):
        raise Exception("Inconsistent lengths")
    count = 0
    for i in range(len(s)):
        count += getWeight(s[i], t[i])
        #print("%s -> %s = %d (%d)" % (s[i], t[i], getWeight(s[i], t[i]), count))
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


def _calculateDistanceMatrix(s, t):
    len_s = len(s)
    len_t = len(t)
    matrix = Matrix(rows=len_s + 1, cols=len_t + 1, format="%3d")
    paths = {}
    for i in range(-1, len_s):
        for j in range(-1, len_t):
            if i < 0 and j < 0:
                matrix[0, 0] = 0
                paths[0, 0] = []
                continue
            if i < 0:
                matrix[0, j + 1] = matrix[0, j] + GAP_WEIGHT
                paths[0, j + 1] = [] if (0, j) not in paths else paths[0, j] + [(0, j + 1)]
                continue
            if j < 0:
                matrix[i + 1, 0] = matrix[i, 0] + GAP_WEIGHT
                paths[i + 1, 0] = [] if (i, 0) not in paths else paths[i, 0] + [(i + 1, 0)]
                continue
            diag = matrix[i, j] + getWeight(s[i], t[j])
            new_step = [(i + 1, j + 1)]
            if s[i] == t[j]:
                matrix[i + 1, j + 1] = diag
                paths[i + 1, j + 1] = paths[i, j] + new_step
            else:
                top = matrix[i, j + 1] + GAP_WEIGHT
                left = matrix[i + 1, j] + GAP_WEIGHT
                matrix[i + 1, j + 1] = max(top, left, diag)

                if top >= left and top >= diag:
                    paths[i + 1, j + 1] = paths[i, j + 1] + new_step
                elif left >= top and left >= diag:
                    paths[i + 1, j + 1] = paths[i + 1, j] + new_step
                else:
                    paths[i + 1, j + 1] = paths[i, j] + new_step
            del paths[i, j]
    return matrix, paths


def editString(s, t):
    matrix, paths = _calculateDistanceMatrix(s, t)

    len_s = len(s)
    len_t = len(t)

    path = paths[len_s, len_t]
    if path[0][0] == 0:
        edited_s = '-'
        edited_t = t[0]
    elif path[0][1] == 0:
        edited_s = s[0]
        edited_t = '-'
    else:
        edited_s = s[0]
        edited_t = t[0]

    prev_step = path[0]
    for step in path[1:]:
        if prev_step[0] + 1 == step[0] and prev_step[1] + 1 == step[1]:
            edited_s += s[step[0] - 1]
            edited_t += t[step[1] - 1]
        elif prev_step[0] == step[0] and prev_step[1] + 1 == step[1]:
            edited_s += '-'
            edited_t += t[step[1] - 1]
        elif prev_step[0] + 1 == step[0] and prev_step[1] == step[1]:
            edited_s += s[step[0] - 1]
            edited_t += '-'
        prev_step = step

    return matrix[len_s, len_t], edited_s, edited_t

if __name__ == "__main__":
    s = input()
    t = input()
    target_d, edited_s, edited_t = editString(s, t)
    print(target_d)
    print(edited_s)
    print(edited_t)
    _validate(target_d, edited_s, edited_t)

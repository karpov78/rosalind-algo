from python.matrix import Matrix

__author__ = 'ekarpov'

def _validate(d, s, t):
    if len(s) != len(t):
        raise Exception("Inconsistent lengths")
    count = 0
    for i in range(len(s)):
        count += 0 if s[i] == t[i] else 1
    if d != count:
        raise Exception("Invalid transformation: expected distance - %d, but was - %d" % (d, count))


def calculateDistanceMatrix(s, t):
    len_s = len(s)
    len_t = len(t)
    matrix = Matrix(rows=len_s + 1, cols=len_t + 1, format="%3d")
    paths = {}
    for i in range(-1, len_s):
        for j in range(-1, len_t):
            if i < 0:
                matrix[0, j + 1] = j + 1
                paths[0, j + 1] = [] if (0, j) not in paths else paths[0, j] + [(0, j + 1)]
                continue
            if j < 0:
                matrix[i + 1, 0] = i + 1
                paths[i + 1, 0] = [] if (i, 0) not in paths else paths[i, 0] + [(i + 1, 0)]
                continue
            diag = matrix[i, j]
            new_step = [(i + 1, j + 1)]
            if s[i] == t[j]:
                matrix[i + 1, j + 1] = diag
                paths[i + 1, j + 1] = paths[i, j] + new_step
            else:
                top = matrix[i, j + 1]
                left = matrix[i + 1, j]
                matrix[i + 1, j + 1] = min(top, left, diag) + 1

                if top <= left and top <= diag:
                    paths[i + 1, j + 1] = paths[i, j + 1] + new_step
                elif left <= top and left <= diag:
                    paths[i + 1, j + 1] = paths[i + 1, j] + new_step
                else:
                    paths[i + 1, j + 1] = paths[i, j] + new_step
            del paths[i, j]
    return matrix, paths


def editString(s, t):
    matrix, paths = calculateDistanceMatrix(s, t)
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

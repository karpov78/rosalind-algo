from python.matrix import Matrix

def calculateNumberOfOptimalAlignments(s, t):
    len_s = len(s)
    len_t = len(t)
    matrix = Matrix(rows=len_s + 1, cols=len_t + 1, format="%3d", default=0)
    n_paths = Matrix(rows=len_s + 1, cols=len_t + 1, format="%3d", default=0)
    for i in range(-1, len_s):
        for j in range(-1, len_t):
            if i < 0 and j < 0:
                matrix[0, 0] = 0
                n_paths[0, 0] = 1
                continue
            if i < 0:
                matrix[0, j + 1] = matrix[0, j] + 1
                n_paths[0, j + 1] = 1
                continue
            if j < 0:
                matrix[i + 1, 0] = matrix[i, 0] + 1
                n_paths[i + 1, 0] = 1
                continue

            top = matrix[i, j + 1] + 1
            left = matrix[i + 1, j] + 1
            diag = matrix[i, j] + (1 if s[i] != t[j] else 0)
            matrix[i + 1, j + 1] = min(top, left, diag)

            if top <= left and top <= diag:
                n_paths[i + 1, j + 1] += n_paths[i, j + 1]
            if left <= top and left <= diag:
                n_paths[i + 1, j + 1] += n_paths[i + 1, j]
            if diag <= left and diag <= top:
                n_paths[i + 1, j + 1] += n_paths[i, j]
            n_paths[i + 1, j + 1] %= 134217727
            #    print('-------------------------------------------------')
            #    print(matrix)
            #    print('-------------------------------------------------')
            #    print(n_paths)
            #    print('-------------------------------------------------')
    return n_paths[len_s, len_t]

if __name__ == '__main__':
    s = input()
    t = input()
    print(calculateNumberOfOptimalAlignments(s, t))
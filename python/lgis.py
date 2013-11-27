from python import timer

_index = lambda len, i, j: i * len + j


def printMatrix(m, n):
    for i in range(n):
        print(' '.join(['%-15s' % str(x) for x in m[i * n:i * n + n]]))


def calculateDistanceMatrix(s, t):
    len_s = len(s)
    matrix = [[]] * (len_s * len_s)

    current_index = 0
    left_index = -1
    top_index = -len_s
    diag_index = -len_s - 1

    for i in range(0, len_s):
        for j in range(0, len_s):
            if i == 0:
                matrix[current_index] = [i] if s[i] == t(j) else []
            elif j == 0:
                matrix[current_index] = matrix[top_index]
            elif s[i] == t(j):
                diag = matrix[diag_index]
                matrix[current_index] = diag + [i]
            else:
                top = matrix[top_index] if j > 0 else []
                left = matrix[left_index] if i > 0 else []

                if len(top) > len(left):
                    matrix[current_index] = top
                elif len(left) > len(top):
                    matrix[current_index] = left
                else:
                    matrix[current_index] = left
                    #matrix[diag_index] = None
            current_index += 1
            top_index += 1
            diag_index += 1
            left_index += 1
    return matrix


def longestIncreasing(s):
    matrix = calculateDistanceMatrix(s, t=lambda x: x + 1)
    return matrix[len(s) * len(s) - 1]


def longestDecreasing(s):
    matrix = calculateDistanceMatrix(s, t=lambda x: len(s) - x)
    return matrix[len(s) * len(s) - 1]


if __name__ == '__main__':
    n = int(input())
    s = [int(x) for x in input().split(' ')]
    with timer.Timer() as t:
        print(' '.join([str(s[x]) for x in (longestIncreasing(s))]))
        print(' '.join([str(s[x]) for x in longestDecreasing(s)]))
    print(t.interval)
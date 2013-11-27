import math

cnk_values = {}


def c(n, k):
    if k == 0 or n < k:
        return 0
    if k == 1 or k == n:
        return 1
    if (n, k) in cnk_values:
        return cnk_values[n, k]
    result = (c(n - 1, k - 1) + c(n - 1, k))
    cnk_values[n, k] = result
    return result


def prob(SIZE, p, k):
    return c(SIZE, k) * math.pow(p, k) * math.pow(1 - p, SIZE - k)


def gen(SIZE, gen):
    res = [0] * SIZE
    for i in range(SIZE):
        p = 0
        for j in range(len(gen)):
            p += gen[j] * prob(SIZE, (j + 1) / SIZE, i + 1)
        res[i] = p
    return res


if __name__ == '__main__':
    N, m, g, k = (int(x) for x in input().split())
    SIZE = 2 * N
    generation = [0] * SIZE
    generation[m - 1] = 1
    for i in range(g):
        print(' '.join(['%.3f' % x for x in generation]))
        generation = gen(SIZE, generation)
    print(' '.join(['%.3f' % x for x in generation]))

    res = 0
    for i in range(SIZE - k, SIZE):
        res += generation[i]
    print(1 - res)


import math

import timer

cache = {}


def c(n, k):
    if (n, k) in cache:
        return cache[n, k]
    elif (n, n - k) in cache:
        return cache[n, n - k]
    elif n == k or k == 0:
        return 1
    else:
        value = c(n - 1, k) + c(n - 1, k - 1)
        cache[n, k] = value
        return value


if __name__ == '__main__':
    n = 2 * int(input())
    A = [0] * n
    sum = 0
    p = 1
    for i in range(n):
        p /= float(2)

    with timer.Timer() as t:
        for j in reversed(range(n)):
            sum += c(n, j + 1)
            A[j] = math.log(sum * p, 10)
        print(' '.join(['%f' % x for x in A]))
    print(t)

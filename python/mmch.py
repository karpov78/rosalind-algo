from util import readDNAs

__author__ = 'evgeny'

factorial_cache = {}


def fact(x):
    if x in factorial_cache:
        return factorial_cache[x]
    if x == 1 or x == 0:
        return 1
    f = x * fact(x - 1)
    factorial_cache[x] = f
    return f


def combination(n, k):
    return fact(n) / (fact(k) * fact(n - k))


def rep_combination(n, k):
    return combination(n + k - 1, k)


def max_pairs(n1, n2):
    n_max = max(n1, n2)
    n_min = min(n1, n2)
    return fact(n_max) / fact(n_max - n_min)


if __name__ == '__main__':
    s = readDNAs()[0][1]
    print s

    spectre = {'A': 0, 'U': 0, 'C': 0, 'G': 0}
    for c in s:
        spectre[c] += 1

    au_pairs = max_pairs(spectre['A'], spectre['U'])
    cg_pairs = max_pairs(spectre['C'], spectre['G'])
    print au_pairs * cg_pairs
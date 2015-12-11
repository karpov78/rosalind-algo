from util import readDNAs

__author__ = 'evgeny'

cat_cache = {}


def cat(n):
    if n == 0 or n == 1:
        return 1

    if n in cat_cache:
        return cat_cache[n]

    res = 0
    for i in xrange(n):
        res += cat(i) * cat(n - i - 1)
    cat_cache[n] = res % 1000000
    return res % 1000000


if __name__ == '__main__':
    s = readDNAs()[0][1]
    print cat(len(s) / 2)

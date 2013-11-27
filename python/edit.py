import sys

__author__ = 'ekarpov'

cache = {}
sys.setrecursionlimit(10000)


def levenstein(s, t):
    len_s = len(s)
    len_t = len(t)

    if len_s == 0:
        return len_t
    elif len_t == 0:
        return len_s
    elif (s, t) in cache:
        return cache[s, t]
    else:
        cost = 1 if s[-1] != t[-1] else 0
        d = min(levenstein(s[:-1], t) + 1, levenstein(s, t[:-1]) + 1,
                levenstein(s[:-1], t[:-1]) + cost)
        cache[s, t] = d
        return d


s = input()
t = input()

print(levenstein(s, t))

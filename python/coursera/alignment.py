import sys

mn_cache = {}


def min_num_coins(n, coins):
    if n == 0:
        return 0
    if n < 0:
        return 10000000000;
    if n in mn_cache:
        return mn_cache[n]
    if n in coins:
        return 1
    res = min([min_num_coins(n - x, coins) for x in coins]) + 1
    mn_cache[n] = res
    return res


sys.setrecursionlimit(10000)
n = int(raw_input())
coins = [int(x) for x in raw_input().split(',')]
print min_num_coins(n, coins)

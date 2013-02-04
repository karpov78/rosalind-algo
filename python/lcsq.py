import sys

__author__ = 'ekarpov'

lcs_cache = {}

def lcs(s, t):
    global lcs_cache

    if len(s) == 0 or len(t) == 0:
        return ''
    elif (s, t) in lcs_cache:
        return lcs_cache[s, t]
    elif s[0] == t[0]:
        result = s[0] + lcs(s[1:], t[1:])
        lcs_cache[s, t] = result
        return result
    else:
        s1 = lcs(s, t[1:])
        s2 = lcs(s[1:], t)
        result = s1 if len(s1) > len(s2) else s2
        lcs_cache[s, t] = result
        return result

if __name__ == "__main__":
    s = input()
    t = input()

    sys.setrecursionlimit(10000)
    print(''.join(lcs(s, t)))

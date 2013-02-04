from python.lcsq import lcs

__author__ = 'ekarpov'

def lss(s, t):
    c = lcs(s, t)
    i = j = k = 0
    res = ''
    while i < len(s) or j < len(t) or k < len(c):
        cs = '$' if i == len(s) else s[i]
        ct = '$' if j == len(t) else t[j]
        cc = '$' if k == len(c) else c[k]
        if cs == ct == cc:
            res += cs
            i += 1
            j += 1
            k += 1
        else:
            if cs != cc:
                res += cs
                i += 1
            if ct != cc:
                res += ct
                j += 1
    return res


if __name__ == "__main__":
    s = input()
    t = input()

    print(lss(s, t))
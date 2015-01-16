from util import getHammingDistance

if __name__ == '__main__':
    t = raw_input()
    s = raw_input()
    d = int(raw_input())

    len_s = len(s)
    len_t = len(t)

    res = []
    for i in range(0, len_s - len_t + 1):
        ss = s[i:i + len_t]
        if getHammingDistance(t, ss) <= d:
            res.append(i)

    print ' '.join([str(x) for x in res])
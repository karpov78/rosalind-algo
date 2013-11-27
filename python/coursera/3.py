import re

if __name__ == '__main__':
    t = raw_input()
    s = raw_input()

    len_t = len(t)
    len_s = len(s)

    #    res = [m.start() for m in re.finditer(t, s)]
    res = []
    for i in range(0, len_s - len_t):
        if s[i:i + len_t] == t:
            res.append(i)
    print(' '.join([str(x) for x in res]))
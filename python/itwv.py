from python.matrix import Matrix


def tryInterwoven(s, t, u, i):
    savepoints = set()
    savepoints.add((i, 0, 0))

    while len(savepoints) > 0:
        i, it, iu = savepoints.pop()
        while it < len(t) and iu < len(u):
            if i >= len(s):
                return False
            if s[i] == t[it]:
                if s[i] == u[iu]:
                    savepoints.add((i + 1, it, iu + 1))
                it += 1
            elif s[i] == u[iu]:
                iu += 1
            else:
                break
            i += 1
        while it < len(t) and t[it] == s[i]:
            if s[i] != t[it]:
                break
            i += 1
            it += 1
        while iu < len(u) and u[iu] == s[i]:
            if s[i] != u[iu]:
                break
            i += 1
            iu += 1
        if it == len(t) and iu == len(u):
            return True
    return False


def isInterwoven(s, t, u):
    for i in range(len(s)):
        if t[0] == s[i] or u[0] == s[i]:
            if tryInterwoven(s, t, u, i):
                return True
    return False


if __name__ == '__main__':
    s = input()
    p = []
    while True:
        l = input()
        if not l: break
        p.append(l)

    m = Matrix(len(p), default=0)
    for i in range(len(p)):
        for j in range(len(p)):
            m[i, j] = isInterwoven(s, p[i], p[j])
    print(m)
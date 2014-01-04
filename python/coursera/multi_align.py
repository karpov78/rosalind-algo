def align(s, t, u):
    score = lambda x, y, z: 1 if x == y == z else 0
    z = len(u) + 1
    y = len(t) + 1
    x = len(s) + 1
    matrix = [[[0] * z for i in xrange(y)] for j in xrange(x)]

    for i in xrange(1, x):
        for j in xrange(1, y):
            for k in xrange(1, z):
                matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1],
                                      matrix[i - 1][j - 1][k], matrix[i - 1][j][k - 1], matrix[i][j - 1][k - 1],
                                      matrix[i - 1][j - 1][k - 1] + score(s[i - 1], t[j - 1], u[k - 1]))

    i = x - 1
    j = y - 1
    k = z - 1
    s_ = ''
    t_ = ''
    u_ = ''
    while i > 0 or j > 0 or k > 0:
        m = matrix[i][j][k]
        if i > 0 and j > 0 and k > 0 and matrix[i - 1][j - 1][k - 1] + score(s[i - 1], t[j - 1], u[k - 1]) == m:
            alignment = [s[i - 1], t[j - 1], u[k - 1]]
            i -= 1
            j -= 1
            k -= 1
        elif i > 0 and j > 0 and matrix[i - 1][j - 1][k] == m:
            alignment = [s[i - 1], t[j - 1], '-']
            i -= 1
            j -= 1
        elif i > 0 and k > 0 and matrix[i - 1][j][k - 1] == m:
            alignment = [s[i - 1], '-', u[k - 1]]
            i -= 1
            k -= 1
        elif j > 0 and k > 0 and matrix[i][j - 1][k - 1] == m:
            alignment = ['-', t[j - 1], u[k - 1]]
            j -= 1
            k -= 1
        elif i > 0 and matrix[i - 1][j][k] == m:
            alignment = [s[i - 1], '-', '-']
            i -= 1
        elif j > 0 and matrix[i][j - 1][k] == m:
            alignment = ['-', t[j - 1], '-']
            j -= 1
        elif k > 0 and matrix[i][j][k - 1] == m:
            alignment = ['-', '-', u[k - 1]]
            k -= 1
        else:
            raise Exception("Invalid alignment")
        s_ = alignment[0] + s_
        t_ = alignment[1] + t_
        u_ = alignment[2] + u_
    return matrix[-1][-1][-1], (s_, t_, u_)


if __name__ == '__main__':
    s = raw_input()
    t = raw_input()
    u = raw_input()
    score, alignment = align(s, t, u)
    print score
    print '\n'.join(alignment)
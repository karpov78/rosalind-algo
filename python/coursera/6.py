def skew(s):
    res = [0]
    skew = 0
    for i in range(s_len):
        if s[i] == 'C':
            skew -= 1
        elif s[i] == 'G':
            skew += 1
        res.append(skew)
    return res


if __name__ == '__main__':
    s = raw_input()
    s_len = len(s)

    sk = skew(s)
    mins = []
    m_value = 1000
    for i in range(len(sk)):
        if sk[i] < m_value:
            m_value = sk[i]
            mins = [i]
        elif sk[i] == m_value:
            mins.append(i)
    print ' '.join([str(x) for x in mins])
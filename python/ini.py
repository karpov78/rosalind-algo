if __name__ == '__main__':
    s = raw_input()
    res = {'A':0, 'C':0, 'G':0, 'T':0}

    for c in s:
        res[c] += 1
    s = ''
    for c in 'ACGT':
          s += str(res[c]) + ' '
    print s
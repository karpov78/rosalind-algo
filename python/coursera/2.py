from string import maketrans


def reverseCompliment(p):
    return p[::-1].translate(maketrans('ATGC', 'TACG'))


if __name__ == '__main__':
    s = raw_input()
    print reverseCompliment(s)

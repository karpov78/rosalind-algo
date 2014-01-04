from Bio.SubsMat import MatrixInfo as matlist

print_array = lambda a: ' '.join(['%3s' % x for x in a])


def find_middle_edge(s, t, score, pen, top=0, bottom=-1, left=0, right=-1):
    get_score = lambda a, b: score[a, b] if (a, b) in score else score[b, a]
    swap = lambda a, b: (b, a)

    if bottom == -1:
        bottom = len(s)
    if right == -1:
        right = len(t)

    h = bottom - top + 1

    m = (left + right) / 2

    curr = [pen * i for i in xrange(h)]
    # print print_array(curr)
    next = [0] * h
    for i in xrange(left, m):
        for j in xrange(h):
            if j == 0:
                next[0] = curr[0] + pen
            else:
                next[j] = max(curr[j] + pen, curr[j - 1] + get_score(t[i], s[top + j - 1]), next[j - 1] + pen)
        curr, next = swap(curr, next)
        # print print_array(curr)

    curr_paths = [(0, '-')] * h
    for j in xrange(h):
        if j == 0:
            next[0] = curr[0] + pen
        else:
            left = curr[j] + pen
            diag = curr[j - 1] + get_score(t[m], s[top + j - 1])
            up = next[j - 1] + pen
            next[j] = max(left, diag, up)
            if next[j] == diag:
                curr_paths[j] = (j - 1, '\\')
            elif next[j] == up:
                curr_paths[j] = curr_paths[j - 1]
            else:
                curr_paths[j] = (j, '-')
    curr, next = swap(curr, next)
    # print print_array(curr)

    next_paths = [(0, '-')] * h
    for i in xrange(m + 1, right):
        for j in xrange(h):
            if j == 0:
                next[0] = curr[0] + pen
            else:
                left = curr[j] + pen
                diag = curr[j - 1] + get_score(t[i], s[top + j - 1])
                up = next[j - 1] + pen
                next[j] = max(left, diag, up)
                if next[j] == diag:
                    next_paths[j] = curr_paths[j - 1]
                elif next[j] == up:
                    next_paths[j] = next_paths[j - 1]
                else:
                    next_paths[j] = curr_paths[j]
        curr, next = swap(curr, next)
        curr_paths, next_paths = swap(curr_paths, next_paths)
        # print print_array(curr)

    max_j = top + curr_paths[-1][0]
    if curr_paths[-1][1] == '\\':
        return ((max_j, m), (max_j + 1, m + 1))
    elif curr_paths[-1][1] == '-':
        return ((max_j, m), (max_j, m + 1))
    else:
        return ((max_j, m), (max_j + 1, m))


def linear_space_alignment(s, t, top=0, bottom=-1, left=0, right=-1):
    if left == right:
        return (s[top:bottom], '-' * (bottom - top))
    if top == bottom:
        return ('-' * (right - left), t[left:right])

    if bottom == -1:
        bottom = len(s)
    if right == -1:
        right = len(t)
        # print 'Quadrant: (%d, %d) (%d, %d)' % (left, top, right, bottom)

    mid_edge = find_middle_edge(s, t, matlist.blosum62, -5, top, bottom, left, right)
    # print 'Mid edge: ' + ' '.join([str(x) for x in mid_edge])
    a1 = linear_space_alignment(s, t, top, mid_edge[0][0], left, mid_edge[0][1])
    a2 = linear_space_alignment(s, t, mid_edge[1][0], bottom, mid_edge[1][1], right)
    if mid_edge[0][0] + 1 == mid_edge[1][0] and mid_edge[0][1] + 1 == mid_edge[1][1]:
        m = (s[mid_edge[0][0]], t[mid_edge[0][1]])
    elif mid_edge[0][0] == mid_edge[1][0]:
        m = ('-', t[mid_edge[0][1]])
    else:
        m = (s[mid_edge[0][0]], '-')
    return (a1[0] + m[0] + a2[0], a1[1] + m[1] + a2[1])


def calc_score(a1, a2, score, pen):
    get_score = lambda a, b: score[a, b] if (a, b) in score else score[b, a]

    s = 0
    for i in xrange(len(a1)):
        if a1[i] == '-' or a2[i] == '-':
            s += pen
        else:
            s += get_score(a1[i], a2[i])
    return s


if __name__ == '__main__':
    # s = 'ACTTAATT'
    # t = 'GAGCAATT'
    s = raw_input()
    t = raw_input()
    alignment = linear_space_alignment(s, t)
    print calc_score(alignment[0], alignment[1], matlist.blosum62, -5)
    print '\n'.join(alignment)
    # print find_middle_edge(s[:4], t[:4], matlist.blosum62, -5)

    # alns = pairwise2.align.globalds(s, t, matlist.blosum62, -5, -5)
    # print int(alns[0][2])
    # print alns[0][0]
    # print alns[0][1]




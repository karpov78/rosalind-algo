mass_table = {'A': 71, 'C': 103, 'D': 115, 'E': 129, 'F': 147, 'G': 57, 'H': 137, 'I': 113, 'K': 128, 'M': 131,
              'N': 114, 'P': 97, 'R': 156, 'S': 87, 'T': 101, 'V': 99, 'W': 186, 'Y': 163}


def expandList(l):
    res = []
    for c in mass_table.values():
        res += [x + [c] for x in l]
    return res


def allKmers(s, k):
    len_s = len(s)
    if k == 0:
        return ['']
    elif k == len_s:
        return [s]
    res = []
    for i in range(len_s):
        res.append(s[i:i + min(k, len_s - i)] + s[0:max(0, i + k - len_s)])
    return res


def getSpectrum(s):
    spectrum = []
    len_s = len(s)
    for i in range(len_s + 1):
        ss = allKmers(s, i)
        for w in ss:
            spectrum.append(sum(w))
    return sorted(spectrum)


def Score(p, s):
    ps = getSpectrum(p)
    i = 0
    j = 0
    res = 0
    while i < len(s) and j < len(ps):
        if ps[j] == s[i]:
            res += 1
            i += 1
            j += 1
        elif ps[j] < s[i]:
            j += 1
        else:
            i += 1
    return res


def cut(board, n):
    res = []
    minS = None
    for x, s in sorted(board, key=lambda k: -k[1]):
        if len(res) <= n or minS == s:
            res.append(x)
            minS = s
        else:
            break
    return res


N = int(raw_input())
spectrum = [int(x) for x in raw_input().split(' ')]
parentMass = max(spectrum)

leaderPeptides = []
leaderboard = [[]]
leaderScore = 0
while len(leaderboard) > 0:
    print 'Leader board size: %d, found: %d, score: %d' % (len(leaderboard), len(leaderPeptides), leaderScore)

    leaderboard = expandList(leaderboard)
    new_leaderboard = []
    for p in list(leaderboard):
        mass = sum(p)
        score = Score(p, spectrum)
        if mass == parentMass:
            score = Score(p, spectrum)
            if score > leaderScore:
                leaderPeptides = [p]
                leaderScore = score
            elif score == leaderScore:
                leaderPeptides.append(p)
            new_leaderboard.append((p, score))
        elif mass < parentMass:
            new_leaderboard.append((p, score))
    leaderboard = cut(new_leaderboard, N)

print 'Leader board size: %d, found: %d, score: %d' % (len(leaderboard), len(leaderPeptides), leaderScore)
print ' '.join(['-'.join([str(y) for y in x]) for x in leaderPeptides])
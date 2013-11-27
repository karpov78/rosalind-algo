import util


def cut(board, spectrum, n):
    global watch

    scores = [(x, util.Score(util.cyclicSpectrum(x), spectrum)) for x in board]
    res = []
    minS = 0
    for x, s in sorted(scores, key=lambda k: -k[1]):
        if len(res) <= n or minS == s:
            res.append(x)
            minS = s
    return res


M = int(raw_input())
N = int(raw_input())
spectrum = [int(x) for x in raw_input().split(' ')]
spectrum.sort()

c = util.convolution(spectrum)
minV = 0
alphabet = []
for m, v in sorted(c.items(), key=lambda k: -k[1]):
    if len(alphabet) <= M or minV == v:
        alphabet.append(m)
        minV = v
    else:
        break

parentMass = max(spectrum)

leaderPeptides = []
leaderboard = [[]]
leaderScore = 0
loopNumber = 1
while len(leaderboard) > 0:
    print 'Iteration ' + str(loopNumber)
    loopNumber += 1

    print 'Leader board size: %d, found: %d, score: %d' % (len(leaderboard), len(leaderPeptides), leaderScore)
    leaderboard = util.expandList(leaderboard, alphabet)
    new_leaderboard = []
    for p in leaderboard:
        mass = sum(p)
        score = util.Score(util.cyclicSpectrum(p), spectrum)
        if mass == parentMass:
            if score > leaderScore:
                leaderPeptides = [p]
                leaderScore = score
            elif score == leaderScore:
                leaderPeptides.append(p)
            new_leaderboard.append(p)
        elif mass < parentMass:
            new_leaderboard.append(p)
    leaderboard = cut(new_leaderboard, spectrum, N)

print 'found: %d, score: %d' % (len(leaderPeptides), leaderScore)
print ' '.join(['-'.join([str(y) for y in x]) for x in leaderPeptides])

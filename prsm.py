from util import getIsotopicWeight
from conv import mDiff, getMaxMultiplicity

def calcDiff(s, R):
    global s_s, i, x, weights
    s_s = set()

    weights = []
    for i in range(1, len(s)):
        weights.append(getIsotopicWeight(s[:i]))
        weights.append(getIsotopicWeight(s[-i:]))
    weights.append(getIsotopicWeight(s))
    diff = mDiff(weights, R)
    max, max_key = getMaxMultiplicity(diff)
    return max

if __name__ == '__main__':
    n = int(input())
    S = []
    for i in range(n):
        S.append(input())

    R = []
    while True:
        line = input()
        if not line: break
        R.append(float(line))

    max = 0
    max_s = ''
    for s in S:
        s_max = calcDiff(s, R)
        if s_max > max:
            max = s_max
            max_s = s
    print(max)
    print(max_s)
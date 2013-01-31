import util

dataset = []
while True:
    s = input()
    if not s:
        break
    dataset.append(s)

pairs = set()
corr = []
for x in dataset:
    if not x in pairs:
        cx = util.reverseComplement(x)
        if not cx in pairs:
            pairs.add(x)
        else:
            pairs.remove(cx)
            corr.append(x)
            corr.append(cx)
    else:
        pairs.remove(x)
        corr.append(x)

err_list = list(pairs)
for i in err_list:
    for j in corr:
        if util.getHammingDistance(i, j) == 1 or util.getHammingDistance(i, util.reverseComplement(j)) == 1:
            print("%s->%s" % (i, j))
            break
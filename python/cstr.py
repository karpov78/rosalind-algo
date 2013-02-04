def buildCharacterTable(data):
    result = []
    for i in range(len(data[0])):
        chars = {}
        for s in data:
            if s[i] in chars:
                chars[s[i]] += 1
            else:
                chars[s[i]] = 1
        c = max(chars, key=lambda x: chars[x])
        if 1 < chars[c] < len(data) - 1:
            row = ['0'] * len(data)
            for j in range(len(data)):
                if data[j][i] == c:
                    row[j] = '1'
            result.append(''.join(row))
    return result


if __name__ == '__main__':
    data = []
    while True:
        s = input()
        if not s: break
        data.append(s)
    print('\n'.join(buildCharacterTable(data)))

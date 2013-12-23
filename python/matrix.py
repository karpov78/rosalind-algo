class Matrix:
    def __init__(self, rows, cols=None, type='i', default=0, format='%d'):
        self._rows = rows
        self._cols = cols if cols else rows
        self._matrix = [[default] * self._cols for x in xrange(self._rows)]
        self._default = default
        self._format = format

    def index(self, row, col):
        return row * self._cols + col

    def decode(self, index):
        x = index / self._cols
        return x, index - x * self._cols

    def isDefault(self, key):
        return self._matrix[key[0]][key[1]] == self._default

    def __len__(self):
        return self._rows

    def __getitem__(self, key):
        if type(key) is tuple:
            return self._matrix[key[0]][key[1]]
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if type(key) is tuple:
            self._matrix[key[0]][key[1]] = value
        else:
            raise TypeError

    def __delitem__(self, key):
        if type(key) is tuple:
            self._matrix[key[0]][key[1]] = self._default
        else:
            raise TypeError

    def __str__(self):
        return '\n'.join([' '.join([self._format % y for y in x]) for x in self._matrix])


def parseIntMatrix(*rows):
    result = Matrix(len(rows), len(rows[0].split(' ')))
    for i in range(len(rows)):
        row = rows[i].split(' ')
        for j in range(len(row)):
            result[i, j] = int(row[j])
    return result

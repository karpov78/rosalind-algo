# coding=utf-8

class Matrix:
    def __init__(self, rows, cols=None, default=1000000000000, format='%d'):
        self._rows = rows
        self._cols = cols if cols else rows
        self._matrix = [default] * (self._rows * self._cols)
        self._default = default
        self._format = format

    def index(self, row, col):
        return row * self._cols + col

    def decode(self, index):
        x = index / self._cols
        return x, index - x * self._cols

    def isDefault(self, key):
        return self._matrix[self.index(key[0], key[1])] == self._default

    def __len__(self):
        return self._rows

    def __getitem__(self, key):
        if type(key) is tuple:
            return self._matrix[self.index(key[0], key[1])]
        elif type(key) is int:
            return self._matrix[key]
        else:
            raise TypeError

    def __setitem__(self, key, value):
        if type(key) is tuple:
            self._matrix[self.index(key[0], key[1])] = value
        elif type(key) is int:
            self._matrix[key] = value
        else:
            raise TypeError

    def __delitem__(self, key):
        if type(key) is tuple:
            self._matrix[self.index(key[0], key[1])] = self._default
        elif type(key) is int:
            self._matrix[key] = self._default
        else:
            raise TypeError

    def __str__(self):
        rows = [''] * self._rows
        for i in range(self._rows):
            rows[i] = ' '.join(
                [self._format % cell for cell in self._matrix[i * self._cols:i * self._cols + self._cols]])
        return '\n'.join(rows)


def parseIntMatrix(*rows):
    result = Matrix(len(rows), len(rows[0].split(' ')))
    for i in range(len(rows)):
        row = rows[i].split(' ')
        for j in range(len(row)):
            result[i, j] = int(row[j])
    return result

# coding=utf-8

class Matrix:
    def __init__(self, rows, cols=None, default=1000000000000, format='%d'):
        self._rows = rows
        self._cols = cols if cols else rows
        self._matrix = [[default for x in range(self._cols)] for x in range(self._rows)]
        self._default = default
        self._format = format

    def isDefault(self, key):
        return self._matrix[key[0]][key[1]] == self._default

    def __len__(self):
        return len(self._matrix)

    def __getitem__(self, key):
        if not type(key) is tuple:
            raise TypeError("Tuple is expected")
        if type(key[0]) is int:
            if type(key[1]) is int:
                if 0 <= key[0] < self._rows and 0 <= key[1] < self._cols:
                    return self._matrix[key[0]][key[1]]
                else:
                    raise IndexError
            elif key[1] is None:
                if 0 <= key[0] < self._rows:
                    return self._matrix[key[0]]
                else:
                    raise IndexError
        elif key[0] is None and type(key[1]) is int:
            if 0 <= key[1] < self._cols:
                new_res = []
                for i in range(self._cols):
                    new_res.append(self._matrix[i][key[1]])
                return new_res
            else:
                raise IndexError
        else:
            raise TypeError


    def __setitem__(self, key, value):
        if not type(key) is tuple or not type(key[0]) is int or not type(key[1]) is int:
            raise TypeError
        self._matrix[key[0]][key[1]] = value

    def __delitem__(self, key):
        if not type(key) is tuple or not type(key[0]) is int or not type(key[1]) is int:
            raise TypeError
        del self._matrix[key[0]]
        self._rows -= 1
        for i in range(self._rows):
            del self._matrix[i][key[1]]
        self._cols -= 1

    def __getattr__(self, item):
        if item == 'cols':
            return self._cols
        elif item == 'rows':
            return self._rows

    def __str__(self):
        return '\n'.join([' '.join([self._format % y for y in x]) for x in self._matrix])

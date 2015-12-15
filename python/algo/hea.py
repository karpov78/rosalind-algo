from util import test_data, swap

class MaxHeap:
    def __init__(self, length, key=lambda _x: 1000000 if not _x else _x):
        self.items = [0] * (length + 1)
        self.inc_size = length
        self.size = 0
        self.key = key

    def size(self):
        return self.size

    def add(self, i):
        if self.last == len(self.items):
            self.items += [0] * self.inc_size
        self.size += 1
        self.items[self.size] = i
        self._shuffle_up(self.last)

    def get_max(self):
        if self.size == 0:
            return -1
        return self.items[1]

    def extract_max(self):
        if self.size == 0:
            raise Exception("Extracting from empty heap")

        _result = self.items[1]
        self.size -= 1
        if self.size > 0:
            self.items[1] = self.items[self.size + 1]
            self._shuffle_down(1)
        return _result

    def _shuffle_up(self, idx):
        while (idx >> 1) > 0:
            p = idx >> 1
            if self.items[p] < self.items[idx]:
                swap(self.items, p, idx)
            idx = p

    def _shuffle_down(self, idx):
        _item_key = self.key(self.items[idx])

        _left_idx = idx * 2 - 1
        if _left_idx > self.size:
            return
        _left_key = self.key(self.items[_left_idx])
        _right_key = self.key(None) if _left_idx + 1 > self.size else self.key(self.items[_left_idx + 1])
        if _left_key <= _right_key and _left_key > _item_key:
            swap(self.items, idx, _left_idx)
            self._shuffle_down(_left_idx)
        elif _right_key > _item_key:
            swap(self.items, idx, _left_idx + 1)
            self._shuffle_down(_left_idx + 1)

    def __add__(self, other):
        self.add(other)
        return self

    def __str__(self):
        return ' '.join([str(self.items[i]) for i in xrange(1, self.size + 1)])


class MinHeap:
    def __init__(self, length, key=lambda _x: 1000000 if not _x else _x):
        self.items = [0] * (length + 1)
        self.inc_size = length
        self.size = 0
        self.key = key

    def __len__(self):
        return self.size

    def add(self, i):
        if self.size > len(self.items):
            self.items += [0] * self.inc_size
        self.size += 1
        self.items[self.size] = i
        self._shuffle_up(self.size)

    def get_min(self):
        if self.size == 0:
            return -1
        return self.items[1]

    def extract_min(self):
        if self.size == 0:
            raise Exception("Extracting from empty heap")

        _result = self.items[1]
        self.size -= 1
        if self.size > 0:
            self.items[1] = self.items[self.size + 1]
            self._shuffle_down(1)
        return _result

    def update(self, key):
        i = 0
        while i <= self.size:
            if key(self.items[i]):
                self._shuffle_up(i)
                return
            i += 1

    def _shuffle_up(self, idx):
        while (idx >> 1) > 0:
            p = idx >> 1
            if self.key(self.items[p]) > self.key(self.items[idx]):
                swap(self.items, p, idx)
            idx = p

    def _shuffle_down(self, idx):
        _item_key = self.key(self.items[idx])

        _left_idx = idx * 2 - 1
        if _left_idx > self.size:
            return
        _left_key = self.key(self.items[_left_idx])
        _right_key = self.key(None) if _left_idx + 1 > self.size else self.key(self.items[_left_idx + 1])
        if _left_key <= _right_key and _left_key < _item_key:
            swap(self.items, idx, _left_idx)
            self._shuffle_down(_left_idx)
        elif _right_key < _item_key:
            swap(self.items, idx, _left_idx + 1)
            self._shuffle_down(_left_idx + 1)

    def __add__(self, other):
        self.add(other)
        return self

    def __str__(self):
        return ' '.join([str(self.items[i]) for i in xrange(1, self.size + 1)])

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]
    h = MaxHeap(n)
    for x in a:
        h += x
    h.validate()
    print h

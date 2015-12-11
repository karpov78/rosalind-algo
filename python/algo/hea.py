from util import test_data

class Heap:
    def __init__(self, length):
        self.heap = [0] * (length + 1)
        self.last = 1

    def size(self):
        return self.last - 1

    def add(self, i):
        if self.size == len(self.heap):
            raise Exception("Heap size exceeded")
        self.heap[self.last] = i
        self._shuffle_up(self.last)
        self.last += 1

    def _shuffle_up(self, idx):
        while (idx >> 1) > 0:
            p = idx >> 1
            if self.heap[p] < self.heap[idx]:
                t = self.heap[p]
                self.heap[p] = self.heap[idx]
                self.heap[idx] = t
            idx = p

    def validate(self):
        for i in xrange(2, self.last):
            if self.heap[i] >self.heap[i >> 1]:
                print "Error index %d is invalid" % i
                break

    def __add__(self, other):
        self.add(other)
        return self

    def __str__(self):
        return ' '.join([str(self.heap[i]) for i in xrange(1, self.last)])

if __name__ == '__main__':
    with open(test_data(__file__)) as f:
        n = int(f.readline())
        a = [int(x) for x in f.readline().split()]
    h = Heap(n)
    for x in a:
        h += x
    h.validate()
    print h

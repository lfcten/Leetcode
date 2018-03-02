class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.sum_array = [0] * (n + 1)

    def lowbit(self, x):
        return x & -x

    def add(self, x, val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)

    def sum(self, x):
        res = 0
        while x > 0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

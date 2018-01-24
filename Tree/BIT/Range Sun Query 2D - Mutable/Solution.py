class Matrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            return
        self.n, self.m = len(matrix), len(matrix[0])
        self.bit = [[0] * (self.m + 1) for _ in range(self.n + 1)]
        self.matrix = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row  + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & - i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.sumCorner(row2, col2) - self.sumCorner(row1 - 1, col2) - self.sumCorner(row2, col1 - 1) + self.sumCorner(row1 - 1, col1 - 1)

    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.bit[i][j]
                j += (j & -j)
            i += (i & - i)
        return res


if __name__ == "__main__":
    # Your NumMatrix object will be instantiated and called as such:
    matrix = [[]]
    obj = Matrix(matrix)
    param_1 = obj.sumRegion(0, 0, 1, 1)
import bisect
from collections.d
class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            print(pos, i, j)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            print(height)
            max_h = max(max_h, high)
            res.append(max_h)
        return res


class Solution1:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        to_cor = {}
        for x, l in positions:
            to_cor[x] = 1
            to_cor[x + l] = 1
        for i, v in enumerate(sorted(to_cor.keys())):
            to_cor[v] = i
        print(to_cor)
        over = Overlapper(len(to_cor))
        ans = []
        mx = 0
        for x, l in positions:
            tmx = over.getMax(to_cor[x], to_cor[x + l]) + l
            mx = max(mx, tmx)
            ans.append(mx)
            over.Update(to_cor[x], to_cor[x + l], tmx)
        print(ans)
        return ans


class Overlapper:
    def __init__(self, n):
        self.line = [0] * n

    def getMax(self, a, b):
        return max(self.line[a:b])

    def Update(self, a, b, mx):
        print(a, b, mx)
        self.line[a:b] = [mx] * (b - a)


if __name__ == "__main__":
    cls = Solution1()
    cls.fallingSquares([[1,5],[4,2],[2,3],[2,1]])
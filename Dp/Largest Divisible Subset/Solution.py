import math


class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        end_num = None
        res = []
        pre = {}
        f = {}

        for num in nums:
            r = 0
            for i in range(1, 1 + int(math.sqrt(num))):
                if num % i == 0:
                    j = num // i
                    if i in f and r < f[i]:
                        pre[num] = i
                        r = f[i]
                    if j in f and r < f[j]:
                        r = f[j]
                        pre[num] = j

            f[num] = r + 1

            if end_num is None or f[end_num] < f[num]:
                end_num = num

        while end_num is not None:
            res.append(end_num)
            end_num = pre.get(end_num)

        return res


if __name__ == "__main__":
    cls = Solution()
    cls.largestDivisibleSubset([1, 5, 10, 2, 12, 20])
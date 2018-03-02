# class FenwickTree:
#     def __init__(self, n):
#         self.n = n
#         self.sum_array = [0] * (n + 1)
#
#     def lowbit(self, x):
#         return x & -x
#
#     def add(self, x, val):
#         while x <= self.n:
#             self.sum_array[x] += val
#             x += self.lowbit(x)
#
#     def sum(self, x):
#         res = 0
#         while x > 0:
#             res += self.sum_array[x]
#             x -= self.lowbit(x)
#         return res
#
#
# class Solution:
#     def countRangeSum(self, nums, lower, upper):
#         """
#         :type nums: List[int]
#         :type lower: int
#         :type upper: int
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         sum_array = [upper, lower - 1]
#         total = 0
#         for num in nums:
#             total += num
#             sum_array += [total, total + lower - 1, total + upper]
#         index = {}
#         for i, x in enumerate(sorted(set(sum_array))):
#             index[x] = i + 1
#
#         tree = FenwickTree(len(index))
#
#         ans = 0
#         for i in range(len(nums) - 1, -1, -1):
#             tree.add(index[total], 1)
#             total -= nums[i]
#             ans += tree.sum(index[upper + total]) - tree.sum(index[lower + total - 1])
#         return ans
#
#
# # class Solution:
# #     def countRangeSum(self, nums, lower, upper):
# #         """
# #         :type nums: List[int]
# #         :type lower: int
# #         :type upper: int
# #         :rtype: int
# #         """
# #         # 1. We construct a Cumulative Distributed Function than enables O(1) range sum.
# #         cdf = [0]
# #         for num in nums:
# #             cdf.append(num + cdf[-1])
# #         # 2. We use a binary indexed tree to enable O(log value) time for each inclusive count.
# #         value2count, minimal, maximal = {}, min(cdf), max(cdf)
# #         totalCount = 0
# #         for value in cdf:
# #             low, up = value - upper, value - lower
# #             low, up = max(low, minimal), min(up, maximal)
# #             if up >= low:
# #                 low, up = low - minimal, up - minimal + 1
# #                 lowSum, upSum = 0, 0
# #                 while low > 0:
# #                     if low in value2count:
# #                         lowSum += value2count[low]
# #                     low -= low & (-low)
# #                 while up > 0:
# #                     if up in value2count:
# #                         upSum += value2count[up]
# #                     up -= up & (-up)
# #                 totalCount += upSum - lowSum
# #             value = value - minimal + 1
# #             while value <= maximal - minimal + 1:
# #                 if value not in value2count:
# #                     value2count[value] = 1
# #                 else:
# #                     value2count[value] += 1
# #                 value += value & (-value)
# #         return totalCount
# if __name__ == "__main__":
#     cls = Solution()
#     cls.countRangeSum([-2, 5, -1], -2, 2)

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res
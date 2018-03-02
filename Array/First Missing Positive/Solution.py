class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        if n == 0:
            return 1
        for i in range(n):
            while 0 < nums[i] < n and nums[nums[i]] != nums[i]:
                nums[i], nums[nums[i]] = nums[nums[i]], nums[i]

        for i in range(n):
            if nums[i] < i:
                return i + 1
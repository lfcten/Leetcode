class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_idx = len(nums) - 1
        if len(nums) <= 1:
            return True

        for i in range(last_idx - 1, -1, -1):
            if nums[i] + i >= last_idx:
                last_idx = i

        return last_idx == 0



class Solution1:
    def canjump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_max = 0
        for ind, val in enumerate(nums):
            if ind <= cur_max:
                cur_max = max(cur_max, ind + val)
                if cur_max >= len(nums) - 1:
                    return True
            else:
                return False
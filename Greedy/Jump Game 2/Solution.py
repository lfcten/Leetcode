class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_max = next_max = 0
        step = 0
        for ind, val in enumerate(nums):
            if ind > cur_max:
                step += 1
                cur_max = next_max
            next_max = max(next_max, ind + val)
            # todo: 到达终点即停止
        return step
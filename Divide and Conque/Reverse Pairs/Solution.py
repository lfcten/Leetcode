class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.res = 0

        def divide(nums):
            if len(nums) >= 2:
                return merge(divide(nums[:len(nums) // 2]), divide(nums[len(nums) // 2:]))
            else:
                return nums

        def merge(nums1, nums2):
            l = len(nums1)
            r = len(nums2)
            i, j = 0, 0
            while i < l and j < r:
                if nums1[i] > 2 * nums2[j]:
                    self.res += l - i
                    j += 1
                else:
                    i += 1
            return sorted(nums1 + nums2)

        divide(nums)
        return self.res

if __name__ == "__main__":
    cls = Solution()
    cls.reversePairs([1, 3, 2, 3, 1])
    cls.reversePairs([2, 4, 3, 5, 1])
class Solution:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        res = [0] * k
        for i in range(k + 1):
            j = k - i
            if i > m or j > n:
                continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            res = max(num, res)
        return res


    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        res = []
        while selects > 0:
            start = res[-1] + 1
            end = n - selects + 1
            res.append(max(range(start, end), key=nums.__getitem__))
            selects -= 1
        res = [nums[item] for item in res[1:]]
        return res

    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans


class Solution1:
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        m = len(nums1)
        n = len(nums2)
        res = []
        cur = [(0, 0)]
        for select in range(k, 0, -1):
            temp = []
            best = -1
            for i, j in cur:
                seg_1 = nums1[i: m + n - j - select + 1]
                seg_2 = nums2[j: m + n - i - select + 1]
                max_seg_1, max_seg_2 = max(seg_1) if seg_1 else -1, max(seg_2) if seg_2 else -1
                print(max_seg_1, max_seg_2)
                max_val = max(max_seg_1, max_seg_2)
                if max_val < best:
                    continue
                if max_val > best:
                    temp = []
                    best = max_val
                if max_val == max_seg_1:
                    temp.append((i + seg_1.index(max_val) + 1, j))
                if max_val == max_seg_2:
                    temp.append((i, j + seg_2.index(max_val) + 1))
            res.append(best)
            cur = set(temp)
        return res




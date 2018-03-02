class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        """
        def findKth(A, m, B, n, k):

            if m > n:
                return findKth(B, n, A, m, k)
            elif m == 0:
                return B[k-1]
            elif k == 1:
                return min(A[0], B[0])

            # divide k into two parts  
            pA = min(k/2, m)
            pB = k - pA

            if A[pA-1] < B[pB-1]:
                return findKth(A[pA:], m-pA, B, n, k-pA)
            elif A[pA-1] > B[pB-1]:
                return findKth(A, m, B[pB:], n-pB, k-pB)
            else:
                return A[pA-1]  

        tmp = len(nums1)+len(nums2)
        if tmp % 2 == 0:
            return (findKth(nums1, len(nums1), nums2, len(nums2), tmp/2) + 
                    findKth(nums1, len(nums1), nums2, len(nums2), tmp/2 + 1))/2.0
        else:
            return findKth(nums1, len(nums1), nums2, len(nums2), tmp/2 + 1)
        """

        m, n = len(nums1), len(nums2)
        if m > n:
            nums2, nums1, n, m = nums1, nums2, m, n

        if m == 0:
            if n % 2 == 0:
                return (nums2[n / 2 - 1] + nums2[n / 2]) / 2.0
            else:
                return nums2[n / 2]

        half = (m + n + 1) / 2
        left, right = 0, m
        while left <= right:
            i = (left + right) / 2
            j = half - i
            if i < m and nums2[j - 1] > nums1[i]:
                left = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                right = i - 1
            else:
                if i == 0:
                    maxLeft = nums2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])

                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                if (m + n) % 2 == 0:
                    return (maxLeft + minRight) / 2.0
                else:
                    return maxLeft


# Time:  O(m * n)
# Space: O(min(m, n))

# Given two integer arrays A and B,
# return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation:
# The repeated subarray with maximum length is [3, 2, 1].
# Note:
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100

class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
            """
        def check(length):
            seen = {A[i:i+length]
                    for i in range(len(A) - length + 1)}
            return any(B[j:j+length] in seen
                       for j in range(len(B) - length + 1))

        A = ''.join(map(chr, A))
        B = ''.join(map(chr, B))

        left, right = 0, min(len(A), len(B)) + 1
        while left < right:
            mid = left + (right-left)/2
            if not check(mid):  # find the min idx such that check(idx) == false
                right = mid
            else:
                left = mid+1
        return left-1
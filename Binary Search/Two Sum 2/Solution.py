# two pointer
class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 1
        j = len(numbers)

        while 1:
            ans = numbers[i - 1] + numbers[j - 1]
            if ans > target:
                j -= 1
            elif ans < target:
                i += 1
            else:
                return [i, j]


# binary search
class Solution1:
    def twoSum(self, numbers, target):
        pass


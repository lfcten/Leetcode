class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        candy = [1] * n
        i = 0
        while i < n - 1:
            if ratings[i] < ratings[i + 1]:
                candy[i + 1] = candy[i] + 1
                i += 1
            elif ratings[i] == ratings[i + 1]:
                i += 1
            else:
                j = i
                while ratings[i] > ratings[i + 1]:
                    i += 1
                for k in range(i, j, -1):
                    candy[k - 1] = max(candy[k] + 1, candy[k - 1])
        print(candy)
        return sum(candy)

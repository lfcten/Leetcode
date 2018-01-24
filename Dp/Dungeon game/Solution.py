class Solution:
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        n = len(dungeon[0])

        dp = [float('inf')] * n
        dp[-1] = 1
        for row in dungeon[::-1]:
            for i in range(n)[::-1]:
                dp[i] = max(min(dp[i: i+2]) - row[i], 0)

        return dp[0]


if __name__ == "__main__":
    instance = Solution()
    print(instance.calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]))

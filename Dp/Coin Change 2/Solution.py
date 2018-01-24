class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """

        dp = [0] * (amount + 1)
        dp[0] = 1
        for c in coins:
            for i in range(1, amount + 1):
                if c <= i:
                    dp[i] += dp[i - c]

        return dp[amount]


if __name__ == "__main__":
    cls = Solution()
    print(cls.change(8839, [3, 7, 405, 436]))

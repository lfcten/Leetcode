# dp
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        Max = float('inf')
        dp = [0] + [Max] * amount
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - c] if i - c >= 0 else Max for c in coins]) + 1

        return [dp[amount], -1][dp[amount] == Max]


# DFS
class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.res = float("inf")
        coins.sort(reverse=True)
        self.DFS(coins, amount, 0, 0)
        return self.res if self.res < float("inf") else -1


    def DFS(self, coins, amount, count, index):
        if amount == 0:
            self.res = min(self.res, count)
            return
        for i in range(index, len(coins)):
            if coins[i] <= amount:
                # prude
                if amount < coins[i] * (self.res - count):
                    self.DFS(coins, amount - coins[i], count + 1, i)
                else:
                    break


if __name__ == "__main__":
    cls = Solution()
    cls1 = Solution1()
    print(cls.coinChange([3, 7, 405, 436], 8839))

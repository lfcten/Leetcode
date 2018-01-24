class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if n == 0:
            return 0

        dp = [[-1] * n for _ in range(n)]
        dp[0][0] = grid[0][0]

        for k in range(1, 2 * (n - 1) + 1) :
            temp = [[-1] * n for _ in range(n)]
            for c1 in range(min(k + 1, n)):
                r1 = k - c1
                if r1 >= n or grid[c1][r1] < 0:
                    continue

                for c2 in range(min(k + 1, n)):
                    r2 = k - c2
                    if r2 >= n or grid[c2][r2] < 0:
                        continue

                    cherry_cur = dp[c1][c2]
                    if c1 > 0:
                        cherry_cur = max(cherry_cur, dp[c1 - 1][c2])
                    if c2 > 0:
                        cherry_cur = max(cherry_cur, dp[c1][c2 - 1])
                    if c1 > 0 and c2 > 0:
                        cherry_cur = max(cherry_cur, dp[c1 - 1][c2 - 1])

                    if cherry_cur < 0:
                        continue

                    if c1 == c2:
                        temp[c1][c2] = cherry_cur + grid[c1][k - c1]
                    else:
                        temp[c1][c2] = cherry_cur + grid[c1][k - c1] + grid[c2][k - c2]

            dp = temp
        return max(0, dp[-1][-1])


class Solution1:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid)

        memo = [[[None] * N for _1 in range(N)] for _2 in range(N)]

        def dp(r1, c1, c2):
            r2 = r1 + c1 - c2
            if (N == r1 or N == r2 or N == c1 or N == c2 or
                        grid[r1][c1] == -1 or grid[r2][c2] == -1):
                return float('-inf')
            elif r1 == c1 == N - 1:
                return grid[r1][c1]
            elif memo[r1][c1][c2] is not None:
                return memo[r1][c1][c2]
            else:
                ans = grid[r1][c1] + (c1 != c2) * grid[r2][c2]
                ans += max(dp(r1, c1 + 1, c2 + 1), dp(r1 + 1, c1, c2 + 1),
                           dp(r1, c1 + 1, c2), dp(r1 + 1, c1, c2))

            memo[r1][c1][c2] = ans
            return ans

        return max(0, dp(0, 0, 0))


if __name__ == "__main__":
    cls = Solution()
    print(cls.cherryPickup([[1,1,1,1,1],[1,1,-1,1,1],[-1,-1,1,1,1],[1,1,1,1,1],[-1,1,1,1,1]]))

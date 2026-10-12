class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]

        for _ in range(m):
            dp[_][0] = 1

        for _ in range(n):
            dp[0][_] = 1

        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i] + dp[j][i-1]

        return dp[-1][-1]
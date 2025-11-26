class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        # dp[i][j][r]
        dp= [[[0] * k for _ in range(n)] for _ in range(m)]

        # initialization
        start_mod = grid[0][0] % k
        dp[0][0][start_mod] = 1
        
        for i in range(m):
            for j in range(n):
                val = grid[i][j]
                for r in range(k):
                    new_r = (r + val) % k
                    if i > 0:
                        dp[i][j][new_r] += dp[i-1][j][r]
                    if j > 0:
                        dp[i][j][new_r] += dp[i][j-1][r] 

                    dp[i][j][new_r] %= MOD
        
        return dp[m-1][n-1][0]
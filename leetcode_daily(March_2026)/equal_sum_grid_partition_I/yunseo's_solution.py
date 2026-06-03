class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        total_sum = sum(sum(row) for row in grid)

        #horizontal cut: i번째 행까지의 누적합
        row_sum = 0
        for i in range(m - 1):
            row_sum += sum(grid[i])
            if row_sum * 2 == total_sum:
                return True
        
        #vertical cut: j번째 열까지의 누적합
        col_sum = 0
        for j in range(n-1):
            col_sum += sum(grid[i][j] for i in range(m))
            if col_sum * 2 == total_sum:
                return True

        return False

        
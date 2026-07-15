class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2
from collections import deque
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        mx = -1
        dq = deque([])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        visited = set([])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    visited.add((row, col))
                    dq.append((row, col, 0))

        while dq:
            x, y, distance = dq.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and (nx, ny) not in visited
                    and grid[nx][ny] == 0
                ):
                    mx = max(mx, distance + 1)
                    visited.add((nx, ny))
                    dq.append((nx, ny, distance + 1))
        return mx

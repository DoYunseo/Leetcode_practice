from typing import List
from collections import deque

def bfs(position, visited, row, col, board):
    dq = deque([position])
    visited.add(position[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    max_land = 1
    while dq:
        print(dq)
        (r, c), _ = dq.popleft()
        print(dq)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < row
                and 0 <= nc < col
                and (nr, nc) not in visited
                and board[nr][nc] == 1
            ):
                visited.add((nr, nc))
                dq.append(((nr, nc), 0))
                max_land += 1
    print(max_land)
    return max_land

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set([])
        size = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    size = max(size, bfs(((i, j), 0), visited, rows, cols, grid))
        return size
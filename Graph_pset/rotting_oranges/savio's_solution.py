from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        initial_rot = []
        count = 0     
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:

                    initial_rot.append(((i, j), 0))
                    count += 1
                elif grid[i][j] == 1:
                    count += 1
        def bfs(initial_rots, grid, ROW, COL, count):
            dq = deque(initial_rots)
            visited = set(initial_rots)
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            max_time = 0
            while dq:
                item = dq.popleft()
                r, c = item[0]
                time = item[1]
                max_time = max(time, max_time)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        dq.append(((nr, nc), time + 1))
            return -1 if len(visited) != count else max_time
        return bfs(initial_rot, grid, ROWS, COLS, count)
                


        
class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        dq = deque()
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dq.append((i, j))
                    grid[i][j] = 0
                else: grid[i][j] = -1
        
        while dq:
            s = len(dq)
            while s > 0:
                x, y = dq.popleft()

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == -1:
                        grid[nx][ny] = grid[x][y] + 1
                        dq.append((nx, ny))
                s -= 1

        hp = [(-grid[0][0], 0, 0)]

        while hp:
            sf_val, x, y= heapq.heappop(hp)

            if x == m - 1 and y == n - 1:
                return -1 * sf_val
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    heapq.heappush(hp, (-min(-sf_val, grid[nx][ny]), nx, ny))
                    grid[nx][ny] = -1
        return -1
        
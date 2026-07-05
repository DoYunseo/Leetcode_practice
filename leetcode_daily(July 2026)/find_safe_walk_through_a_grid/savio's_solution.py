class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        cost = [[float('inf')] * n for _ in range(m)]
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

        start_cost = grid[0][0]  # 1 if start cell itself is unsafe
        cost[0][0] = start_cost
        dq = deque([(0, 0)])

        while dq:
            x, y = dq.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    edge_cost = grid[nx][ny]  # 1 if stepping onto unsafe cell, else 0
                    new_cost = cost[x][y] + edge_cost

                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        if edge_cost == 0:
                            dq.appendleft((nx, ny))
                        else:
                            dq.append((nx, ny))

        return health - cost[m - 1][n - 1] >= 1
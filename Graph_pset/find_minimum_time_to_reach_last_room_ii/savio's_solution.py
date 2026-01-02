import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        hp = []
        result = [[float("inf") for _ in range(m)] for _ in range(n)]
        result[0][0] = 0
        print(result)
        heapq.heappush(hp, (0, (0, 0)))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while hp:
            src_time, position = heapq.heappop(hp)
            x, y = position
            if src_time > result[x][y]:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m:
                    move = 1 if (nx + ny) % 2 == 1 else 2
                    min_time = max(src_time, moveTime[nx][ny]) + move
                    if min_time < result[nx][ny]:
                        result[nx][ny] = min_time
                        heapq.heappush(hp, (min_time, (nx, ny)))
        return result[n - 1][m - 1]

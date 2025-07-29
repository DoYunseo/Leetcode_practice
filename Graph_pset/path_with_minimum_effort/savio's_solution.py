class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        result = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        print(result)
        hp = []
        heapq.heappush(hp, (0, (0, 0)))
        result[0][0] = 0

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while hp:
            effort, pos = heapq.heappop(hp)
            x, y = pos

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < rows and 0 <= ny < cols:
                    effort_calc = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    print(nx, ny)
                    if effort_calc < result[nx][ny]:
                        result[nx][ny] = effort_calc
                        heapq.heappush(hp, (effort_calc, (nx, ny)))
        return result[rows - 1][cols - 1]
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        INF = int(1e9)
        m = len(heights)
        n = len(heights[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        effort = [[INF] * n for _ in range(m)]
        effort[0][0] = 0

        heap = [(0,0,0)]  #(effort, x, y)
        
        while heap:
            diff, x, y = heappop(heap)
            if x == m-1 and y == n-1:
                return diff
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    max_effort = max(diff, abs(heights[x][y] - heights[nx][ny]))
                    if effort[nx][ny] > max_effort:
                        effort[nx][ny] = max_effort
                        heappush(heap, (max_effort, nx,ny))
                        
        
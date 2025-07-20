class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        result = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dq = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    dq.append([(r, c), 0])
                    visited[r][c] = 1
        while dq:
            pos, dist = dq.popleft()
            r, c = pos
            result[r][c] = dist
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and (visited[nr][nc] == 0):
                    visited[nr][nc] = 1
                    new_dist = dist + 1
                    dq.append([(nr, nc), new_dist])
        return result

            



        
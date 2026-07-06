class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        MOD = (10 ** 9) + 7

        cost_matrix = [[-float("inf")] * n for _ in range(m)]
        path_count = [[0] * n for _ in range(m)]

        cost_matrix[m - 1][n - 1] = 0
        path_count[m - 1][n - 1] = 1

        directions = [(-1, 0), (0, -1), (-1, -1)]

        # process cells in strictly increasing order of row+col
        cells = [(i, j) for i in range(m) for j in range(n)]
        cells.sort(key=lambda p: p[0] + p[1], reverse=True)
        print(cells)

        for x, y in cells:
            if board[x][y] == "X":
                continue
            if cost_matrix[x][y] == -float("inf") and (x, y) != (m - 1, n - 1):
                continue  # unreachable so far

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != "X":
                    cell = board[nx][ny]
                    digit = 0 if cell in ("S", "E") else int(cell)
                    new_cost = cost_matrix[x][y] + digit

                    if new_cost > cost_matrix[nx][ny]:
                        cost_matrix[nx][ny] = new_cost
                        path_count[nx][ny] = path_count[x][y] % MOD
                    elif new_cost == cost_matrix[nx][ny]:
                        path_count[nx][ny] = (path_count[nx][ny] + path_count[x][y]) % MOD

        if cost_matrix[0][0] == -float("inf"):
            return [0, 0]
        return [cost_matrix[0][0], path_count[0][0] ]
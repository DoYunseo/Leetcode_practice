from typing import List
from collections import deque

def bfs(position, visited, row, col, board):
    dq = deque([position])
    visited.add(position)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while dq:
        r, c = dq.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < row
                and 0 <= nc < col
                and (nr, nc) not in visited
                and board[nr][nc] == "X"
            ):
                visited.add((nr, nc))
                dq.append((nr, nc))


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        count = 0
        visited = set([])
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "X" and (i, j) not in visited:
                    bfs((i, j), visited, rows, cols, board)
                    count += 1
        return count
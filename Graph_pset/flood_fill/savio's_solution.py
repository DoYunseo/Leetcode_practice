from collections import deque
from typing import List

def bfs(position_node, image, starting_color, visited, ROWS, COLS, color):
        dq = deque([position_node])
        visited.add(position_node)
        directions: List = [
            (-1, 0), (1, 0), (0, -1), (0, 1)
        ]
        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                while 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == starting_color and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    image[nr][nc] = color
                    dq.append((nr, nc))

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set([])
        ROW:int = len(image)
        COL: int = len(image[0])
        for r in range(ROW):
            for c in range(COL):
                if r == sr and c == sc and (sr, sc) not in visited:
                    #start bfs from here
                    bfs((sr, sc), image,image[sr][sc], visited, ROW, COL, color)
        image[sr][sc] = color
        print(image)
        return image
        
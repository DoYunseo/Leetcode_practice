from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        hmap = defaultdict(list)

        # get the stuffs in the top matrix
        for i in range(rows):
            r = 0
            c = i

            while r < rows and c < rows:
                hmap[r-c].append(grid[r][c])
                c += 1
                r += 1
        # get the stuff in the bottom matrix

        for i in range(1, rows):
            r = i
            c = 0 

            while r < rows and c < rows:
                hmap[r-c].append(grid[r][c])
                c += 1
                r += 1
        print(hmap)

        for key, val in hmap.items():
            if key >= 0:
                val.sort(reverse=True)
            if key < 0:
                val.sort()
        print(hmap)

        col = 0
        row = 0
        count = 0
        while row < rows and col < rows and count < len(hmap[row - col]):
            grid[row][col] = hmap[row - col][count]
            col += 1
            row += 1
            count += 1
        
        for i in range(1, rows):
            c = i
            r = 0
            count = 0
            while r < rows and c < rows and count < len(hmap[r - c]):
                grid[r][c] = hmap[r - c][count]
                c += 1
                r += 1
                count += 1
        print(grid)

        for i in range(1, rows):
            r = i
            c = 0
            count = 0
            while r < rows and c < rows and count < len(hmap[r - c]):
                grid[r][c] = hmap[r - c][count]
                c += 1
                r += 1
                count += 1
        return grid

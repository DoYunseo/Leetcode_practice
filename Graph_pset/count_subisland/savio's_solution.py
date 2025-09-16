from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find_ulp_parent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.find_ulp_parent(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        ulp1, ulp2 = self.find_ulp_parent(node1), self.find_ulp_parent(node2)
        if ulp1 == ulp2:
            return

        rank1, rank2 = self.rank[ulp1], self.rank[ulp2]

        if rank1 == rank2:
            self.parent[ulp2] = ulp1
            self.rank[ulp1] += 1
        elif rank1 > rank2:
            self.parent[ulp2] = ulp1
        else:
            self.parent[ulp1] = ulp2


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows = len(grid1)
        cols = len(grid1[0])
        number = rows * cols
        visited = set()
        dsu = DisjointSet(number)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Build Union-Find for grid1 using DFS
        def dfs(node, parent_no, visited, directions, dsu, grid):
            visited.add(node)
            x, y = node
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and grid[nx][ny] == 1
                    and (nx, ny) not in visited
                ):
                    new_no = (nx * cols) + ny
                    dsu.union(parent_no, new_no)
                    dfs((nx, ny), parent_no, visited, directions, dsu, grid)

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited and grid1[i][j] == 1:
                    no = (i * cols) + j
                    dfs((i, j), no, visited, directions, dsu, grid1)

        # Now find islands in grid2 and check if they're sub-islands
        visited2 = set()
        count = 0

        def dfs_from_back(node, visited2, directions, grid2, component):
            x, y = node
            visited2.add(node)
            idx = x * cols + y
            component.add(idx)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < rows
                    and 0 <= ny < cols
                    and grid2[nx][ny] == 1
                    and (nx, ny) not in visited2
                ):
                    dfs_from_back((nx, ny), visited2, directions, grid2, component)

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and (i, j) not in visited2:
                    component = set()
                    dfs_from_back((i, j), visited2, directions, grid2, component)
                    valid = True
                    parent_set = set()

                    for idx in component:
                        r, c = idx // cols, idx % cols
                        if grid1[r][c] == 0:
                            valid = False
                            break
                        parent_set.add(dsu.find_ulp_parent(idx))
                    if valid and len(parent_set) == 1:
                        count += 1

        return count

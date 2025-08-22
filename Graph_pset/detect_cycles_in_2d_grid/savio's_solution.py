from typing import List

class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(node, visited, directions, rows, cols, parent_node, path_length):
            visited.add(node)
            x, y = node
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                neighbor = (nx, ny)

                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == grid[x][y]:
                    if neighbor == parent_node: # Ignore the immediate parent
                        continue 
                    if neighbor in visited: # Found a cycle if not parent and already visited
                        if path_length >= 4:
                            return True
                    else: # Explore unvisited neighbor
                        if dfs(neighbor, visited, directions, rows, cols, node, path_length + 1):
                            return True
            return False
                    
        visited = set([])
        rows = len(grid)
        cols = len(grid[0])
        parent = [[(-1, -1) for _ in range(cols)] for _ in range(rows)]
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    if dfs((i, j), visited, directions, rows, cols, (-1, -1), 1):
                        return True
        return False
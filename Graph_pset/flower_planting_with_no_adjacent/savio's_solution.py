class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        result = [0] * (n + 1)
        adj_list = {i: [] for i in range(1, n + 1)}
        visited = set([])

        for u, v in paths:
            adj_list[u].append(v)
            adj_list[v].append(u)
        

        def dfs(node):
            visited.add(node)
            used_colors = set([])
            for n in adj_list[node]:
                used_colors.add(result[n])
            
            for color_choice in range(1, 5):
                if color_choice not in used_colors:
                    result[node] = color_choice
                    break
            for nbor in adj_list[node]:
                if nbor not in visited:
                    dfs(nbor)
        
        for i in range(1, n + 1):
            if i not in visited:
                dfs(i)
        return result[1:]
class Solution:

    def dfs(self, node, adj, visited, depth):
        visited.add(node)
        max_depth = depth
        for nbor in adj[node]:
            if nbor not in visited:
                max_depth = max(max_depth, self.dfs(nbor, adj, visited, depth + 1))
        return max_depth
        
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(edges)
        visited = set()
        MOD = (10 ** 9) + 7

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        for i in range(1, n + 2):
            if i not in visited:
                visited.add(i)
                max_depth = self.dfs(i, adj, visited, 0)
        
        return (2 ** (max_depth - 1)) % MOD
        



        
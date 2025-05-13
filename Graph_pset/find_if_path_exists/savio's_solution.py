class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Steps to solving this problem. First you build your adjacency list
        if n == 1:
            return True
        if n > 1 and len(edges) == 0:
            return False

        adj_list = {i: [] for i in range(n)}
        
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        print(adj_list)
        
        #step 2: do a dfs on the adjacency list

        def dfs(adj_list, source):
            if not adj_list:
                return
            visited = set()
            def dfs_helper(node):
                if node in visited:
                    return
                visited.add(node)
                for neighbor in adj_list[node]:
                    dfs_helper(neighbor)
                return
            dfs_helper(source)
            return visited
        res = dfs(adj_list, source)
        return True if destination in res else False







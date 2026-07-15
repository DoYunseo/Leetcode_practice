class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # to solve it we just need to find if the number of indegrees are even for each of the 
        adj_list = defaultdict(list)
        visited = set([])
        count = 0

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        def dfs(node):
            visited.add(node)
            num_v = 1
            num_edges_doubled = len(adj_list[node])
            for nbor in adj_list[node]:
                if nbor not in visited:
                    sub_num_v, sub_num_edges_doubled = dfs(nbor)
                    num_v += sub_num_v
                    num_edges_doubled += sub_num_edges_doubled
            return num_v, num_edges_doubled
        
        for i in range(n):
            if i not in visited:
                num_v, num_edges_doubled = dfs(i)
                if num_v == 1:
                    count += 1
                    continue

                if num_edges_doubled == num_v * (num_v - 1):
                    count += 1
        return count 

                
        
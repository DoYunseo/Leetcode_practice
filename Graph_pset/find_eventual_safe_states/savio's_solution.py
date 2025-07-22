class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj_list = {i: graph[i] for i in range(n)}
        print(adj_list)

        output = []
        visited = set([])
        pathVis = [0] * n

        def dfs(node, visited, pathVis):
            visited.add(node)
            pathVis[node] = 1

            for nbor in adj_list[node]:
                if nbor not in visited:
                    if dfs(nbor, visited, pathVis) == False:
                        return False
                elif pathVis[nbor]:
                    return False 
            
            pathVis[node] = 0
            return True

        for i in range(n):
            if pathVis[i] == 0:
                if dfs(i, visited, pathVis) == True:
                    output.append(i)
        return output
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #get the indegrees and outdegrees 
        in_degree = {i: 0 for i in range(1, n + 1)}
        out_degree = {i: 0 for i in range(1, n + 1)}

        if n > 1 and not trust:
            return -1
        
        if n == 1:
            return 1
        
        for u, v in trust:
            out_degree[u] += 1
            in_degree[v] += 1
        print(out_degree, in_degree)

        #look for that single person that everyone reports to and does not report to anyone.
        for i in range(1, n + 1):
            if out_degree[i] == 0 and in_degree[i] == n - 1:
                return i
        return -1

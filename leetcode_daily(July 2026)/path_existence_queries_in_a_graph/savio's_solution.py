class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
    
    def fnd_parent(self, node):
        if self.parent[node] == node:
            return node
        self.parent[node] = self.fnd_parent(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        upu, upv = self.fnd_parent(u), self.fnd_parent(v)
        if self.rank[upu] == self.rank[upv]:
            self.parent[upv] = upu
            self.rank[upu] += 1
        elif self.rank[upu] > self.rank[upv]:
            self.parent[upv] = upu
        else:
            self.parent[upu] = upv
    def sp(self, u, v):
        return self.fnd_parent(v) == self.fnd_parent(u)

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        union = Union(n)
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                union.union(i + 1, i)
            
        
        result = []
        for u, v in queries:
            if union.sp(u, v):
                result.append(True)
            else:
                result.append(False)
        return result



        
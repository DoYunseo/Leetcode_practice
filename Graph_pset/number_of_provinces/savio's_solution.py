class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ans = 0
        seen = set()
        n = len(isConnected)
        adjList = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    adjList[i].append(j)
        
        def bfs(start):
            queue = deque([start])
            seen.add(start)
            while queue:
                city = queue.popleft()
                print(city)
                for neighbor in adjList[city]:
                    if neighbor not in seen:
                        queue.append(neighbor)
                        seen.add(neighbor)
        for i in range(n):
            if i not in seen:
                ans += 1
                bfs(i)
        return ans
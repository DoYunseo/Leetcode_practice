class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = {i: rooms[i] for i in range(len(rooms))}
        visited = set([])
        def dfs(node, visited, adj_list):
            if node not in visited:
                visited.add(node)

            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, visited, adj_list)
        for i in range(len(rooms)):
            if i != 0 and i not in visited:
                return False
            else:
                dfs(0, visited, adj_list)
        return True
            
        
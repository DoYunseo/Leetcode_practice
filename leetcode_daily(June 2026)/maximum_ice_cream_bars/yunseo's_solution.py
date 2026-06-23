class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        cnt = 0
        
        while costs and costs[-1] <= coins:
            coins -= costs.pop()
            cnt += 1
        return cnt
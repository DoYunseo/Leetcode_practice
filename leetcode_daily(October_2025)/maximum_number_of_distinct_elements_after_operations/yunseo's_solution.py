class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        prev = -math.inf

        for num in nums:
            candidate = max(num - k, prev + 1)
            if candidate <= num + k:
                curr = candidate
                cnt += 1
                prev = curr

        return cnt
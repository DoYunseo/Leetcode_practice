class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        before = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                if before != -1 and i - before - 1 < k:
                    return False
                before = i

        return True

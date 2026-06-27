class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)

        for i in range(0, n):
            cnt = 0
            length = 0
            for j in range(i, n):
                length += 1
                if nums[j] == target:
                    cnt += 1
                if cnt * 2 > length:
                    ans += 1
        return ans
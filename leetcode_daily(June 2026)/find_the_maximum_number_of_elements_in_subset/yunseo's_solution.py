from collections import Counter
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ans = 1
        count = Counter(nums)

        if 1 in count:
            ones = count[1]
            ans = max(ans, ones if ones % 2 == 1 else ones -1)
        
        for x in count:
            if x == 1:
                continue
            length = 0
            cur = x
            while count[cur] >= 2:
                length += 2
                cur = cur * cur
            if count[cur] >= 1:
                length += 1
            else:
                length -= 1
            ans = max(ans, length)
        
        return ans

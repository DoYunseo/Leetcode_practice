class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        al = 0
        for g in gain:
            al += g
            if ans < al:
                ans = al
        return ans

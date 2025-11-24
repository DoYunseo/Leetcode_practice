class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        answer = []
        s = ''

        for i in range(len(nums)):
            s += str(nums[i])
            val = int(s, 2)

            # track modulo 5
            answer.append(val % 5 == 0)
        return answer
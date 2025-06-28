class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        
        j_list = []
        for i in range(n):
            if nums[i] == key:
                j_list.append(i)

        ans = set()
        for j in j_list:
            indices = list(range(j-k,j+k+1))
            for index in indices:
                if 0 <= index < n:
                    ans.add(index)
        
        return list(ans)
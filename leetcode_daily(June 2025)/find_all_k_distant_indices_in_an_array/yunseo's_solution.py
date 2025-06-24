class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        n = len(nums)
        #print(n)
        j_list = []
        for i in range(n):
            if nums[i] == key:
                j_list.append(i)
    
        #print(j_list)

        ans = set()
        for j in j_list:
            indices = list(range(j-k,j+k+1))
            #print(indices)
            for index in indices:
                if 0 <= index < n:
                    ans.add(index)
        
       
        #print(ans)
        return list(ans)
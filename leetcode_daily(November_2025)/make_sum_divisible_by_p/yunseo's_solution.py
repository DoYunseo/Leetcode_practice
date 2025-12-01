class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # prefix sum + hashmap
        total = sum(nums)
        r = total % p

        if r == 0:
            return 0
        
        prefix = 0
        best = len(nums)
        mod_index = {0: -1} #prefix mod p -> earliest index

        for j, num in enumerate(nums):
            prefix = (prefix + num) % p
            target = (prefix - r) % p

            if target in mod_index:
                best = min(best, j - mod_index[target])
            
            mod_index[prefix] = j

        return best if best < len(nums) else -1 

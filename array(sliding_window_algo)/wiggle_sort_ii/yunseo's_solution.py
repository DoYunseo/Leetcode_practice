class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # 1. sort the list 
        sorted_nums = sorted(nums)
        print(sorted_nums)

        # 2. divide it into small, large
        n = len(nums)
        mid = (n + 1) // 2
        small = sorted_nums[:mid][::-1]
        large = sorted_nums[mid:][::-1]

        # 3. odd index: large number / even index: small number
        for i in range(n):
            if i % 2 == 0:
                nums[i] = small[i // 2]
            else:
                nums[i] = large[i // 2]
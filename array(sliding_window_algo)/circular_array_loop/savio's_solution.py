from typing import List
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def is_not_cycle(prev, pointer, lst):
            current_direction = lst[pointer] >= 0
            # if the current and prev and pointing
            # in different directions then there is no cycle
            # you should break and start from another iteration
            # also if when you move and then somehow you land at the same position
            if (current_direction != prev) or (lst[pointer] % len(lst) == 0):
                return True 
            return False
        
        n = len(nums)
        for i in range(n):
            slow = i
            fast = i
            prev = nums[i] > 0
            # move slow one step 
            while True:
                slow = (slow + nums[slow]) % n
                if is_not_cycle(prev, slow, nums):
                    break
                
                # first fast move
                fast = (fast + nums[fast]) % n
                if is_not_cycle(prev, fast, nums):
                    break
                #second fast move
                fast = (fast + nums[fast]) % n
                if is_not_cycle(prev, fast, nums):
                    break
                if fast == slow:
                    return True
        return False
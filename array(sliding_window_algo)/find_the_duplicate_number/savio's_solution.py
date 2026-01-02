from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast

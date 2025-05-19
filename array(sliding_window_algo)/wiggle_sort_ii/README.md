# 324. Wiggle Sort II

Given an integer array `nums`, reorder it such that `nums[0] < nums[1] > nums[2] < nums[3]....`

You may assume the input array always has a valid answer.

# Savio's solution Complexity Analysis

Single pass through the array is `O(n)` but we do a sort prior to the even-odd exchange, which is `O(n log n)`

Therefore, the overall time complexity is `O(n log n)`

# Yunseo's solution Complexity Analysis

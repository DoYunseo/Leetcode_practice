2210. Count Hills and Valleys in an Array

You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.

# Yunseo's complexity analysis
Time complexity: O(n^2) - due to in-place pop(i), which takes O(n) time in the worst case.
Space complexity: O(1) - all operations are done in-place with only constant extra space.
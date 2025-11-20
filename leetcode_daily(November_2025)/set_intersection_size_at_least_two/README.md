757. Set Intersection Size At Least Two

You are given a 2D integer array intervals where intervals[i] = [starti, endi] represents all the integers from starti to endi inclusively.

A containing set is an array nums where each interval from intervals has at least two integers in nums.

For example, if intervals = [[1,3], [3,7], [8,9]], then [1,2,4,7,8,9] and [2,3,4,8,9] are containing sets.
Return the minimum possible size of a containing set.

## Yunseo's complexity analysis
- Time complexity: O(n^2) - it has two for loop
- Space complexity: O(n) - use additional 'todo' list that has length of n
# 1394. Find Lucky Integer in an Array

Given an array of integers `arr`, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return `-1`.

# Savio's Solution Complexity Analysis

For this problem, my solution's run time is `O(2n)`. Iterating through the array once to fill the hashmap takes `O(n)` time. Then iterating once through the hashmap which is less than `n` but in the worst case where all the members of the array are unique and there are no duplicates, that runtime complexity will be `O(n)`.

Dropping all constants, my solution's run time complexity is `O(n)`

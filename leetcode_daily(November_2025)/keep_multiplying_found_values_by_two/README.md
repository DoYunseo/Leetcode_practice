# 2154. Keep Multiplying Found Values By Two

You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 \* original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.

# Savio's complexity Analysis

- Time complexity: `O(n)` in the worst case every value in the set is a multiple of the original hence we go up to `n`
- Space complexity: `O(n)` using the set to store the values again

# Yunseo's complexity Analysis
- Time complexity: O(N): goes through len(nums), which is n in the worst case
- Space complexity: O(1): not using any additional space

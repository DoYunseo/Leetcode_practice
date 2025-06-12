# 2367. Number of Arithmetic Triplets

You are given a 0-indexed, strictly increasing integer array `nums` and a positive integer `diff`. A triplet `(i, j, k)` is an arithmetic triplet if the following conditions are met:

`i < j < k`,
`nums[j] - nums[i] == diff`, and
`nums[k] - nums[j] == diff`.
Return the number of unique **arithmetic triplets**.

# Savio's Complexity Analysis

# Yunseo's Complexity Analysis
Time complexity: O(n^3) 
Because it uses three nested loops to check all possible triplets in the list.
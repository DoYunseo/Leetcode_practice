# 2200. Find All K-Distant Indices in an Array

You are given a 0-indexed integer array nums and two integers key and k. A k-distant index is an index i of nums for which there exists at least one index j such that |i - j| <= k and nums[j] == key.

Return a list of all k-distant indices sorted in increasing order

# Yunseo's complexity Analysis
Time complexity: O(n * k) in the worst case,
where n is the length of nums and k is the distance range
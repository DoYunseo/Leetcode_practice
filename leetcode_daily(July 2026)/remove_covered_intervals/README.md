# 1288. Remove Covered Interval

Given an array intervals where `intervals[i] = [li, ri]` represent the interval `[li, ri)`, remove all intervals that are covered by another interval in the list.

The interval `[a, b)` is covered by the interval `[c, d)` if and only if `c <= a` and `b <= d`.

Return the number of remaining intervals.

# Savio's Complexity Analysis

- Time complexity: `O(n log n)` due to sorting
- Space complexity: `O(n)` new list to store result

# 3169. Count Days Without Meetings

You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.

# Savio's complexity analysis

Time complexity: `O(n log n) + O(n)`. Ignoring smaller factors, the time complexity scales by `O(n log n)`
Space complexity: `0(n)`

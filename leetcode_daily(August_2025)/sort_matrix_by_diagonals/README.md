# 3446. Sort Matrix By Diagonals

You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.

# Savio's solution's Complexity Analysis

Time complexity: `O(n^2)`. Filling the matrix in place take `O(n^2)`
Space complexity: `O(n)`: Took a dictionary to store the values in the same diagonal. It's not `O(n^2)` because I filled the same matrix given in the problem statement.

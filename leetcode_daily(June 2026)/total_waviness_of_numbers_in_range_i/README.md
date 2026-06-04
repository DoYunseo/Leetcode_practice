# 3751. Total Waviness Of Numbers In Range I

You are given two integers num1 and num2 representing an inclusive range [num1, num2].

The waviness of a number is defined as the total count of its peaks and valleys:

A digit is a peak if it is strictly greater than both of its immediate neighbors.
A digit is a valley if it is strictly less than both of its immediate neighbors.
The first and last digits of a number cannot be peaks or valleys.
Any number with fewer than 3 digits has a waviness of 0.
Return the total sum of waviness for all numbers in the range [num1, num2].

# Savio's Complexity Analysis

- Time complexity: `O(m * d)` where `m = num2 - num1 + 1`, `d = number of digits ~= log_10(num2)`. We're taking the log of the second number because that is the maximum number of digits the number in that range can potentially reach.

- Space complexity: `O(n)` this is for the _digit_ characters which I stored in an array.

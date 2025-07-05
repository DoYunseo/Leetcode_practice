#

# Savio's Solution Complexity Analysis

For this problem, my solution's run time is `O(2n)`. Iterating through the array once to fill the hashmap takes `O(n)` time. Then iterating once through the hashmap which is less than `n` but in the worst case where all the members of the array are unique and there are no duplicates, that runtime complexity will be `O(n)`.

Dropping all constants, my solution's run time complexity is `O(n)`

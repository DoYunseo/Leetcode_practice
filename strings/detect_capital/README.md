# 520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like `"USA"`.
All letters in this word are not capitals, like `"leetcode"`.
Only the first letter in this word is capital, like `"Google"`.
Given a string `word`, return `true` if the usage of capitals in it is right.

# Savio's Time Complexity Analysis

For each check it is one pass through the string which comes down to `O(n)`, where `n` is the length of the `string`

# Yunseo's Time Complexity Analysis

Time complexity: `O(n)` where 'n' is the length of the string 'word'
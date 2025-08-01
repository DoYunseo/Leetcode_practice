# 3136 Valid Word

A word is considered **valid** if:

- It contains a **minimum** of 3 characters.
- It contains only digits (0-9), and English letters (uppercase and lowercase).
- It includes **at least** one **vowel**.
- It includes **at least** one **consonant**.
You are given a string `word`.

Return `true` if `word` is valid, otherwise, return `false`.

Notes:

`'a'`, `'e'`, `'i'`, `'o'`, `'u'`, and their uppercases are **vowels**.
A **consonant** is an English letter that is not a vowel.

# Savio's complexity analysis

- Space complexity: `O(n)` - space for set and hashmap
- Time complexity: `O(n)` - single loop through `str`

# Yunseo's complexity analysis

- Time complexity: `O(n)` - single loop through str word
- Space complexity: `O(1)` - only a fixed number of variables are used
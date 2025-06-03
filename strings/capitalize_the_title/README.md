# 2129. Capitalize the Title

You are given a string `title` consisting of one or more words separated by a single space, where each word consists of English letters. **Capitalize** the string by changing the capitalization of each word such that:

- If the length of the word is `1` or `2` letters, change all letters to lowercase.
- Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
  Return _the **capitalized**_ `title`.

# Savio's Complexity Analysis

Time complexity of the solution is dependent on the length of the title, once we split it by the space, we trim it down, so essentially the time complexity is `O(length of title)`

# Yunseo's Complexity Analysis

The time complexity of my solution is `O(n)`, where n = title.length().
Because the function processes each character in the input string exactly once through splitting, transforming, and joining.
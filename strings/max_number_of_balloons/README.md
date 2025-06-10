# 1189. Maximum number of balloons

Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.

You can use each character in `text` **at most once**. Return the maximum number of instances that can be formed.

# Savio's solution complexity analysis:

In the worst case, the time complexity is `O(5)` where `5` is the number of **unique** characters in balloon.

# Yunseo's solution complexity analysis

The time complexity is `O(n)`, where n is the length of the input string text, since it processes each character once and performs constant-time dictionary operations.
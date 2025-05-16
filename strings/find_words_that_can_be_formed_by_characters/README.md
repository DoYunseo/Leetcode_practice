1160. Find Words That Can Be Formed by Characters

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used once for **each** word in `words`).

Return _the sum of lengths of all good strings in words_.

# Savio's Solution Complexity Analysis

- To populate the hashmap which stores the freq of chars that takes `O(c)` where `c` is the length of `chars`
- We then loop through each `word` in `words`, which takes `O(w)` where `w` is the length of the words array.
- Considering the constraints posed by the question, the upper bound of `w = 100`
- Then we count the characters of every word in words once. Counting one word takes `O(l)` where `l` is the length of the word.
- We then loop through the key and val pair of the word in the just created counter and do simple `O(1)` checks. The upper bound for this loop is `O(26)` since each word can only contain the letters of the alphabet and there's only `26` **unique** letters. Thus this inner loop can run at most `26` times for each word

Putting this together, we have that the cost of processing characters = `O(C)`
Total cost of looping over words: `sum(O(l) for each word in words)`, which is equivalent to `O(S)`

Thus, the total time complexity is `O(C) + O(S)`

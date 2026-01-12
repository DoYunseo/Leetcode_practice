102. Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Yunseo's complexity analysis
Time complexity: O(N) - where N is the number of nodes in the tree. Each node is visited exactly once during the BFS traversal. 
Space complexity: O(N) - where N is the number of nodes. In the worst case, the queue and the output list may store up to N nodes.
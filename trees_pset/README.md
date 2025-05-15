# 1261. Find Elements in a Contaminated Binary Tree

Given a binary tree with the followinf rules:

1. `root.val == 0`
2. For any `treeNode`:

- If `treeNode.val` has a value `x` and `treeNoode.left != null`, then `treeNode.left.val = 2 * x + 1`
- If `treeNode.val` has a value `x` and `treeNoode.right != null`, then `treeNode.right.val = 2 * x + 2`

Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.

Implement the `FindElements` class:

- `FindElements(TreeNode* root)` initializes the object with a contaminated binary tree and recovers it.

- `bool find(int target)` Returns `true` if the `target` value exists in the recovered binary tree.

# Savio's solution critique

My solution wasn't really elegant. I had to perform two searches for the item but I could have maintained sort of like a set to add the newly transformed node values so i could query them when implementing the concrete find method.

Anyway, moving on to the complexity analysis of my solution.

First we traverse the entire tree structure which takes us about `O(N)` where N is the number of nodes, because we visit one node and perform the necessary transformation before visiting another on the same level

I also perform a dfs algorithm to find the element which I'm interested in finding. In the worst case, we would exhaust the tree and not find the target, so that is again `O(N)`

Adding both, we have: `O(N) + O(N) = O(N)` (dropping the constants)

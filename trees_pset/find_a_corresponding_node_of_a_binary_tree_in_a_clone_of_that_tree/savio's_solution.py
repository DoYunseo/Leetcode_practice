from typing import TreeNode
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def dfs(head, target):
            if not head:
                return None
            if head.val == target.val:
                return head
            left = dfs(head.left, target)
            if left:
                return left
            right = dfs(head.right, target)
            if right:
                return right
        return dfs(cloned, target)    
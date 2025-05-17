# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from collections import deque

def bfs(root):
    root.val = 0
    dq = deque([root])
    while dq:
        item = dq.popleft()
        if item.left:
            if item.left.val == -1:
                item.left.val = 0
            item.left.val = 2 * item.val + 1
            dq.append(item.left)
        if item.right:
            if item.right.val == -1:
                item.right.val = 0
            item.right.val = 2 * item.val + 2
            dq.append(item.right)

    return root
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        recovered = bfs(root)
        self.root = recovered

        

    def find(self, target: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            if node.val == target:
                return True
            return dfs(node.left, target) or dfs(node.right, target)
        return dfs(self.root, target)

        
            
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
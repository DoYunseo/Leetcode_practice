from collections import deque
from typing import List
# efinition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        deck = deque()
        deck.append(root)
        result = []
        while deck:
            size = len(deck)
            arr = []
            for i in range(size):
                popped = deck.popleft()
                if popped.left:
                    deck.append(popped.left)
                if popped.right:
                    deck.append(popped.right)
                arr.append(popped.val)
            result.append(arr)
        return result[::-1]
            
         
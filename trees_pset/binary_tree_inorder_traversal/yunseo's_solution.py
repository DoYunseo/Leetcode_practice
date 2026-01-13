# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        cur = root
        ans = []

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            ans.append(cur.val)

            cur = cur.right

        return ans
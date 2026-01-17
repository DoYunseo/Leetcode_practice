# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        maxi = float("-inf")
        level = 0
        maxlevel = 0
        while dq:
            n = len(dq)
            items = []
            for i in range(n):
                node = dq.popleft()
                items.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            level += 1
            if sum(items) > maxi:
                maxi = sum(items)
                maxlevel = level

        return maxlevel


            

        
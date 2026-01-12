# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])

        while q:
            size = len(q)
            nodes = []
            for _ in range(size):
                node = q.popleft()
                
                if node:
                    nodes.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    nodes.append(None)
                    q.append(None)
                    q.append(None)
                    
            # check if every nodes in same level is symmetric 
            if nodes != nodes[::-1]:
                return False
            if all (v is None for v in nodes):
                break
                
        return True
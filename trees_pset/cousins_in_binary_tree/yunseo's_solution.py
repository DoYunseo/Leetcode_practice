# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque([root])
        level = 1
        cousin = False
        parent_x = 0
        parent_y = 0

        while q:
            size = len(q)
            lst = []

            for _ in range(size):
                node = q.popleft()
                lst.append(node.val)
                
                if node.left:
                    if node.left.val == x:
                        parent_x = node
                    if node.left.val == y:
                        parent_y = node
                    q.append(node.left)
                if node.right:
                    if node.right.val == x:
                        parent_x = node
                    if node.right.val == y:
                        parent_y = node
                    q.append(node.right)
            
            if x in lst and y in lst:
                if parent_x != parent_y:
                    print(parent_x, parent_y)
                    cousin = True
            
        return cousin
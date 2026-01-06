# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        level = 1
        best_level = 1
        max_sum = float('-inf')

        while q:
            level_sum = 0
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                level_sum += node.val
                
                # if next level exist
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)  

            # update best_level
            if max_sum < level_sum:
                max_sum = level_sum
                best_level = level
            level += 1
                    
        return best_level 
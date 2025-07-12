# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sums = 0
        def dfs(root, arr):
            if not root:
                return arr[0]
            if root.left:
                if not root.left.left and not root.left.right:
                    arr[0] += root.left.val
            left = dfs(root.left, arr)
            print(left)
            right = dfs(root.right, arr)
            print(right)
            return arr[0]
        return dfs(root, [0])

        '''
        Root = 3
        left = 9
        9 --> 
        root = 9

        left = 0
        right = 0

        --root = 20--
        left = 15

        --root =15 --
        left
        root = 7

        Bubble up to 20:
        return value of 
        '''



        
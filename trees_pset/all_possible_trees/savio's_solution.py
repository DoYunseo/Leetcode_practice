# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        memo = {0: [], 1:[TreeNode()]}

        def dfs(n):
             #map n to list of fbt we can create with n nodes
            if n in memo:
                return memo[n]
            res = []
            for l in range(1, n, 2): 
                r = n - 1 - l
                leftTrees, rightTrees = dfs(l), dfs(r)

                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0, t1, t2))
            memo[n] = res
            return res
        return dfs(n)
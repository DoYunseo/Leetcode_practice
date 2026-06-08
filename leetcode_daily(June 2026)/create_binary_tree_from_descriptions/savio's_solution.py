# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mapping = defaultdict(lambda: [None, None])
        children = set()
        root_val = None
        for item in descriptions:
            if item[2] == 1:
                mapping[item[0]][0] = item[1]
            
            if item[2] == 0:
                mapping[item[0]][1] = item[1]
            children.add(item[1])

        for item in descriptions:
            if item[0] not in children:
                root_val = item[0]
                break

        # now building the tree
        nodes = {}
        for parent, children in mapping.items():
            if parent not in nodes:
                nodes[parent] = TreeNode(parent)
            if children[0] and children[0] not in nodes:
                nodes[children[0]] = TreeNode(children[0])
            if children[1] and children[1] not in nodes:
                nodes[children[1]] = TreeNode(children[1])
        
        for parent, children in mapping.items():
            nodes[parent].left = nodes[children[0]] if children[0] else None
            nodes[parent].right = nodes[children[1]] if children[1] else None
        
        return nodes[root_val]





        
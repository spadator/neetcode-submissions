# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(node, nodeP, nodeQ):
            if not node or not nodeP or not nodeQ:
                return 
            
            if (max(nodeP.val, nodeQ.val) < node.val):
                return dfs(node.left, nodeP, nodeQ)
            elif (min(nodeP.val, nodeQ.val) > node.val):
                return dfs(node.right, nodeP, nodeQ)
            else:
                return node
        
        return dfs(root, p, q)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)
        
        level = []
        while queue:
            res = []
            qLength = len(queue)
            for i in range(qLength):
                node = queue.popleft()
                if node:
                    res.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right) 
            if res:
                level.append(res)

        return level
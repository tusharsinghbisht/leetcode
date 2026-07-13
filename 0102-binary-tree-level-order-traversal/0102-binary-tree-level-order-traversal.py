# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        prev = [root]
        res = []

        while True:
            r = []
            prev_=[]
            for node in prev:
                r.append(node.val)
                if node.left != None:
                    prev_.append(node.left)
                if node.right != None:
                    prev_.append(node.right)
            res.append(r)

            if not prev_:
                return res
            prev = prev_
            
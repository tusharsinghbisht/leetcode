# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
            
        prev = [root]
        res = []
        level = 0
        while True:
            r = []
            if level % 2: #odd
                prevr = prev[::-1]
            else:
                prevr = prev
            for node in prevr:
                r.append(node.val)
            
            res.append(r)
            prev_ = []
            for node in prev:
                if node.left != None:
                    prev_.append(node.left)
                if node.right != None:
                    prev_.append(node.right)
                    
            if not prev_:
                return res
            prev = prev_
            level += 1

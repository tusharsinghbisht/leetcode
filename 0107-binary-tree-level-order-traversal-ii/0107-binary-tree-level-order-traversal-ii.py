# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []


        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = [0]*level_size

            for i in range(level_size):
                node = queue.popleft()
                current_level[i] = node.val

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            
            result.append(current_level)
        return result[::-1]
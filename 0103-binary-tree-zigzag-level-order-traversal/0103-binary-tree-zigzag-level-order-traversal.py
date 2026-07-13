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
            
        result = []
        queue = deque([root])

        is_left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = [0]*level_size

            for i in range(level_size):
                node = queue.popleft()
                index = i if is_left_to_right else level_size-1-i
                current_level[index] = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)
            is_left_to_right = not is_left_to_right

        return result
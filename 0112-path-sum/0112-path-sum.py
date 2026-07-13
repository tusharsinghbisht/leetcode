# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False


        queue = deque([(root, root.val)])

        while queue:
            node, currSum = queue.popleft()

            if currSum == targetSum and not node.left and not node.right:
                return True

            if node.left:
                queue.append((node.left, currSum+node.left.val))
            if node.right:
                queue.append((node.right, currSum+node.right.val))

        return False
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.req()
        return 11

    def req(self, root: Optional[TreeNode], sum: int, targetSum: int):
        if root is None:
            return  0


solution = Solution()

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)

root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)

root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

print(solution.pathSum(root, 8))


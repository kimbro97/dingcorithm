# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.max_length = 0

        def dfs(node, direction, length):
            if not node:
                return
            self.max_length = max(self.max_length, length)
            if node.left:
                dfs(node.left, 0, length + 1 if direction == 1 else 1)
            if node.right:
                dfs(node.right, 1, length + 1 if direction == 0 else 1)

        dfs(root, 0, 0)  # 왼쪽 방향
        dfs(root, 1, 0)  # 오른쪽 방향

        return self.max_length
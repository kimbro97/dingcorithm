# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countGoodNodes(root, root.val)

    def countGoodNodes(self, root, max_so_far) -> int:
        if root is None:
            return 0

        good = 1 if root.val >= max_so_far else 0

        new_max = max(max_so_far, root.val)

        left_count = self.countGoodNodes(root.left, new_max)
        right_count = self.countGoodNodes(root.right, new_max)

        return good + left_count + right_count




solution = Solution()

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)


print(solution.goodNodes(root))

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        leaves1 = []
        leaves2 = []
        self.getLeafSequence(root1, leaves1)
        self.getLeafSequence(root2, leaves2)
        return leaves1 == leaves2

    def getLeafSequence(self, root, leaves):
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
            return
        self.getLeafSequence(root.left, leaves)
        self.getLeafSequence(root.right, leaves)


# Tree 1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

# Tree 2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)

solution = Solution()

print(solution.leafSimilar(root1, root2))  # Output: True
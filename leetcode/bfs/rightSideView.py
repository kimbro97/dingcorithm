# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_length = len(queue)
            for i in range(level_length):
                node = queue.popleft()

                # 레벨의 마지막 노드일 때 결과에 추가
                if i == level_length - 1:
                    result.append(node.val)

                # 왼쪽 자식 추가
                if node.left:
                    queue.append(node.left)
                # 오른쪽 자식 추가
                if node.right:
                    queue.append(node.right)

        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

solution = Solution()
print(solution.rightSideView(root))


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.left.left = TreeNode(5)

print(solution.rightSideView(root2))

print(solution.rightSideView(None))
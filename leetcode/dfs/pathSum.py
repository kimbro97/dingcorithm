# Definition for a binary tree node.
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0

            curr_sum += node.val

            count = prefixSumCount[curr_sum - targetSum]

            prefixSumCount[curr_sum] += 1

            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            prefixSumCount[curr_sum] -= 1

            return count

        prefixSumCount = defaultdict(int)
        prefixSumCount[0] = 1
        return dfs(root, 0)
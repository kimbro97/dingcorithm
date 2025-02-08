from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        max_sum = current_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, current_sum)

        return max_sum / k


solution = Solution()
print(solution.findMaxAverage([1,12,-5,-6,50,3], 4))
print(solution.findMaxAverage([5], 1))
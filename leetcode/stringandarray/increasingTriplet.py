from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


solution = Solution()
print(solution.increasingTriplet([1,2,3,4,5]))
print(solution.increasingTriplet([5,4,3,2,1]))
print(solution.increasingTriplet([2,1,5,0,4,6]))
print(solution.increasingTriplet([20,100,10,12,5,13]))

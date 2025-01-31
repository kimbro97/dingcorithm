from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        max_value = max(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_value:
                result[i] = True

        return result


solution = Solution()

print(solution.kidsWithCandies([2,3,5,1,3], 3))


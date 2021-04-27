from copy import deepcopy


class Solution:


    def twoSum(self, nums: list, target: int) -> list:
        """
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        for idx, number in enumerate(nums):
            subNums = deepcopy(nums)
            # because position is important I can't remove the item
            subNums[idx] = -200
            for idx2, subNumber in enumerate(subNums):
                if (target - number) == subNumber:
                    return [idx,idx2]

solution = Solution()
print(solution.twoSum([3,2,4],6))
# print(2+2)

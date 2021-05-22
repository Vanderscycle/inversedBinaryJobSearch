class Solution:
    def searchInsert(self, nums, target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
        """
        for i,num in enumerate(nums):
            if num >= target:
                return (i)
        return len(nums)
            #elif num >

if __name__ == "__main__":
    test = [1,3,5,6]
    solution = Solution()
    print(solution.searchInsert(test,5))

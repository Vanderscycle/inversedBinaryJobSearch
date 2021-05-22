from statistics import median
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
        """
        nums1 += nums2
        if len(nums1) == 1:
            return nums1[0]
        return median(nums1)

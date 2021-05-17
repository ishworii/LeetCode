'''
A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)  - 1
        while r > l:
            m = (l + r)//2
            if nums[m] > nums[m + 1]:
                r = m
            else:
                l = m + 1
        return l
        

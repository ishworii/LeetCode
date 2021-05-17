'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

'''

class Solution:
    def reverse(self,arr:list,start:int,end:int) -> None:
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start , end = start + 1,end - 1
            
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums,0,n -1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)

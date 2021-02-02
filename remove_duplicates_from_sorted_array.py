'''
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        
        left = 1
        right = len(nums)-1
        
        value = nums[0]
        
        while left <= right:
            if value == nums[left]:
                nums.pop(left)
                right -= 1
            else:
                value = nums[left]
                left += 1
            

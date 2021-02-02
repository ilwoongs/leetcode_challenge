'''
Intersection of Two Arrays II

Given two arrays, write a function to compute their intersection.
'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = collections.Counter(nums1)
        result = []
        
        for i in nums2:
            if counts[i]>0:
                counts[i] -= 1
                result.append(i)
                
        return result
                

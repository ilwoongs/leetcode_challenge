"""
42. Trapping Rain Water - Hard
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""

#This problem can be solved using a two-pointer technique
class Solution:
    def trap(self, height: List[int]) -> int:
        fromLeft = []
        fromRight = []
        higher = 0
        total = 0
        
        for i in height:
            if i>higher:
                higher = i
            fromLeft.append(higher)
        
        higher = 0
        
        for j in reversed(height):
            if j>higher:
                higher = j
            fromRight.append(higher)
        fromRight.reverse()

        for i in range(len(fromLeft)):
            minHeight = min(fromLeft[i],fromRight[i])
            total += minHeight - height[i]
            
        return total
        
        
        

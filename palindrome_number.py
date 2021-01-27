"""
9. Palindrome Number
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

#This algorithm compares characters from start to end with characters from end to start to check whether the input is palindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        i = 0
        j = len(xStr)-1
        
        while i<=j:
            if xStr[i] != xStr[j]:
                return False
            i += 1;
            j -= 1;
        return True
        

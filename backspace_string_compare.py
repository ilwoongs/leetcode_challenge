'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
'''

#used stack
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool: 
        def finalStr(word:str):
            tempStack = []
            for i in range(len(word)):
                if word[i] == '#':
                    if tempStack == []:
                        continue
                    else:
                        tempStack.pop()
                else:
                    tempStack.append(word[i])
            return tempStack
        return finalStr(S) == finalStr(T)

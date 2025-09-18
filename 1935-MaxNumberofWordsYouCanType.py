'''
Problem Name: 1935. Maximum Number of Words You Can Type
Attempted: # 18-09-2025
'''

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s = text.split(" ")
        count = 0
        for m in s:
            flag = True
            for j in brokenLetters:
                if j in m:
                    flag = False
            if flag:
                count+=1
        return count
                

'''
Problem Name: 459. Repeated Substring Pattern
Attempted : # 02-08-2025
'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if (len(s) < 2):
            return False
        count = 0
        substr = ""
        for i in s:
            substr += i
            if s.count(substr) > 1:
                c = s.count(substr)
                if c*len(substr) == len(s):
                    return True
        return count > 1
# above works but mind blown solution below:


'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        a=s+s
        if s in a[1:-1]:
            return True
        return False
'''

s = Solution()
print(s.repeatedSubstringPattern("abcabcabcabc"))
print(s.repeatedSubstringPattern("aba"))
print(s.repeatedSubstringPattern("abab"))
print(s.repeatedSubstringPattern("abaababaab"))

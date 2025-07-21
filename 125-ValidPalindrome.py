'''
Problem Name: 125. Valid Palindrome
Attempted : # 21-07-2025
'''
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        sub = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        return sub == sub[::-1]
    

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
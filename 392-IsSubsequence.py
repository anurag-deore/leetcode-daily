'''
Problem Name: 392. Is Subsequence
Attempted : # 30-07-2025
'''


class Solution:
    def isSubsequence(self, t: str, s: str) -> bool:
        j = 0
        if (len(s) > len(t)):
            return False
        if len(s) == 0:
            return False
        for i in t:
            if i == s[j]:
                j += 1
            if (j == len(s)):
                return True
        return False


s = Solution()
print(s.isSubsequence("ahbgdc", "abc"))
print(s.isSubsequence("ahbgdc", ""))
print(s.isSubsequence("ahbgdc", "axc"))

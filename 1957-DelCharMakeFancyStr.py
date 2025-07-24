'''
Problem Name: 1957. Delete Characters to Make Fancy String
Attempted : # 25-07-2025
'''
# import time


class Solution:
    def makeFancyString(self, s: str) -> str:
        n = len(s)
        i = 2
        while n > 0 and i < n:
            # time.sleep(0.5)
            if s[i-2] == s[i-1] == s[i]:
                s = s[:i] + s[i+1:]
                n = len(s)
            else:
                i += 1
        return s


s = Solution()
print(s.makeFancyString("leeetcode"))
print(s.makeFancyString("aaabaaaa"))

'''
Problem Name: 1323. Maximum 69 Number
Attempted : # 21-08-2025
'''


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        try:
            i = s.index("6")
            s = s[:i] + "9" + s[i+1:]
        except:
            None
        return int(s)


s = Solution()
print(s.maximum69Number(9669))
print(s.maximum69Number(9996))
print(s.maximum69Number(9999))

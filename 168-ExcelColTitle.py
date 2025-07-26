'''
Problem Name: 168. Excel Sheet Column Title
Attempted : # 26-07-2025
'''


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = {i: chr(i + 65) for i in range(0, 26)}
        if columnNumber == 0:
            return ""
        columnNumber -= 1
        return self.convertToTitle(columnNumber//26) + letters[columnNumber % 26]


s = Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(28))
print(s.convertToTitle(701))
# print(s.convertToTitle(8001))
print(s.convertToTitle(2147483647))

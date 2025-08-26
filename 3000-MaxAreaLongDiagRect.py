'''
Problem Name: 3000. Maximum Area of Longest Diagonal Rectangle
Attempted : # 26-08-2025
'''


class Solution:
    def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
        maxdiagonals = 0
        maxArea = 0
        for i in dimensions:
            diag = i[0]*i[0] + i[1]*i[1]
            area = i[0] * i[1]
            print(diag, area)
            if diag > maxdiagonals:
                maxdiagonals = diag
                maxArea = area
            elif diag == maxdiagonals:
                maxArea = max(maxArea, area)
        return maxArea


s = Solution()
print(s.areaOfMaxDiagonal([[10, 3], [5, 9], [8, 3]]))
print(s.areaOfMaxDiagonalRectangle([[10, 3], [5, 9], [8, 3]]))
# print(s.areaOfMaxDiagonal([[2, 6], [5, 1], [3, 10], [8, 4]]))
# print(s.areaOfMaxDiagonal([[3, 4], [4, 3]]))

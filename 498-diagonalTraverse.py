'''
Problem Name: 498. Diagonal Traverse
Attempted : # 25-08-2025
'''
class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        result = []
        for d in range(m + n - 1):
            intermediate = []
            # Determine the starting point for this diagonal
            r = 0 if d < n else d - n + 1
            c = d if d < n else n - 1
            while r < m and c > -1:
                intermediate.append(mat[r][c])
                r += 1
                c -= 1
            # Reverse order for even diagonals
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result
    

s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.findDiagonalOrder([[1,2],[3,4]]))

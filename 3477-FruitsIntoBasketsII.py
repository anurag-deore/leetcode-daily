'''
Problem Name: 3477. Fruits Into Baskets II
Attempted : # 06-08-2025
'''

class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        popped = 0
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if baskets[j] >= fruits[i]:
                    baskets.pop(j)
                    popped += 1
                    break
        return len(fruits) - popped
    

s = Solution()
print(s.numOfUnplacedFruits([4,2,5], [3,5,4]))

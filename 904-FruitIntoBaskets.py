'''
Problem Name: 904. Fruit Into Baskets
Attempted : # 04-08-2025
'''


class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        # n = len(fruits)
        # if n < 2:
        #     return n
        # b1 = fruits[0]
        # b2 = fruits[1]
        # i = 2
        # maxSum = 2
        # maxcollected = 0
        # while i < n:
        #     # print( f'{b1},{b2} fruits[i] = {fruits[i]}, sum => {maxSum}\n')
        #     if fruits[i] == b1 or fruits[i] == b2:
        #         maxSum += 1
        #     else:
        #         b1 = fruits[i-1]
        #         b2 = fruits[i]
        #         maxSum = 2
        #     i += 1
        #     maxcollected = max(maxcollected, maxSum)
        # # print(b1, b2)
        # return maxcollected
        basket1 = 0
        max_fruits = 0
        fruit_count = {}
        for basket2 in range(len(fruits)):
            fruit_count[fruits[basket2]] = fruit_count.get(
                fruits[basket2], 0) + 1
            while len(fruit_count) > 2:
                fruit_count[fruits[basket1]] -= 1
                if fruit_count[fruits[basket1]] == 0:
                    del fruit_count[fruits[basket1]]
                basket1 += 1
            current_fruits = basket2 - basket1 + 1
            max_fruits = max(max_fruits, current_fruits)
        return max_fruits


s = Solution()
# print(s.totalFruit([1, 2, 1]))
print(s.totalFruit([0, 0, 1, 1]))
# print(s.totalFruit([0, 1, 4, 2, 3, 2, 2, 1]))

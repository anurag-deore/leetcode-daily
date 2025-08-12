'''
Problem Name: 412. Fizz Buzz
Attempted : # 12-08-2025
'''


class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        s = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                s.append("FizzBuzz")
            elif i % 3 == 0:
                s.append("Fizz")
            elif i % 5 == 0:
                s.append("Buzz")
            else:
                s.append(str(i))
        return s


s = Solution()
print(s.fizzBuzz(15))

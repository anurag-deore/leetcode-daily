'''
Problem Name: 1900. The Earliest and Latest Rounds Where Players Compete
Attempted : # 13-07-2025
'''

'''
Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
'''

class Solution:
  def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @functools.lru_cache(None)
        def simulateRounds(pos1, pos2, playersRemaining):
            # Base case: players are paired in this round
            if pos1 == pos2:
                return (1, 1)

            # Ensure consistent ordering
            if pos1 > pos2:
                return simulateRounds(pos2, pos1, playersRemaining)

            earliestRound = math.inf
            latestRound = -math.inf

            nextRoundCount = (playersRemaining + 1) // 2  # Players who proceed to next round

            # Try all valid future positions for our two players
            for i in range(1, pos1 + 1):  # Future pos of first player
                for j in range(pos1 - i + 1, pos2 - i + 1):  # Future pos of second player
                    combinedPos = i + j

                    # Validity check — ensure they can still meet
                    lowerLimit = pos1 + pos2 - playersRemaining // 2
                    if not (lowerLimit <= combinedPos <= nextRoundCount):
                        continue

                    early, late = simulateRounds(i, j, nextRoundCount)
                    earliestRound = min(earliestRound, early + 1)
                    latestRound = max(latestRound, late + 1)

            return (earliestRound, latestRound)

        # Map firstPlayer and secondPlayer to symmetric positions
        left = firstPlayer
        right = n - secondPlayer + 1
        return list(simulateRounds(left, right, n))

  def __repr__(self):
    return f"Solution()"

  def __str__(self):
    return "Solution class for Earliest and Latest Rounds problem"
  
s = Solution()
print(s.earliestAndLatest(11,2,4))
# print(s.earliestAndLatest(5,1,5))
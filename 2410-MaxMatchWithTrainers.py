'''
Problem Name: 2410. Maximum Matching of Players With Trainers
Attempted : # 13-07-2025
'''

class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        # print(players)
        # print(trainers)
        j = 0
        i = 0
        matches = 0
        # iterate = min(len(players),len(trainers))
        # print("iterate",iterate)
        while i < len(players) and j < len(trainers):
            # print("Round => ",i)
            # print(players[i],trainers[j])
            if(players[i]<=trainers[j]):
                i+=1
                j+=1
                matches += 1
            else:
                i+=1
        return matches
    

s = Solution()
print(s.matchPlayersAndTrainers([4,7,9],[8,2,5,8]))
print(s.matchPlayersAndTrainers([1,1,1],[10]))
print(s.matchPlayersAndTrainers([2,3,1,1,3],[2,4,2]))
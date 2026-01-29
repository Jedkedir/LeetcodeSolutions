class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = set()
        loser_count = Counter()
        for winner,loser in matches:
            loser_count[loser]+=1
            players.add(winner)
            players.add(loser)
        no_loss = []
        one_loss = []
        for player in sorted(list(players)):
            if loser_count[player] == 0:
                no_loss.append(player)
            elif loser_count[player] == 1:
                one_loss.append(player)
        return [no_loss,one_loss]
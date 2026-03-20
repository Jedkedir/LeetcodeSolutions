class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        p_ptr, t_ptr, matches = 0, 0, 0
        players.sort()
        trainers.sort()
        while p_ptr < len(players) and t_ptr < len(trainers):
            if players[p_ptr] <= trainers[t_ptr]:
                matches += 1
                p_ptr += 1
                t_ptr += 1
            else:
                t_ptr += 1
        return matches
class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_dist = abs(target[0]) + abs(target[1])
        for gx, gy in ghosts:
            ghost_dist = abs(target[0] - gx) + abs(target[1] - gy)
            if ghost_dist <= my_dist:
                return False
        return True
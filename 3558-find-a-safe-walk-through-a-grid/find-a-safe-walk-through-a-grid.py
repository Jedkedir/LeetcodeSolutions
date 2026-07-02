from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        min_cost = [[float('inf')] * n for _ in range(m)]
        q = deque()
        q.append((0, 0))
        min_cost[0][0] = grid[0][0]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    next_cost = min_cost[r][c] + grid[nr][nc]
                    if next_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = next_cost
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
        return health - min_cost[m - 1][n - 1] >= 1
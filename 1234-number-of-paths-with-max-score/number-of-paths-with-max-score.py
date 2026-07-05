class Solution:
    def pathsWithMaxScore(self, board: list[str]) -> list[int]:
        MOD = 1_000_000_007
        n = len(board)
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[n - 1][n - 1] = [0, 1]
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if board[r][c] == 'X' or dp[r][c][0] == -1:
                    continue
                curr_score, curr_paths = dp[r][c]
                for dr, dc in [(-1, 0), (0, -1), (-1, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and board[nr][nc] != 'X':
                        cell_val = 0
                        if board[nr][nc].isdigit():
                            cell_val = int(board[nr][nc])
                        next_score = curr_score + cell_val
                        if next_score > dp[nr][nc][0]:
                            dp[nr][nc][0] = next_score
                            dp[nr][nc][1] = curr_paths
                        elif next_score == dp[nr][nc][0]:
                            dp[nr][nc][1] = (dp[nr][nc][1] + curr_paths) % MOD
        max_score, paths = dp[0][0]
        return [max_score if max_score != -1 else 0, paths]
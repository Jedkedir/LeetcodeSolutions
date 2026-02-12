class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_to_color = defaultdict(int)
        color_counts = defaultdict(int)
        res = []
        for ball, color in queries:
            if ball in ball_to_color:
                old_color = ball_to_color[ball]
                color_counts[old_color] -= 1
                if color_counts[old_color] == 0:
                    del color_counts[old_color]
            ball_to_color[ball] = color
            color_counts[color] = color_counts[color] + 1
            res.append(len(color_counts))
        return res
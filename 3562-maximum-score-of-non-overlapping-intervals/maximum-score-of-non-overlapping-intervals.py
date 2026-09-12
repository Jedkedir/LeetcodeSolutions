class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        events = sorted(
            (start, end, weight, i) 
            for i, (start, end, weight) in enumerate(intervals)
        )
        events.sort(key=lambda x: x[1])
        end_times = [x[1] for x in events]
        dp = [[(0, ())] * 5 for _ in range(n + 1)]
        for i in range(1, n + 1):
            start, end, weight, orig_idx = events[i - 1]
            p = bisect_right(end_times, start - 1)
            for k in range(5):
                best = dp[i - 1][k]
                if k >= 1:
                    prev_weight, prev_tuple = dp[p][k - 1]
                    cand_weight = prev_weight + weight
                    cand_tuple = tuple(sorted(prev_tuple + (orig_idx,)))
                    if cand_weight > best[0]:
                        best = (cand_weight, cand_tuple)
                    elif cand_weight == best[0] and cand_weight > 0:
                        if cand_tuple < best[1]:
                            best = (cand_weight, cand_tuple)
                dp[i][k] = best
        best_weight = -1
        best_indices = ()
        for k in range(1, 5):
            w, idxs = dp[n][k]
            if w > best_weight:
                best_weight = w
                best_indices = idxs
            elif w == best_weight and w > 0:
                if idxs < best_indices:
                    best_indices = idxs
        return list(best_indices)
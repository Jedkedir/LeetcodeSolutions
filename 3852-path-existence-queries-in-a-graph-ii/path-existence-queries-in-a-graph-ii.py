class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        sorted_pairs = sorted((val, idx) for idx, val in enumerate(nums))
        pos = [0] * n
        for i, (_, original_idx) in enumerate(sorted_pairs):
            pos[original_idx] = i
        
        LOG = n.bit_length() + 1
        jump = [[0] * LOG for _ in range(n)]
        
        right = 0
        for i in range(n):
            while right + 1 < n and sorted_pairs[right + 1][0] - sorted_pairs[i][0] <= maxDiff:
                right += 1
            jump[i][0] = right
            
        for j in range(1, LOG):
            for i in range(n):
                jump[i][j] = jump[jump[i][j - 1]][j - 1]
                
        ans = []
        for u, v in queries:
            a, b = pos[u], pos[v]
            if a > b:
                a, b = b, a
            if a == b:
                ans.append(0)
                continue
                
            steps = 0
            curr = a
            for j in range(LOG - 1, -1, -1):
                if jump[curr][j] < b:
                    curr = jump[curr][j]
                    steps += (1 << j)
            
            if jump[curr][0] >= b:
                ans.append(steps + 1)
            else:
                ans.append(-1)
                
        return ans
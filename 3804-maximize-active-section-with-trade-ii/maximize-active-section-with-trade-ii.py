from itertools import pairwise

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: list[list[int]]) -> list[int]:
        ones = s.count('1')
        groups, g_idx = [], []
        
        for i, c in enumerate(s):
            if c == '0':
                if i > 0 and s[i - 1] == '0':
                    groups[-1][1] += 1
                else:
                    groups.append([i, 1])
            g_idx.append(len(groups) - 1)

        if not groups:
            return [ones] * len(queries)

        adj = [a[1] + b[1] for a, b in pairwise(groups)]
        m = len(adj)
        k = m.bit_length()
        st = [adj] + [[0] * m for _ in range(k - 1)]
        
        for j in range(1, k):
            for i in range(m - (1 << j) + 1):
                st[j][i] = max(st[j - 1][i], st[j - 1][i + (1 << (j - 1))])

        def query(l, r):
            if l > r:
                return 0
            p = (r - l + 1).bit_length() - 1
            return max(st[p][l], st[p][r - (1 << p) + 1])

        ans = []
        for l, r in queries:
            il, ir = g_idx[l], g_idx[r]
            left = groups[il][1] - (l - groups[il][0]) if il != -1 else -1
            right = r - groups[ir][0] + 1 if ir != -1 else -1

            r_bound = ir if s[r] == '1' else ir - 1
            start_adj, end_adj = il + 1, r_bound - 1

            res = ones
            if s[l] == '0' and s[r] == '0' and il + 1 == ir:
                res = max(res, ones + left + right)
            elif start_adj <= end_adj:
                res = max(res, ones + query(start_adj, end_adj))

            if s[l] == '0' and il + 1 <= r_bound:
                res = max(res, ones + left + groups[il + 1][1])

            if s[r] == '0' and il < ir - 1:
                res = max(res, ones + right + groups[ir - 1][1])

            ans.append(res)

        return ans
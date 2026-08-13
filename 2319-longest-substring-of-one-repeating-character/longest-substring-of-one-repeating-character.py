class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        self.max_len = [0] * (4 * self.n)
        self.pref_len = [0] * (4 * self.n)
        self.suff_len = [0] * (4 * self.n)
        self.pref_char = [''] * (4 * self.n)
        self.suff_char = [''] * (4 * self.n)
        self.s = list(s)
        self._build(1, 0, self.n - 1)

    def _merge(self, node: int, left_child: int, right_child: int, left_size: int, right_size: int):
        lc_pref_c, lc_pref_l = self.pref_char[left_child], self.pref_len[left_child]
        lc_suff_c, lc_suff_l = self.suff_char[left_child], self.suff_len[left_child]
        lc_max = self.max_len[left_child]

        rc_pref_c, rc_pref_l = self.pref_char[right_child], self.pref_len[right_child]
        rc_suff_c, rc_suff_l = self.suff_char[right_child], self.suff_len[right_child]
        rc_max = self.max_len[right_child]

        self.pref_char[node] = lc_pref_c
        self.pref_len[node] = lc_pref_l + (rc_pref_l if lc_pref_l == left_size and lc_pref_c == rc_pref_c else 0)

        self.suff_char[node] = rc_suff_c
        self.suff_len[node] = rc_suff_l + (lc_suff_l if rc_suff_l == right_size and rc_suff_c == lc_suff_c else 0)

        self.max_len[node] = max(lc_max, rc_max)
        if lc_suff_c == rc_pref_c:
            self.max_len[node] = max(self.max_len[node], lc_suff_l + rc_pref_l)

    def _build(self, node: int, l: int, r: int):
        if l == r:
            ch = self.s[l]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.pref_char[node] = ch
            self.suff_char[node] = ch
            return

        mid = (l + r) // 2
        lc, rc = 2 * node, 2 * node + 1
        self._build(lc, l, mid)
        self._build(rc, mid + 1, r)
        self._merge(node, lc, rc, mid - l + 1, r - mid)

    def update(self, node: int, l: int, r: int, idx: int, ch: str):
        if l == r:
            self.s[idx] = ch
            self.pref_char[node] = ch
            self.suff_char[node] = ch
            return

        mid = (l + r) // 2
        lc, rc = 2 * node, 2 * node + 1
        if idx <= mid:
            self.update(lc, l, mid, idx, ch)
        else:
            self.update(rc, mid + 1, r, idx, ch)
        self._merge(node, lc, rc, mid - l + 1, r - mid)


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: list[int]) -> list[int]:
        st = SegmentTree(s)
        ans = []
        n = len(s)
        for ch, idx in zip(queryCharacters, queryIndices):
            st.update(1, 0, n - 1, idx, ch)
            ans.append(st.max_len[1])
        return ans
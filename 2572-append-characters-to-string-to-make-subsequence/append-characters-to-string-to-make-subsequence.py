class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        reader,writer = 0,0
        n_s,n_t = len(s),len(t)
        while reader < n_s and writer < n_t:
            if s[reader] == t[writer]:
                writer += 1
            reader += 1
        return n_t - writer
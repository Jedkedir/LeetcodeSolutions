class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n:
            return False
        s1_count = Counter(s1)
        window_count = Counter(s2[:m])
        if s1_count == window_count:
            return True
        for i in range(m, n):
            window_count[s2[i]] += 1
            window_count[s2[i-m]] -= 1
            if window_count[s2[i-m]] == 0:
                del window_count[s2[i-m]]
            if s1_count == window_count:
                return True
        return False
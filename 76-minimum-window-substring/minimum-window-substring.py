class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s: return ""
        dict_t = Counter(t)
        required = len(dict_t)
        left, right = 0, 0
        formed = 0
        window_counts = defaultdict(int)
        res = float("inf"), None, None
        while right < len(s):
            ch = s[right]
            window_counts[ch]  += 1
            if ch in dict_t and window_counts[ch] == dict_t[ch]:
                formed += 1
            while left <= right and formed == required:
                ch = s[left]
                if right - left + 1 < res[0]:
                    res = (right - left + 1, left, right)
                window_counts[ch] -= 1
                if ch in dict_t and window_counts[ch] < dict_t[ch]:
                    formed -= 1
                left += 1    
            right += 1    
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]
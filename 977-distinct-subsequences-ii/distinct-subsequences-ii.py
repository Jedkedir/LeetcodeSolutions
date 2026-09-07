class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 1_000_000_007
        total = 1
        last = [0] * 26
        for char in s:
            idx = ord(char) - ord('a')
            new_subsequences = (total - last[idx]) % MOD
            total = (total + new_subsequences) % MOD
            last[idx] = (last[idx] + new_subsequences) % MOD
        return (total - 1) % MOD
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1_000_000_007
        size = r - l + 1
        dp = [1] * size
        
        for i in range(1, n):
            new_dp = [0] * size
            if i % 2 == 1:
                prefix_sum = 0
                for v in range(size):
                    new_dp[v] = prefix_sum
                    prefix_sum = (prefix_sum + dp[v]) % MOD
            else:
                suffix_sum = 0
                for v in range(size - 1, -1, -1):
                    new_dp[v] = suffix_sum
                    suffix_sum = (suffix_sum + dp[v]) % MOD
            dp = new_dp
            
        return (sum(dp) * 2) % MOD
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def count_waviness_up_to(limit_num: int) -> int:
            if limit_num <= 0:
                return 0
            s = str(limit_num)
            n = len(s)
            memo = {}
            def dp(idx: int, prev1: int, prev2: int, is_tight: bool, is_zero: bool):
                if idx == n:
                    return 0, 1 
                state = (idx, prev1, prev2, is_tight, is_zero)
                if state in memo:
                    return memo[state]
                limit = int(s[idx]) if is_tight else 9
                total_waviness = 0
                total_combinations = 0
                for d in range(limit + 1):
                    next_tight = is_tight and (d == limit)
                    next_zero = is_zero and (d == 0)
                    next_prev1 = d if not next_zero else -1
                    next_prev2 = prev1 if not next_zero else -1
                    suffix_waviness, suffix_combinations = dp(idx + 1, next_prev1, next_prev2, next_tight, next_zero)
                    wave_contribution = 0
                    if not is_zero and prev2 != -1:
                        if (prev2 < prev1 and prev1 > d) or (prev2 > prev1 and prev1 < d):
                            wave_contribution = suffix_combinations
                    total_waviness += suffix_waviness + wave_contribution
                    total_combinations += suffix_combinations
                memo[state] = (total_waviness, total_combinations)
                return memo[state]
            return dp(0, -1, -1, True, True)[0]
        return count_waviness_up_to(num2) - count_waviness_up_to(num1 - 1)
from math import lcm

class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        n = len(coins)
        
        # Precompute LCMs and signs for all non-empty subsets
        subsets = []
        for mask in range(1, 1 << n):
            current_lcm = 1
            bits = 0
            for i in range(n):
                if (mask >> i) & 1:
                    bits += 1
                    current_lcm = lcm(current_lcm, coins[i])
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))

        def count_multiples(m: int) -> int:
            total = 0
            for l, sign in subsets:
                total += sign * (m // l)
            return total

        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
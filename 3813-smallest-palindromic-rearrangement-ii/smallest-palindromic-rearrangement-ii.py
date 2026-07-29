class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        counts = Counter(s)
        half_counts = [counts[chr(c + 97)] // 2 for c in range(26)]
        mid = next((chr(c + 97) for c in range(26) if counts[chr(c + 97)] % 2), "")

        def count_ways(cnt):
            total = sum(cnt)
            res = 1
            for freq in cnt:
                res *= comb(total, freq)
                if res >= k:
                    return k
                total -= freq
            return res

        if count_ways(half_counts) < k:
            return ""

        left = []
        half_len = sum(half_counts)
        for _ in range(half_len):
            for i in range(26):
                if half_counts[i] == 0:
                    continue
                half_counts[i] -= 1
                ways = count_ways(half_counts)
                if ways >= k:
                    left.append(chr(i + 97))
                    break
                k -= ways
                half_counts[i] += 1

        return "".join(left) + mid + "".join(reversed(left))
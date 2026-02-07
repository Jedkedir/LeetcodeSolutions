class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for i in range(1, len(words)):
            common &= Counter(words[i])
        res = []
        for ch, count in common.items():
            res.extend([ch] * count)
        return res
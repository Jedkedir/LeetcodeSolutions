class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        res = []
        sortedLetters = sorted(count.items(), key=lambda item: item[1], reverse=True)
        for ch,freq in sortedLetters:
            res.append(ch * freq)
        return ''.join(res)
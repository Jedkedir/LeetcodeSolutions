class Solution:
    def mapWordWeights(self, words: list[str], weights: list[int]) -> str:
        ans = []
        for word in words:
            total_weight = sum(weights[ord(char) - 97] for char in word)
            remainder = total_weight % 26
            mapped_char = chr(122 - remainder)
            ans.append(mapped_char)
        return "".join(ans)
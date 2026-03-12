class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0
        n = len(word)
        for i in range(n):
            curr = set()
            for j in range(i, n):
                if word[j] not in vowels:
                    break
                curr.add(word[j])
                if len(curr) == 5:
                    count += 1
        return count
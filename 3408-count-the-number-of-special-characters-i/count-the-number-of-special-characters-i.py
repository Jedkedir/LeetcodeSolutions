class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set = set(word)
        special_count = 0
        for i in range(26):
            lower_char = chr(ord('a') + i)
            upper_char = chr(ord('A') + i)
            if lower_char in char_set and upper_char in char_set:
                special_count += 1
        return special_count
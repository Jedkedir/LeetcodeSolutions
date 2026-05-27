class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        state = {}
        for char in word:
            if char.islower():
                if char not in state:
                    state[char] = 1
                elif state[char] == 2:
                    state[char] = -1
            else:
                lower = char.lower()
                if lower in state and state[lower] == 1:
                    state[lower] = 2
                elif lower not in state:
                    state[lower] = -1
        return sum(1 for status in state.values() if status == 2)
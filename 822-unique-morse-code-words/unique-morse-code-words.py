class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        seen = set()
        for word in words:
            transformation = []
            for ch in word:
                i = ord(ch) - ord('a')
                transformation.append(morse[i])
            seen.add("".join(transformation))
        return len(seen)
            
    
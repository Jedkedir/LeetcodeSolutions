class Solution:
    def isPalindrome(self, s: str) -> bool:
        de = deque([])
        for char in s:
            if char.isalnum():
                de.append(char.lower())

        while len(de) > 1:
            if de.popleft() != de.pop():
                return False
        return True        
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] == -asteroid:
                    stack.pop()
                elif stack[-1] < -asteroid:
                    stack.pop()
                    continue
                break
            else:
                stack.append(asteroid)
        return stack
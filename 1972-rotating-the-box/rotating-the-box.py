class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        for r in range(rows):
            empty = cols - 1
            for c in range(cols - 1, -1, -1):
                if boxGrid[r][c] == '#':
                    boxGrid[r][c], boxGrid[r][empty] = boxGrid[r][empty], boxGrid[r][c]
                    empty -= 1
                elif boxGrid[r][c] == '*':
                    empty = c - 1
        res = [['' for _ in range(rows)] for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                res[c][rows - 1 - r] = boxGrid[r][c]
        return res
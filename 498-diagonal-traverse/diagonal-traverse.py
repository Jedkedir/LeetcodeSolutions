class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = defaultdict(list)
        for row in range(rows):
            for col in range(cols):
                diagonals[row + col].append(mat[row][col])
        res = []
        for k in range(rows + cols - 1):
            if k % 2 == 0:
                res = [*res,*diagonals[k][::-1]]
            else:
                res = [*res,*diagonals[k]]
        return res
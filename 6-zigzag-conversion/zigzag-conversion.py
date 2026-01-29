class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        cycle = 2 * numRows - 2
        rows = [''] * numRows
        for i, char in enumerate(s):
            position = i % cycle
            if position < numRows:
                row = position
            else:
                row = cycle - position
            rows[row] += char
        return ''.join(rows)